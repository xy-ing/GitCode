#!/usr/bin/python
# _*_coding:utf-8_*_

import os
import time


g_path = "/var/log/disk/"
log_dir = "/root/"
#end_str = "Generated 28000000 nonces in"
end_str = "Generated"
lsdir = os.listdir(g_path)
file_nums = len(lsdir)


# 记录未完成的日志
def log_file(now_time, l_dir):
    real_log_file = log_dir + l_dir
    with open(real_log_file, "a") as f:
        f.write(now_time + " " + l_dir + " 未完成\n")
        # f.write("-"*30 + "\n")


def monitor_log_file():
    num = 0
    # 循环日志目录下文件
    for file_op in lsdir:
        real_filedir = g_path + file_op
        # 打开文件
        with open(real_filedir, "r") as f:
            all_lines = f.readlines()
            last_line = all_lines[-1]
            # 对比完成度
            if end_str in last_line:
                print(real_filedir + " 已完成")
                num += 1
            else:
                now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                log_file(now_time, file_op)
    return num


# 开始执行P盘命令
def join_com(file_fish_num):
    if file_fish_num == file_nums:
        time.sleep(5)
        # start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        print("开始执行")
        os.system("nohup top -d 5 -n 500 -b >> /root/top.txt &")
        os.system("nohup top -d 5 -n 500 -b >> /root/top1.txt &")

file_fish_num = monitor_log_file()
join_com(file_fish_num)
