#!/usr/bin/python
# -*- coding: utf-8 -*-

#Primero subproceso de importación, este es el módulo que utilizaremos para interactuar con el cmd.
import subprocess
#El módulo del sistema operativo en Python proporciona funciones para interactuar con el sistema operativo.
import os
import errno
import glob
import shutil
#----------------Baner---------------------------
print (".     __      __  _   ___   _             ")
print (".     \ \    / / | | | __| | |        ")
print (".      \ \/\/ /  |_| | _|  |_|        ")
print (".       \_/\_/   (_) |_|   (_)            ")
print (".    Autor: Luishino Pericena Choque        ")
print (".    https://lpericena.blogspot.com/      ")
#Creamos una carpeta/folder donde se gurdara las claves de wifi
try:
    os.mkdir('./wifi')
except OSError as error:
    if error.errno != errno.EEXIST:
        raise
#Muestra todas las redes wifi que la pc fue conectada
show = subprocess.check_output(['netsh', 'wlan', 'show', 'profile'])
print show
networks = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'])
print networks
#exporta las claves de wifi en archivos .xml
a = subprocess.check_output(['netsh', 'wlan', 'export', 'profile','key=clear']).decode('utf-8').split('\n')
#Mover archivos .xml a la carpeta wifi
source_dir = './' #Inicio de la carpeta 
dst = './wifi' #Nueva carpeta destinario 
files = glob.iglob(os.path.join(source_dir, "*.xml"))#englobar los archivos a mover
for file in files:
    if os.path.isfile(file):
        shutil.move(file, dst) #Mover todos los archivos a una nueva carpeta
