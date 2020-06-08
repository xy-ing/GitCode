#!/usr/bin/python3
# _*_coding:utf-8_*_

from io import StringIO

f = StringIO("Hello!\nHi!\nGoodbye!")

while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
