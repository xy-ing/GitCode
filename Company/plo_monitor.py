#!/usr/bin/python
# _*_coding:utf-8_*_


import time
import os
import re
import psutil
from dingding_send import * 


def course(course_name):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == course_name:
            a = "aaaaaaaaaaa"
            return a
    else:
        a ="bbb"
        return a


#b = Get_Local_Ip()
#print(b.get_ip_address("ens33"))
a = course("top")
print(a)


