import argparse
import json
import os

from src.board import Board
from src.profile import Profile
from src.sound import Sound

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Delly Soundboard (for yelling at cyclists)')
    parser.add_argument('-c', '--config', default='config/alerts.json')
    parser.add_argument('-s', '--sounds', default='sounds')

    args = parser.parse_args()

    with open(args.config) as alert_file:
        cfg = json.load(alert_file)

        profiles = []
        for name, profile in cfg.items():
            hotkey = profile["hotkey"]
            sounds = [Sound(os.path.join(args.sounds, sound_file), hkey)
                      for hkey, sound_file in profile["sounds"].items()]
            profiles.append(Profile(name, hotkey, sounds))

        board = Board(profiles)
        board.run()
