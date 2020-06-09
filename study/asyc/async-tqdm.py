#!/usr/bin/python3
# _*_coding:utf-8_*_


from tqdm import tqdm
from time import sleep

# for i in tqdm(range(1000)):
#     sleep(0.1)
with tqdm(total=1000) as pbar:
    for i in range(1000):
        pbar.update(1)
