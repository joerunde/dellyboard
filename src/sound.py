import os
from sys import platform

from playsound import playsound


class Sound(object):
    '''Plays a sound
    '''
    def __init__(self, sound_file: str, key_combo: str):
        self._sound_file = sound_file
        self._key_combo = key_combo

    @property
    def key_combo(self):
        return self._key_combo

    @property
    def sound_file(self):
        return self._sound_file

    def play(self):
        if platform.startswith('linux'):
            os.system('aplay {}'.format(self.sound_file))
            pass
        else:
            playsound(self.sound_file)
