#!/bin/bash

cp ./systemfiles/dock.rules /etc/udev/rules.d/
chmod +x ./aoa2detached.sh
chmod +x ./launcher.sh
chmod +x ./aoa2initialization.py
chmod +x ./aoa2start.sh
chmod +x ./aoa2write.py
chmod +x ./aoa2hid.py

chmod +x ./sensors/buttons.py
chmod +x ./sensors/ds18b20.py

