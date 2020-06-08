#!/usr/bin/python3
# _*_coding:utf-8_*_


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...'%n)
        r = '200 OK'


def produce(c):
    # c.send(None)
    next(c)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCE] Produceing %s...'%n)
        r = c.send(n)
        print('[PRODUCE] Consumer return: %s'%r)
        print('-----------------')
    c.close()

c = consumer()
produce(c)
