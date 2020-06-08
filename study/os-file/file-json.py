#!/usr/bin/python3
# _*_coding:utf-8_*_

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student("Bob", 22, 88)

def student2dict(std):
    return {
        "name": std.name,
        "age": std.age,
        "score": std.score
    }


print(json.dumps(s, default=student2dict))
#print(json.dumps(s))
