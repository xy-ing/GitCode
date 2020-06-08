#!/usr/bin/python3
# _*_coding:utf-8_*_


import logging

# 获取logger对象
logger = logging.getLogger()

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('/python_workspaces/study/logs/log.log')

# 再创建一个handler，用于控制台输出
ch = logging.StreamHandler()

# 创建一个formatter，两个handler使用相同的日志模式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 绑定formatter到handler上
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 绑定handler到logger对象上
logger.addHandler(fh)
logger.addHandler(ch)

# 设置日志级别
logger.setLevel(logging.WARNING)

logging.debug('logger debug message')
logging.info('logger info messsage')
logging.warning('logger warning message')
logging.error('logger error message')
logging.critical('logger critical message')

