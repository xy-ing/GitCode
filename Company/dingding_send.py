#!/usr/bin/python
# _*_coding:utf-8_*_

import requests
import json
import time
import socke
import fcntl
import struct


class Get_Local_Ip(object):
    def get_ip_address(self, ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,
            struct.pack('256s', ifname[:15]))[20:24])

class DingTalk_Base(object):
    def __init__(self):
        self.__headers = {'Content-Type': 'application/json;charset=utf-8'}
        self.url = ''

    def send_msg(self, text, ip_addr, now_time):
        json_text = {
            # "msgtype": "text",
            # "text": {
            #     "content": text
            # },
            "msgtype": "markdown",
            "markdown": {"title": "机器进程监控",
                         "text": "### 矿机(ddam)进程监控\n" +
                                '> 当前所在机器: %s\n\n'%ip_addr +
                                '> 当前时间: %s\n\n' %now_time +
                                '> 进程状态: %s\n\n' %text
                        },
            "at": {
                "atMobiles": [
                    "18514278603"
                ],
                "isAtAll": True
            }
        }
        return requests.post(self.url, json.dumps(json_text), headers=self.__headers).content


class DingTalk_Disaster(DingTalk_Base):
    def __init__(self):
        super(DingTalk_Disaster, self).__init__()
        # 填写机器人的url
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=dbf2fda849cac25c9d6544f8f0e5970b37396f3a1e43e39b8544c1f511be42c7'


if __name__ == '__main__':
    ding = DingTalk_Disaster()
    ding.send_msg('wec a', "192.168.1.14", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
