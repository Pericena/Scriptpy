# -*- coding: utf-8 -*-
#powerhell python setup.py py2exe

import sys
from distutils.core import setup

kwargs = {}
if 'py2exe' in sys.argv:
    import py2exe
	


    kwargs = {
        'console' : [{
            'script'         : 'WiFi.py',
            'description'    : 'Descripcion del programa.',
            'icon_resources' : [(90, 'icon.ico')]
            }],
        'zipfile' : None,
        'options' : { 'py2exe' : {
            'dll_excludes'   : ['w9xpopen.exe'],
            'bundle_files'   : 1,
            'compressed'     : True,
            'optimize'       : 2
            }},
         }

setup(
    name='WiFi',
    author='Luishiño',
    author_email='lpericena@gmail.com',
    **kwargs)
