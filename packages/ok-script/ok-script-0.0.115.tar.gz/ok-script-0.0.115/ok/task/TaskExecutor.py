import sys
import threading
import time
from typing import Tuple

from ok.capture.BaseCaptureMethod import CaptureException
from ok.capture.adb.DeviceManager import DeviceManager
from ok.gui.Communicate import communicate
from ok.logging.Logger import get_logger
from ok.scene.Scene import Scene
from ok.stats.StreamStats import StreamStats
from ok.task.BaseTask import BaseTask
from ok.task.TriggerTask import TriggerTask

logger = get_logger(__name__)


class TaskDisabledException(Exception):
    pass


class CannotFindException(Exception):
    pass


class FinishedException(Exception):
    pass


class WaitFailedException(Exception):
    pass


class TaskExecutor:
    current_scene: Scene | None = None
    last_scene: Scene | None = None
    frame_stats = StreamStats()
    _frame = None
    paused = True
    ocr = None
    pause_start = time.time()
    pause_end_time = time.time()
    _last_frame_time = 0

    def __init__(self, device_manager: DeviceManager,
                 wait_until_timeout=10, wait_until_before_delay=1, wait_until_check_delay=0,
                 exit_event=None, trigger_tasks=[], onetime_tasks=[], scenes=[], feature_set=None,
                 ocr=None,
                 config_folder=None, debug=False):
        self.device_manager = device_manager
        self.feature_set = feature_set
        self.wait_until_check_delay = wait_until_check_delay
        self.wait_until_before_delay = wait_until_before_delay
        self.wait_scene_timeout = wait_until_timeout
        self.exit_event = exit_event
        self.debug_mode = False
        self.debug = debug
        self.ocr = ocr
        self.current_task = None
        self.trigger_tasks = trigger_tasks
        self.onetime_tasks = onetime_tasks
        self.scenes = scenes
        self.config_folder = config_folder or "config"
        self.trigger_task_index = -1
        for scene in self.scenes:
            scene.executor = self
            scene.feature_set = self.feature_set
        for task in self.trigger_tasks:
            task.set_executor(self)
        for task in self.onetime_tasks:
            task.set_executor(self)
        self.thread = threading.Thread(target=self.execute, name="TaskExecutor")
        self.thread.start()

    @property
    def interaction(self):
        return self.device_manager.interaction

    @property
    def method(self):
        return self.device_manager.capture_method

    def nullable_frame(self):
        return self._frame

    def check_frame_and_resolution(self, supported_ratio, min_size, time_out=3):
        if supported_ratio is None or min_size is None:
            return True, '0x0'
        self.device_manager.update_resolution_for_hwnd()
        start = time.time()
        frame = None
        while frame is None and time.time() - start < time_out:
            frame = self.method.get_frame()
            time.sleep(0.1)
        if frame is None:
            logger.error(f'check_frame_and_resolution failed can not get frame after {time_out}')
            return False, '0x0'
        width = self.method.width
        height = self.method.height
        if height == 0:
            actual_ratio = 0
        else:
            actual_ratio = width / height

        # Parse the supported ratio string
        supported_ratio = [int(i) for i in supported_ratio.split(':')]
        supported_ratio = supported_ratio[0] / supported_ratio[1]

        # Calculate the difference between the actual and supported ratios
        difference = abs(actual_ratio - supported_ratio)
        support = difference <= 0.01 * supported_ratio
        if not support:
            logger.error(f'resolution error {width}x{height} {frame is None}')
        if not support and frame is not None:
            communicate.screenshot.emit(frame, "resolution_error")
        # Check if the difference is within 1%
        if support and min_size is not None:
            if width < min_size[0] or height < min_size[1]:
                support = False
        return support, f"{width}x{height}"

    def can_capture(self):
        return self.method is not None and self.interaction is not None and self.interaction.should_capture()

    def next_frame(self):
        self.reset_scene()
        while not self.exit_event.is_set():
            if self.can_capture():
                self._frame = self.method.get_frame()
                if self._frame is not None:
                    self._last_frame_time = time.time()
                    height, width = self._frame.shape[:2]
                    if height <= 0 or width <= 0:
                        logger.warning(f"captured wrong size frame: {width}x{height}")
                        self._frame = None
                    return self._frame
            self.sleep(0.001)
        raise FinishedException()

    def is_executor_thread(self):
        return self.thread == threading.current_thread()

    def connected(self):
        return self.method is not None and self.method.connected()

    @property
    def frame(self):
        while self.paused and not self.debug_mode:
            self.sleep(1)
        if self.exit_event.is_set():
            logger.info("Exit event set. Exiting early.")
            sys.exit(0)
        if self._frame is None:
            return self.next_frame()
        else:
            return self._frame

    def sleep(self, timeout):
        """
        Sleeps for the specified timeout, checking for an exit event every 100ms, with adjustments to prevent oversleeping.

        :param timeout: The total time to sleep in seconds.
        """
        if self.debug_mode:
            time.sleep(timeout)
            return
        self.reset_scene()
        self.frame_stats.add_sleep(timeout)
        self.pause_end_time = time.time() + timeout
        while True:
            if self.exit_event.is_set():
                logger.info("Exit event set. Exiting early.")
                return
            if self.current_task and not self.current_task.enabled:
                raise TaskDisabledException()
            if not (self.paused or (
                    self.current_task is not None and self.current_task.paused) or self.interaction is None or not self.interaction.should_capture()):
                to_sleep = self.pause_end_time - time.time()
                if to_sleep <= 0:
                    return
                time.sleep(to_sleep)
            time.sleep(0.1)

    def pause(self, task=None):
        if task is not None:
            if self.current_task != task:
                raise Exception(f"Can only pause current task {self.current_task}")
        else:
            self.paused = True
            communicate.executor_paused.emit(self.paused)
        self.reset_scene()
        self.pause_start = time.time()

    def start(self):
        if self.paused:
            self.paused = False
            communicate.executor_paused.emit(self.paused)
            self.pause_end_time += self.pause_start - time.time()

    def wait_scene(self, scene_type, time_out, pre_action, post_action):
        return self.wait_condition(lambda: self.detect_scene(scene_type), time_out, pre_action, post_action)

    def wait_condition(self, condition, time_out=0, pre_action=None, post_action=None, wait_until_before_delay=-1,
                       raise_if_not_found=False):
        if wait_until_before_delay == -1:
            wait_until_before_delay = self.wait_until_before_delay
        self.reset_scene()
        start = time.time()
        if time_out == 0:
            time_out = self.wait_scene_timeout
        while not self.exit_event.is_set():
            if pre_action is not None:
                pre_action()
            self.sleep(wait_until_before_delay)
            self.next_frame()
            result = condition()
            self.add_frame_stats()
            result_str = list_or_obj_to_str(result)
            if result:
                logger.debug(
                    f"found result {result_str} {(time.time() - start):.3f} delay {wait_until_before_delay} {self.wait_until_check_delay}")
                return result
            if post_action is not None:
                post_action()
            if time.time() - start > time_out:
                logger.info(f"wait_until timeout {condition} {time_out} seconds")
                break
            self.sleep(self.wait_until_check_delay)
        if raise_if_not_found:
            raise WaitFailedException()
        return None

    def reset_scene(self):
        self._frame = None
        self.last_scene = self.current_scene or self.last_scene
        self.current_scene = None

    def next_task(self) -> Tuple[BaseTask | None, bool]:
        if self.exit_event.is_set():
            logger.error(f"next_task exit_event.is_set exit")
            return None, False
        cycled = False
        for onetime_task in self.onetime_tasks:
            if onetime_task.enabled:
                return onetime_task, True
        if len(self.trigger_tasks) > 0:
            if self.trigger_task_index >= len(self.trigger_tasks) - 1:
                self.trigger_task_index = -1
                cycled = True
            self.trigger_task_index += 1
            task = self.trigger_tasks[self.trigger_task_index]
            if task.enabled and task.should_check_trigger():
                return task, cycled
        return None, cycled

    def active_trigger_task_count(self):
        return len([x for x in self.trigger_tasks if x.enabled])

    def execute(self):
        logger.info(f"start execute")
        while not self.exit_event.is_set():
            if self.paused:
                logger.info(f'executor is paused sleep')
                self.sleep(1)
            task, cycled = self.next_task()
            if not task:
                time.sleep(1)
                continue
            if cycled:
                self.next_frame()
                self.detect_scene()
            elif time.time() - self._last_frame_time > 1:
                logger.warning(f'processing cost too much time, get new frame')
                self.next_frame()
                self.detect_scene()
            try:
                if task.trigger():
                    self.current_task = task
                    self.current_task.running = True
                    communicate.task.emit(self.current_task)
                    if cycled or self._frame is None:
                        self.next_frame()
                    self.current_task.run()
                    if not isinstance(self.current_task, TriggerTask):
                        self.current_task.disable()
                    self.current_task = None
                    communicate.task.emit(task)
                if self.current_task is not None:
                    self.current_task.running = False
                    if not isinstance(self.current_task, TriggerTask):
                        communicate.task.emit(self.current_task)
                    self.current_task = None
            except FinishedException:
                logger.info(f"FinishedException, breaking")
                break
            except Exception as e:
                if isinstance(e, CaptureException):
                    communicate.capture_error.emit()
                name = ""
                if self.current_task is not None:
                    name = self.current_task.name
                    if not isinstance(self.current_task, TriggerTask):
                        self.current_task.disable()
                logger.error(f"{name} exception", e)
                if self._frame is not None:
                    communicate.screenshot.emit(self.frame, name)
                self.current_task = None
                communicate.task.emit(None)

        logger.debug(f'exit_event is set, destroy all tasks')
        for task in self.onetime_tasks:
            task.on_destroy()
        for task in self.trigger_tasks:
            task.on_destroy()

    def add_frame_stats(self):
        self.frame_stats.add_frame()
        mean = self.frame_stats.mean()
        if mean > 0:
            communicate.frame_time.emit(mean)
            communicate.fps.emit(round(1000 / mean))
            scene = "None"
            if self.current_scene is not None:
                scene = self.current_scene.name or self.current_scene.__class__.__name__
            communicate.scene.emit(scene)

    def latest_scene(self):
        return self.current_scene or self.last_scene

    def detect_scene(self, scene_type=None):
        latest_scene = self.latest_scene()
        if latest_scene is not None:
            # detect the last scene optimistically
            if latest_scene.detect(self._frame):
                self.current_scene = latest_scene
                return latest_scene
        for scene in self.scenes:
            if scene_type is not None and not isinstance(scene, scene_type):
                continue
            if scene != latest_scene:
                if scene.detect(self._frame):
                    self.current_scene = scene
                    logger.debug(f"TaskExecutor: scene changed {scene.__class__.__name__}")
                    return scene
        if self.current_scene is not None:
            logger.debug(f"TaskExecutor: scene changed to None")
            self.current_scene = None
        return self.current_scene

    def stop(self):
        logger.info('stop')
        self.exit_event.set()

    def wait_until_done(self):
        self.thread.join()

    def get_all_tasks(self):
        return self.onetime_tasks + self.trigger_tasks

    def get_task_by_class_name(self, class_name):
        for onetime_task in self.onetime_tasks:
            if onetime_task.__class__.__name__ == class_name:
                return onetime_task
        for trigger_task in self.trigger_tasks:
            if trigger_task.__class__.__name__ == class_name:
                return trigger_task


def list_or_obj_to_str(val):
    if val is not None:
        if isinstance(val, list):
            return ', '.join(str(obj) for obj in val)
        else:
            return str(val)
    else:
        return None
