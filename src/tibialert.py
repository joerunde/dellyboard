from threading import Timer
from playsound import playsound
import typing


class TibiAlert(object):
    def __init__(self, timeout_seconds: float, sound_file: str, key_combo: str, name: str = "Unnamed Alert"):
        self._timer: Timer = None

        self._timeout_seconds = timeout_seconds
        self._sound_file = sound_file
        self._name = name
        self._key_combo = key_combo

        self._chained_alerts: typing.List[TibiAlert] = []

    @property
    def timeout_seconds(self):
        return self._timeout_seconds

    @property
    def key_combo(self):
        return self._key_combo

    @property
    def name(self):
        return self._name

    @property
    def sound_file(self):
        return self._sound_file

    @property
    def chained_alerts(self):
        return self._chained_alerts

    def chain(self, alert: 'TibiAlert'):
        if len(alert.chained_alerts) == 0:
            self._chained_alerts.append(alert)
        else:
            raise ValueError("nah dog")

    def notify(self):
        self._reset_timer()
        for a in self._chained_alerts:
            a.notify()

    def _reset_timer(self):
        if self._timer is not None:
            self._timer.cancel()
        self._timer = Timer(self._timeout_seconds, self._alert)
        self._timer.start()
        print("Set {} timer for {} seconds".format(self._name, self._timeout_seconds))

    def _alert(self):
        playsound(self._sound_file)
