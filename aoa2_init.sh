#!/bin/bash

/home/pi/AndroidCarAudioDock/aoa2enable.py $1 $2
(sleep 1s ; alsaloop -P hw:1,0,0 -C hw:2,0,0 -f S16_LE -r 44100 -t 50000 -S 2) &