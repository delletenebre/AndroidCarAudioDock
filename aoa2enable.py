#!/usr/bin/python

import usb.core
import usb.util
import struct
import time
import sys

APP = {
    'manufacturer': 'delletenebre',
    'model': 'car',
    'version': '1.0',
    'description': '',
    'url': '',
    'serial': ''
}


def enable_accessory_mode(dev):
    type_out = usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_OUT
    version = dev.ctrl_transfer(
        usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_IN, 51, 0, 0, 2)

    version = struct.unpack('<H', version)[0]
    if version < 2:
        raise ValueError("AOA version is not compatible")

    # Send identity strings
    assert dev.ctrl_transfer(
        type_out, 52, 0, 0, APP['manufacturer']) == len(APP['manufacturer'])

    assert dev.ctrl_transfer(
        type_out, 52, 0, 1, APP['model']) == len(APP['model'])

    assert dev.ctrl_transfer(
        type_out, 52, 0, 2, APP['description']) == len(APP['description'])

    assert dev.ctrl_transfer(
        type_out, 52, 0, 3, APP['version']) == len(APP['version'])

    assert dev.ctrl_transfer(
        type_out, 52, 0, 4, APP['url']) == len(APP['url'])

    assert dev.ctrl_transfer(
        type_out, 52, 0, 5, APP['serial']) == len(APP['serial'])

    # Enable Audio support
    dev.ctrl_transfer(type_out, 58, 1, 0, None)

    # Start in accessory mode
    dev.ctrl_transfer(type_out, 53, 0, 0, None)

    time.sleep(1)


if __name__ == '__main__':
    # Find device by VID & PID
    dev = usb.core.find(idVendor=int(sys.argv[1], 16),
                        idProduct=int(sys.argv[2], 16))
    if dev is not None:
        enable_accessory_mode(dev)

    # dev = usb.core.find(idVendor=0x18D1)
    # if dev is None:
    #     raise ValueError("Device in accessory mode not found")

    # endpoint_in = dev[0][(0, 0)][0]

    # # while True:
    # try:
    #     data = endpoint_in.read(1024, 0)
    #     message = ''.join([chr(x) for x in data])

    # except usb.core.USBError as e:
    #     print("failed to send IN transfer")
    #     print(e)
    #     break
    # usb.util.dispose_resources(dev)
