import threading
import time
from subprocess import Popen
from sys import platform


class Player:
    '''Starts playing a sound when initialized. Non-Blocking.
    Playback can be terminated, but will wait a configurable bit of time so it can be nice and smooth'''

    min_playback: float

    def __init__(self, sound_file):
        self.start_time = time.time()

        if platform.startswith('linux'):
            self._play_process = Popen(["aplay", sound_file])
        else:
            self._play_process = Popen(["python3", "-m", "src._play_mac_windows", sound_file])

    def terminate(self, force_now=False):
        if force_now:
            print("forcing immediate termination")
            self._play_process.kill()
        else:
            terminate_thread = threading.Thread(target=self._async_terminate, args=[self._play_process])
            terminate_thread.start()

    def _async_terminate(self, old_process):
        '''Kills the old play process asynchronously'''
        min_time = self.min_playback
        end_time = min_time + self.start_time
        to_sleep = end_time - time.time()
        if to_sleep > 0:
            print("sleeping", to_sleep)
            time.sleep(to_sleep)
        else:
            print("Not sleeping, terminating now")

        old_process.kill()
