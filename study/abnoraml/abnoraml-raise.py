#!/usr/bin/python3
# _*_coding:utf-8_*_


# err_raise.py
#class FooError(ValueError):
#    pass
#
#def foo(s):
#    n = int(s)
#    if n == 0:
#        raise FooError('invalid value: %s' %s)
#    return 10/n
#
#foo('0')

class ShortInputException(Exception):
    def __init__(self,length,aleast):
        self.length = length
        self.aleast = aleast

def main():
    try:
        s = input('aaaa: ')
        if len(s) < 3:
            raise ShortInputException(len(s), 3)
    except ShortInputException as e:
        print("ShortInputException: 输入长度是:%d, 长度至少应是:%d"%(e.length, e.aleast))
    else:
        print(s)

main()
