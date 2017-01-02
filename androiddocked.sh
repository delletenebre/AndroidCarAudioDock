#!/bin/bash

/usr/local/bin/aoa2usbaudio.py $1 $2
(sleep 1s ; alsaloop -P hw:1,0,0 -C hw:2,0,0 -f S16_LE -r 44100 -t 50000 -S 2)&
#(sleep 1s ; /usr/local/bin/aoa2hid.py 18d1 2d02)
exit 0
