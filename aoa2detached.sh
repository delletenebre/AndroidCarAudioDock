#!/bin/bash

ps -ef | grep "sensors/buttons.py" | awk '{print $2}' | xargs sudo kill -9
ps -ef | grep "sensors/ds18b20.py" | awk '{print $2}' | xargs sudo kill -9
