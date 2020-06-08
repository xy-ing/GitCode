#!/usr/bin/python3
# _*_coding:utf-8_*_


def gen():
    total = 0
    while True:
        x = yield
        print('加',x)
        if not x:
            break
        total += x
    return total

def main():
    g1 = gen()
    g1.send(None)
    g1.send(2)
    g1.send(3)
    g1.send(None)

main()
