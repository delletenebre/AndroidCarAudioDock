#!/usr/bin/python

import subprocess

if __name__ == '__main__':
    output = subprocess.check_output(['ps', '-ef'])
    for line in output.split('\n'):
        if 'sensors/buttons.py' in line:
            print line