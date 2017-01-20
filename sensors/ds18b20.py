#!/usr/bin/python

import glob
import time
import os


def read_temp_raw():
    f = open(glob.glob('/sys/bus/w1/devices/28*')[0] + '/w1_slave', 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = round(float(temp_string) / 1000.0, 1)
        # temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c  # , temp_f


def main():
    while True:
        try:
            os.system("/home/pi/AndroidCarAudioDock/aoa2write.py \"<outtemp:%s>\"" % read_temp())
            time.sleep(3)
        except:
            pass


if __name__ == '__main__':
    main()
