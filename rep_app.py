import os
import socket
import subprocess

hostname = socket.gethostname()
my_ip = socket.gethostbyname(hostname)

if my_ip == '18.217.40.214':
    subprocess.call('cmd /k cd ../../ && python app.py')
elif my_ip != '18.217.40.214':
    print('You are not authorized to use this app')