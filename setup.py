'''
File: setup.py
Created on: Thursday, 2023-10-05 @ 19:27:12
Author: HackXIt (<hackxit@gmail.com>)
-----
Last Modified: Thursday, 2023-10-05 @ 19:29:05
Modified By:  HackXIt (<hackxit@gmail.com>) @ HACKXIT
-----
'''
import os
import subprocess

# Name of the virtual environment
env_name = "env"

# Create the virtual environment
subprocess.call(f'python -m venv {env_name}', shell=True)

# Activate the virtual environment
activate_this = os.path.join(env_name, 'bin', 'activate_this.py')
exec(open(activate_this).read(), {'__file__': activate_this})

# Install packages from requirements.txt
subprocess.call(f'{env_name}/bin/pip install -r requirements.txt', shell=True)