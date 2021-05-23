import argparse
import json
import os

from src.board import Board
from src.player import Player
from src.profile import Profile
from src.sound import Sound

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Delly Soundboard (for yelling at cyclists)')
    parser.add_argument('-c', '--config', default='config/sounds.json')
    parser.add_argument('-s', '--sounds', default='sounds')

    args = parser.parse_args()

    with open('config/config.json') as cfg_file:
        Player.min_playback = json.load(cfg_file)['min_playback_seconds']

    with open(args.config) as alert_file:
        profile_config = json.load(alert_file)

        profiles = []
        for name, profile in profile_config.items():
            hotkey = profile["hotkey"]
            sounds = [Sound(os.path.join(args.sounds, sound_file), hkey)
                      for hkey, sound_file in profile["sounds"].items()]
            profiles.append(Profile(name, hotkey, sounds))

        board = Board(profiles)
        board.run()
