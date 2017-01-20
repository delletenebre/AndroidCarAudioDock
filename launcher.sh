#!/bin/bash

/home/pi/AndroidCarAudioDock/aoa2initialization.py $1 $2

/home/pi/AndroidCarAudioDock/sensors/buttons.py
/home/pi/AndroidCarAudioDock/sensors/ds18b20.py

echo /home/pi/AndroidCarAudioDock/route_audio.sh $1 $2 | at now