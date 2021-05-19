from pynput import keyboard
from src.tibialert import TibiAlert
from src.tibialert_factory import TibiAlertFactory
import typing
import sys


class TibiAlerter:

    def __init__(self, config_json: dict):

        self.alerts_by_hotkey: typing.Dict[str, TibiAlert] = {}

        for alert_name, alert_config in config_json.items():
            tibi_alert = TibiAlertFactory.create_alert(alert_name, alert_config)
            if tibi_alert.key_combo not in self.alerts_by_hotkey:
                self.alerts_by_hotkey[tibi_alert.key_combo] = tibi_alert
            else:
                self.alerts_by_hotkey[tibi_alert.key_combo].chain(tibi_alert)
        print(self.alerts_by_hotkey)

    def run(self):
        notify_dict = {key_combo: alert.notify for key_combo, alert in self.alerts_by_hotkey.items()}

        # Really dumb hack, because windows :(
        # Make dang sure that whatever dumb terminal you run in doesn't let the interrupt signal be swallowed
        notify_dict["<ctrl>+c"] = sys.exit

        with keyboard.GlobalHotKeys(notify_dict) as hotkey_listener:
            hotkey_listener.join()
