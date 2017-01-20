#!/usr/bin/python

import os
from gpiozero import Button
from signal import pause


buttons = {
    '27': {
        'button': Button(27),
        'is_held': False,
        'name': 'time'
    },
    '17': {
        'button': Button(17),
        'is_held': False,
        'name': 'menu'
    },
    '22': {
        'button': Button(22),
        'is_held': False,
        'name': 'navi'
    },
    '23': {
        'button': Button(23),
        'is_held': False,
        'name': 'info'
    },
    '24': {
        'button': Button(24),
        'is_held': False,
        'name': 'voice'
    }
}


def send(pin, action):
    os.system("/home/pi/AndroidCarAudioDock/aoa2write.py \"<{0}:{1}>\"".format(pin, action))


def check(current_button):
    pin = str(current_button.pin.number)
    button = buttons[pin]
    name = button['name'] + 'btn'

    if current_button.is_held:
        send(name, 'hold')
        button['is_held'] = True
    else:
        if button['is_held']:
            button['is_held'] = False
        else:
            send(name, 'press')


def main():
    for key in buttons:
        buttons[key]['button'].when_released = check
        buttons[key]['button'].when_held = check
    pause()


if __name__ == '__main__':
    main()
