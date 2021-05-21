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

        # print("---------------------------")
        # old_play_process = None
        # if self._play_process is not None:
        #     print("pressed\t\t", time.time())
        #     #if self._play_process.is_alive():
        #     #if self._play_process.
        #     old_play_process = self._play_process
        #     # self._play_process.terminate()
        #     print("terminated\t", time.time())
        # #self._play_process = Popen(target=self._play)
        # self._play_process = Popen(["python3", "-m", "src._sound", self.sound_file])
        # print("created\t\t", time.time())
        # # self._play_process.start()
        #
        #
        # if old_play_process:
        #     go_dumb_shit = threading.Thread(target=self._godumbshit, args=[old_play_process])
        #     go_dumb_shit.start()
    #
    # def _godumbshit(self, old_process):
    #     time.sleep(0.25)
    #     old_process.terminate()
    #
    # def _play(self):
    #     print("started\t", time.time())
    #     if platform.startswith('linux'):
    #         os.system('aplay {}'.format(self.sound_file))
    #         pass
    #     else:
    #         playsound(self.sound_file)
