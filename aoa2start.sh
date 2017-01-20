#!/bin/bash

/home/pi/AndroidCarAudioDock/aoa2initialization.py $1 $2

(single.py -c /home/pi/AndroidCarAudioDock/sensors/buttons.py) &
(single.py -c /home/pi/AndroidCarAudioDock/sensors/ds18b20.py) &

(sleep 1s ; alsaloop -P hw:1,0,0 -C hw:2,0,0 -f S16_LE -r 44100 -t 50000 -S 2) &
