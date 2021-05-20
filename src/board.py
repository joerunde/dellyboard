import sys
from typing import List

from pynput import keyboard

from src.profile import Profile


class Board:
    '''Holds a set of soundboard profiles.
    Accepts keyboard input and plays sounds from the current profile
    '''

    def __init__(self, profiles: List[Profile]):
        self._profiles = profiles
        self._current_profile = profiles[0]

        self._swap_profile_map = {}
        for profile in profiles:
            print("Registering callback for profile", profile.name)

            def swapper(profile):
                def _swap():
                    print("Swapping to profile:", profile.name)
                    self._current_profile = profile

                return _swap

            self._swap_profile_map[profile.hotkey] = swapper(profile)

        all_sound_hotkeys = set()
        for p in profiles:
            all_sound_hotkeys.update(set(list(p.map.keys())))
            print(all_sound_hotkeys)

        self._sound_fn_map = {}
        for hotkey in all_sound_hotkeys:
            def player(hotkey):
                def _sound():
                    print("playing for hotkey", hotkey)
                    if hotkey in self._current_profile.map:
                        self._current_profile.map[hotkey]()
                    else:
                        print("No sound on profile")
                return _sound

            print("Adding fn for hotkey:", hotkey)
            self._sound_fn_map[hotkey] = player(hotkey)

    def run(self):
        '''Start listening for inputs'''
        print("hello")
        notify_dict = self._sound_fn_map
        notify_dict.update(self._swap_profile_map)

        # Really dumb hack, because windows :(
        # Make dang sure that whatever dumb terminal you run in doesn't let the interrupt signal be
        # swallowed
        notify_dict["<ctrl>+c"] = sys.exit

        notify_dict["<ctrl>+6"]()

        print(notify_dict)
        with keyboard.GlobalHotKeys(notify_dict) as hotkey_listener:
            hotkey_listener.join()

    def _swap(self, profile):
        print("Swapping to profile:", profile.name)
        self._current_profile = profile
