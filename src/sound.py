from src.play import Play


class Sound(object):
    '''Plays a sound
    '''

    # Static list of playing sounds
    _playing_list = []

    def __init__(self, sound_file: str, key_combo: str):
        self._sound_file = sound_file
        self._key_combo = key_combo

    @property
    def key_combo(self):
        return self._key_combo

    @property
    def sound_file(self):
        return self._sound_file

    @classmethod
    def terminate_all(cls, force_now=False):
        while len(cls._playing_list) > 0:
            player = cls._playing_list.pop(0)
            player.terminate(force_now=force_now)

    def play(self):
        Sound.terminate_all()

        player = Play(self.sound_file)
        self._playing_list.append(player)
