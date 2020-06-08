#!/usr/bin/python
# _*_coding:utf-8_*_


import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError as e:
        print('cannot open', arg)
        print(e)
    else:
        print(arg,'has',len(f.readlines()), 'lines')
        f.close
