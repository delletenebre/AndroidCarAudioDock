#!/bin/bash

#Update Sources and install necessary software for dock
#sudo apt-get update
#sudo apt-get install git at

#Install pyusb
#git clone https://github.com/walac/pyusb
#cd pyusb
#sudo python setup.py install

#Install docking related files
cp ./systemfiles/dock.rules /etc/udev/rules.d/
chmod +x ./launcher.sh
chmod +x ./aoa2_init.sh
chmod +x ./aoa2detached.sh
chmod +x ./aoa2enable.py
chmod +x ./aoa2hid.py
chmod +x ./aoa2write.py

chmod +x ./sensor_ds18b20.py
chmod +x ./setupgpio.sh
