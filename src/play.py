import threading
import time
from subprocess import Popen


class Play:
    '''Starts playing a sound when initialized. Non-Blocking.
    Playback can be terminated, but will wait a configurable bit of time so it can be nice and smooth'''

    min_playback: float

    def __init__(self, sound_file):
        self.start_time = time.time()
        self._play_process = Popen(["python3", "-m", "src._sound", sound_file])

    def terminate(self, force_now=False):
        if force_now:
            self._play_process.terminate()
        else:
            go_dumb_shit = threading.Thread(target=self._async_terminate, args=[self._play_process])
            go_dumb_shit.start()

    def _async_terminate(self, old_process):
        '''Kills the old play process asynchronously so that'''
        min_time = self.min_playback
        end_time = min_time + self.start_time
        to_sleep = max(end_time - time.time(), 0.1)
        print("sleeping", to_sleep)
        time.sleep(to_sleep)

        old_process.terminate()