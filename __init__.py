# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Función que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys
import time
from subprocess import Popen

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'android' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)
import pyndroid

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

"""
    Automate Android devices
"""

platform = sys.platform
if platform == "win32":
    pyndroid.PATH = cur_path + 'win' + os.sep
elif platform == "darwin":
    pyndroid.PATH = cur_path + 'mac' + os.sep

if module == "unlock":
    pin = GetParams('pin')
    type_ = GetParams('type')
    wake_screen = GetParams('wake')
    try:
        if type_ == "pin":
            pyndroid.unlock_with_pin(pin)
        if type_ == "swipe":
            pyndroid.unlock_with_swipe(wake_screen=wake_screen)

    except Exception as e:
        PrintException()
        raise e

if module == "start":
    try:
        app = GetParams('app')
        start = pyndroid.start_app(app)

    except Exception as e:
        PrintException()
        raise e

if module == "shell":
    app = GetParams('shell')
    result = GetParams('result')
    try:

        con = pyndroid.execute_by_shell(app)[0].decode('utf-8')

        if result:
            SetVar(result, con)

    except Exception as e:
        PrintException()
        raise e

if module == "touch":
    try:
        x = GetParams('x')
        y = GetParams('y')

        pyndroid.tap(x, y)
        time.sleep(1)

    except Exception as e:
        PrintException()
        raise e

if module == "write":
    text = GetParams("text")

    try:
        write = pyndroid.write(text)
        time.sleep(1)

    except Exception as e:
        PrintException()
        raise e

if module == "swipe":
    start = GetParams("start")
    end = GetParams("end")
    duration = GetParams("duration")

    try:
        start = eval(start)
        end = eval(end)
        swipe = pyndroid.swipe(start[0], start[1], end[0], end[1], duration)
        print(swipe)
        time.sleep(1)

    except Exception as e:
        PrintException()
        raise e

if module == "sendKeyEvent":
    event = GetParams("event")

    try:
        pyndroid.execute_by_key_event(event)

    except Exception as e:
        PrintException()
        raise e

if module == "devices":
    long_output = GetParams("long_output")
    result = GetParams("result")
    try:
        devices_list = pyndroid.list_devices(long_output=long_output)
        devices_list = devices_list.split("\r\n")[1:]
        devices = []
        for device in devices_list:
            if device:
                devices.append(device)

        SetVar(result, devices)

    except Exception as e:
        PrintException()
        raise e
