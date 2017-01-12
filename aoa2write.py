#!/usr/bin/python

import usb.core
import usb.util
import sys


def write(data):
    dev = usb.core.find(idVendor=0x18D1)
    if dev is not None:
        dev[0][(0, 0)][1].write(data, 100)
        usb.util.dispose_resources(dev)


if __name__ == '__main__':
    write(sys.argv[1])
