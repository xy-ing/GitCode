#!/usr/bin/python3
# _*_coding:utf-8_*_

#try:
#    print('try...')
#    r = 10/0
#    print('result: ',r)
#except ZeroDivisionError as e:
#    print('except: ',e)
#finally:
#    print('finally...')
#print("END")
import time

try:
    f = open('test.txt','r')
    while True:
        content = f.readline()
        if len(content) == 0:
            break
        time.sleep(2)
        print(content)
except Exception as e:
    print('没有这个文件')
    print(e)
