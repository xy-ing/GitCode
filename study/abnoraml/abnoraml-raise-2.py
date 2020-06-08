#!/usr/bin/python3
# _*_coding:utf-8_*_


class Test(object):
    def __init__(self, switch):
        self.switch = switch
    
    def calc(self, a, b):
        try:
            return a/b
        except Exception as e:
            if self.switch:
                print("捕获开启，已经捕获到了异常，信息如下")
                print(e)
            else:
                raise

a = Test(True)
a.calc(11,0)
print('---------------------------------------------------')
a = Test(False)
a.calc(11,0)
