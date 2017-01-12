#!/usr/bin/python

import time
import subprocess

if __name__ == '__main__':
    while True:
        try:
            proc = subprocess.Popen(['python', 'ds18b20.py'], stdout=subprocess.PIPE)
            for line in proc.stdout:
                print 'temp: ' + line.replace('\n', '').replace('\r', '')
            time.sleep(2)
        except:
            print("failed to send IN transfer")
            proc.kill()
            break
