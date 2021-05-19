import argparse
import json

from src.tibialert_factory import TibiAlertFactory
from src.tibialerter import TibiAlerter

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Hotkey alerts (for Tibia)')
    parser.add_argument('-c', '--config', default='config/alerts.json')
    parser.add_argument('-s', '--sounds', default='sounds')

    args = parser.parse_args()

    with open(args.config) as alert_file:
        TibiAlertFactory.set_sounds_dir(args.sounds)
        TibiAlerter(json.load(alert_file)).run()
