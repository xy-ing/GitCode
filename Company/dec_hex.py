#!/usr/bin/python3
#_*_coding:utf-8_*_


# 转账(data参数)补位
def cover(end_num):
    wei = len(str(end_num))
    buwei = 64 - wei
    new_end_num = buwei * "0" + str(end_num)
    print("\033[1;32mHex: \033[0m", new_end_num)


# 转账(data参数)转换进制
def oct_hex(number):
    ddam_num = int(number + "000000000")
    hex_num = hex(ddam_num)
    cover(hex_num[2:])


# 转账(data参数)入口
def tran():
    ori_number = input('\033[1;32mPlease input your monry: \033[0m')
    list_num = list(ori_number)
    if "." in list_num:
        list_num.remove('.')
        int_number = ''.join(list_num)
        oct_hex(int_number)
    else:
        oct_hex(ori_number)


# 查询(data参数)
def inqu(account):
    way_name = "70a08231"
    account = account[1:]
    print("\033[1;32mAccount: \033[0m{}".format(way_name+account))


# 主函数
if __name__ == '__main__':
    lie = '''\033[1;32mPlease Choice Your Operation!\033[0m

   \033[1m1、转账(transfer)
   2、查询(Inquire)\033[0m
    '''
    print(lie)
    judge = input("\033[1;32mPlease input 1 or 2: \033[0m")
    if judge == "1":
        tran()
    elif judge == "2":
        acc = input("\033[1;32mPlease input your account: \033[0m")
        inqu(acc)
    else:
        print("\033[1;31mPlease input 1 or 2!!!\033[0m")
