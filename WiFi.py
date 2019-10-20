#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import os
import errno
import glob
import shutil
print (".     __      __  _   ___   _             ")
print (".     \ \    / / | | | __| | |        ")
print (".      \ \/\/ /  |_| | _|  |_|        ")
print (".       \_/\_/   (_) |_|   (_)            ")
print (".    Autor: Luishino Pericena Choque        ")
print (".    https://lpericena.blogspot.com/      ")
try:
    os.mkdir('./wifi')
except OSError as error:
    if error.errno != errno.EEXIST:
        raise
a = subprocess.check_output(['netsh', 'wlan', 'export', 'profile','key=clear']).decode('utf-8').split('\n')
source_dir = './' 
dst = './wifi'  
files = glob.iglob(os.path.join(source_dir, "*.xml"))
for file in files:
    if os.path.isfile(file):
        shutil.move(file, dst) 
