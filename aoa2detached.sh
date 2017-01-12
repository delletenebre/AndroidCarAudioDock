#!/bin/bash

ps -ef | grep "sensor_ds18b20.py" | awk '{print $2}' | xargs sudo kill -9
