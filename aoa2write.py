#!/usr/bin/python

import usb.core
import usb.util
import sys


def write(data):
    products = [0x2d00, 0x2d01, 0x2d02, 0x2d03, 0x2d04, 0x2d05]
    for pid in products:
        dev = usb.core.find(idVendor=0x18D1, idProduct=pid)
        if dev is not None:
            dev[0][(0, 0)][1].write(data, 100)
            usb.util.dispose_resources(dev)
            break


if __name__ == '__main__':
    write(sys.argv[1])
