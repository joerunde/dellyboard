from typing import List

from src.sound import Sound


class Profile:
    '''Holds a profile of sounds
    '''

    def __init__(self, name: str, hotkey: str, sounds: List[Sound]):
        self._name = name
        self._sounds = sounds
        self._hotkey = hotkey

        # map a dict of key combo -> function that plays a sound
        self._map = {sound.key_combo: sound.play for sound in self.sounds}

    @property
    def name(self):
        return self._name

    @property
    def sounds(self):
        return self._sounds

    @property
    def hotkey(self):
        return self._hotkey

    @property
    def map(self):
        return self._map
