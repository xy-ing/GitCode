#!/usr/bin/python3
# _*_coding:utf-8_*_


try:
    runoob()
except AssertionError as error:
    print(error)
else:
    try:
        with open('while-1.py','r') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行.')
