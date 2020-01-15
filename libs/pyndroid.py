
import os
from subprocess import Popen, PIPE
import time

PATH = ""
ENV = os.environ.copy()

# Function definitions


def list_devices(long_output=False):
    """

    :param long_output: boolean, by default is False
    :return:
    """

    adb = [PATH + 'adb', 'devices', '-l'] if long_output else [PATH + 'adb', 'devices']
    con = Popen(adb, env=ENV, stdout=PIPE, stderr=PIPE)
    return con.communicate()[0].decode('utf-8')


def press_unlock():
    adb = [PATH + 'adb', 'shell', 'input', 'keyevent', '26']
    con = Popen(adb, env=ENV, stdout=PIPE, stderr=PIPE)


def press_home():
    adb = [PATH + 'adb', 'shell', 'input', 'keyevent', '3']
    con = Popen(adb, env=ENV, stdout=PIPE, stderr=PIPE)


def press_menu():
    adb = [PATH + 'adb', 'shell', 'input', 'keyevent', '82']
    con = Popen(adb, env=ENV, stdout=PIPE, stderr=PIPE)


def start_app(app):
    adb = [PATH + 'adb', 'shell', 'am', 'start', '-n', app]
    con = Popen(adb, env=ENV, stdout=PIPE, stderr=PIPE)


def write(text):
    """

    :param text: string
    :return:
    """
    adb = [PATH + 'adb', 'shell', 'input', 'text', text]
    con = Popen(adb, env=ENV, stdout=PIPE, stderr=PIPE)


def tap(x, y):
    """

    :param x: int, coordinate in x
    :param y: int, coordinate in y
    :return:
    """
    x = str(x)
    y = str(y)
    adb = [PATH + 'adb', 'shell', 'input', 'tap', x, y]
    con = Popen(adb, env=ENV, stdout=PIPE, stderr=PIPE)


def swipe(x1, y1, x2, y2, duration=100):
    """

    :param x1: int, first coordinate in x
    :param y1: int, first coordinate in y
    :param x2: int, last coordinate in x
    :param y2: int, last coordinate in y
    :param duration: int, time
    :return:
    """
    x1 = str(x1)
    y1 = str(y1)
    x2 = str(x2)
    y2 = str(x2)
    duration = str(duration)

    adb = [PATH + 'adb', 'shell', 'input', 'swipe', x1, y1, x2, y2, duration]
    con = Popen(adb, env=ENV, stdout=PIPE, stderr=PIPE)


def execute_by_key_event(code):
    """

    :param code: int, keyEvent
    :return:
    """
    adb = [PATH + 'adb', 'shell', 'input', 'keyevent', str(code)]
    con = Popen(adb, env=ENV, stdout=PIPE, stderr=PIPE)


def execute_by_shell(params):
    """

    :param params: str,  commands
    :return:
    """
    adb = [PATH + 'adb', 'shell', params]
    con = Popen(adb, env=ENV, stdout=PIPE, stderr=PIPE)


def unlock_with_pin(pin, wake_screen=True):
    """

    :param pin: str,
    :param wake_screen: bool, by default is True
    :return:
    """
    if wake_screen:
        press_unlock()
    time.sleep(1)
    write(pin)
    time.sleep(1)
    execute_by_key_event(66)


def unlock_with_swipe(wake_screen=True):
    """

    :param wake_screen: bool, by default is True
    :return:
    """
    if wake_screen:
        press_unlock()
    time.sleep(1)
    swipe(400, 800, 400, 100, 250)

