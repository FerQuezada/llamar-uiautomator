# !/usr/bin/python
# C:\Users\fer_q\AppData\Local\Android\Sdk
"""

"""
from subprocess import check_call, check_output
import time
import datetime
import argparse
from uiautomator import Device
import pytz
import opciones

#---------------------------------------------------------


def wifi(device, serial, wifi_status):
    # Menu_click
    # d(text='ENC', className='android.widget.Switch').click()
    if wifi_status == 'ON':
        if d( text='Apagado', className='android.widget.Switch').exists:
            time.sleep(1)
            print("Status: Wi-Fi Apagado")
            d(text='Apagado', className='android.widget.Switch').click()
            time.sleep(5)
            if d(text='ENC', className='android.widget.Switch').exists:
                print("Wi-Fi Encendido --- Turned On")
        else:
            print("Wi-Fi estaba encendido - No need Turn on")

    if wifi_status == 'OFF':
        if d( text='ENC', className='android.widget.Switch').exists:
            time.sleep(1)
            print("Status: Wi-Fi Encendido")
            d(text='ENC', className='android.widget.Switch').click()
            time.sleep(5)
            if d(text='Apagado', className='android.widget.Switch').exists:
                print("Wi-Fi Apagado --- Turned Off")
        else:
            print("Wi-Fi estaba Apagado - No need Turn Off")

    check_call(
        ['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
    time.sleep(3)

    return

    '''
    try:
        d(text='Apagado', className='android.widget.Switch').click()
        time.sleep(5)
        d.press.back()
        #time.sleep(1)
        #d.press.home()

        return
    except:
        d(text='ENC', className='android.widget.Switch').click()
        time.sleep(5)
        d.press.back()
        return
    '''

def lee_entero():
    while True:
        entrada = raw_input("What do you want to do? ")
        try:
            entrada = int(entrada)
            return entrada
        except ValueError:
            print "Not a valid option"


def colgar():

    while True:
        answer = raw_input("Make another call? press y or ")
        if answer == "y":
            # check_call(['adb', 'shell', 'input', 'keyevent 6'])
            return 1
        elif answer != "":
            exit()
            print "Not a valid option"


def entero():
    while True:
        any = raw_input("Press any number to end call")
        try:
            any = int(any)
            return any
        except ValueError:
            print "Not a valid option"


# ---------------------------------------------------------------------------


if __name__ == "__main__":
    # No arguments are call
    # args = get_arguments()
    while (1):
        # a = devname()
        # print(a)

        print("1 Local number")
        print("2 National number")
        print("3 International number")
        print("4 Emergency number")

        while True:
            entrada = lee_entero()
            if entrada == 1:
                numero = raw_input("Enter the number you want to call")
                opciones.llamada(numero)
                # opciones.local()
                break
            elif entrada == 2:
                # opciones.national()
                break
            elif entrada == 3:
                # opciones.international()
                break
            elif entrada == 4:
                # opciones.emergency()
                break
            else:
                print("Not a valid option")

        # print("Enter a phone number to call")

    # print()
        respuesta = colgar()
        # print("Want to finish? press 1")
        # answer = raw_input("Want to make another call? press any number")
        # respuesta = entero(answer)

        if respuesta == '1':
            exit()

