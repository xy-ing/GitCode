#!/usr/bin/python3
# _*_coding:utf-8_*_


#def foo():
#    print("starting...")
#    while True:
#        res = yield 4
#        print('res:',res)
#
#g = foo()
#print(next(g))
#print("*"*20)
#print(g.send(7))
#print(next(g))
def func():
    for i in range(10):
        yield i 
        print("start %s",i)

f = func()
for d in f:
    print(d)
    print("-"*10)
