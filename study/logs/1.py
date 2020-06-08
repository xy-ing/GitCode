#!/usr/bin/python3
# _*_coding:utf-8_*_


import logging

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',          # 日志格式
                    datefmt='%Y-%m-%d %H:%M:%S',    # 时间格式：2018-11-12 23:50:21
                    filename='/tmp/test.log',    # 日志的输出路径
                    filemode='a')                      # 追加模式

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
