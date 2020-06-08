#!/usr/bin/python3
# _*_coding:utf-8_*_


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        if number == 10:
            break
        number += 1

for i in get_primes(1):
    print(i)
