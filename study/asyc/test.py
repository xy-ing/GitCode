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
def gen2():
    while True:
        total = yield from gen()
        print('加和总数是：',total)

def main():
    # g1 = gen()
    # g1.send(None)
    # g1.send(2)
    # g1.send(3)
    # g1.send(None)
    g2 = gen2()
    g2.send(None)
    g2.send(2)
    g2.send(3)
    g2.send(None)

main()
