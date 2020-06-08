#!/usr/bin/python3
# _*_coding:utf-8_*_


from io import StringIO
f = StringIO()
f.write("Hello")
f.write(" ")
f.write("World!")
print(f.getvalue())
