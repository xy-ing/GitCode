#!/usr/bin/python3
# _*_coding:utf-8_*_


import time,threading


# 新线程执行的代码
def loop():
    print("Thread %s is running..."%(threading.current_thread().name))
    n = 0
    while n < 5:
        n = n + 1
        print("Thread %s >>> %s."%(threading.current_thread().name, n))
        time.sleep(1)
    print("Thread %s ended."%threading.current_thread().name)


print("Thread %s is running..."%threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print("Thread %s ended..."%threading.current_thread().name)
