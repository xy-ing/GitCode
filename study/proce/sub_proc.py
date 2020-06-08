#!/usr/bin/python3
# _*_coding:utf-8_*_


import subprocess

print("$nslookup www.python.org")

r = subprocess.call(['nslookup','www.python.org'])
print('Exit code...',r)
