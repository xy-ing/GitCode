#!/usr/bin/python
# _*_coding:utf_*_

import time
from pymysql import *


def add_nonce():
    i = 0
    card = 28000000
    conn = connect(host="192.168.1.249", port=3306, user="root", password="plo_123.*", database="plo_record")
    cs = conn.cursor()
    while i <= 23:
        num = i * card
        sql = "INSERT INTO nonce_start(nonce) VALUES(%s)"%num
        cs.execute(sql)
        conn.commit()
        i += 1
    cs.close()
    conn.close()
    print("Ok")

add_nonce()
