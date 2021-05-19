from unittest import TestCase
from unittest import mock
import unittest
from src import tibialert
from threading import Event

REAL_SOUND = "../sounds/Jsquad.wav"


class TestTibiAlert(TestCase):

    def test_notify_triggers_alert_later(self):
        subject = tibialert.TibiAlert(0.01, "test any sound")

        alerted = Event()
        with mock.patch.object(subject, '_alert', side_effect=lambda: alerted.set()) as mock_alert:
            subject.notify()
            alerted.wait(2)
            mock_alert.assert_called()

    def test_alert_plays_correct_sound(self):
        expected_file = "test any file"
        subject = tibialert.TibiAlert(0.01, expected_file)

        alerted = Event()
        with mock.patch('src.tibialert.playsound', side_effect=lambda _: alerted.set()) as mock_playsound:
            subject.notify()
            alerted.wait(2)
            mock_playsound.assert_called_with(expected_file)
