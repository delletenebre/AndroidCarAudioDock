#!/bin/bash

# enable BCM 17 // open relay +12v (BAT)
echo 17 > /sys/class/gpio/export
echo high > /sys/class/gpio/gpio17/direction

exit 0
