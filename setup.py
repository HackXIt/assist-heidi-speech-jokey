'''
File: setup.py
Created on: Thursday, 2023-10-05 @ 19:27:12
Author: HackXIt (<hackxit@gmail.com>)
-----
Last Modified: Thursday, 2023-10-05 @ 19:32:01
Modified By:  HackXIt (<hackxit@gmail.com>) @ HACKXIT
-----
'''
import os
import platform
import subprocess

def create_venv():
    venv_cmd = ['python', '-m', 'venv', 'venv']
    if platform.system() == 'Windows':
        python_activation = 'venv\\Scripts\\activate'
    else:
        python_activation = 'source venv/bin/activate'
    subprocess.run(venv_cmd)
    subprocess.run(python_activation, shell=True)
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

if __name__ == '__main__':
    create_venv()
