from src.tibialert import TibiAlert
import os

class TibiAlertFactory:
    sound_directory = "."

    @classmethod
    def set_sounds_dir(cls, dir: str):
        cls.sound_directory = dir

    @classmethod
    def create_alert(cls, name: str, alert_json: dict):
        sound_file = os.path.join(cls.sound_directory, alert_json["sound"])
        if not os.path.isfile(sound_file):
            raise ValueError("{} is not a file!".format(sound_file))
        return TibiAlert(alert_json["timeout_s"],
                         sound_file,
                         alert_json["hotkey"],
                         name)
