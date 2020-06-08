#!/usr/bin/python
# _*_coding:utf-8_*_
import os


g_path = "/data/"


new_miner_addr = "DD11d0b206ca9f980acf614005157557cf4e5360bea7a68c98c21c989d4c709ba5"
join_str = "_"
file_name = []
lsdir = os.listdir(g_path)


for dir_data in lsdir:
	miner = ["DD11d0b206ca9f980acf614005157557cf4e5360bea7a68c98c21c989d4c709ba5"]
	real_dir = g_path+dir_data
	file_show = os.listdir(real_dir)
	miner_address = sorted(file_show)[0]
	old_addr = real_dir + "/" + str(miner_address)
	m = miner_address.split("_")[1]
	n = miner_address.split("_")[-1]
	miner.append(m)
	miner.append(n)
	new_addr = real_dir + "/" + join_str.join(miner)
	#os.system("mv %s %s"%(old_addr, new_addr))
        print(new_addr, old_addr)

	


