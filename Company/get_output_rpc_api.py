#!/usr/bin/python
#_*_coding:utf-8_*_

import json
import requests
import datetime
import time

glo_main_net_url = 'https://rpc.ddam.one'
glo_headers = {"Content-Type":"application/json"}


def get_output_miner(miner_addr):
    (miner_key, miner_value), = miner_addr.items()

    data_json = {
        "method": "Gx_balance",
        "params": [miner_value],
        "jsonrpc": "2.0",
        "id": 1
    }

    get_result = requests.post(url=glo_main_net_url, data=json.dumps(data_json), headers=glo_headers)
    rea = json.loads(get_result.text)
    print("%s 的值是： %s"%(miner_key, rea['result']['data']))


aa = {"wuhan":"DD3f7bbdccda4a5e7f245e659abe90286cadf95b0f5c5546bb4971fd6c8d4ffde7"}

get_output_miner(aa)

