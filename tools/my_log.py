# -*- encoding:utf-8 -*-

import logging
from project_path import *

class MyLog:

    def mylog(self,msg,level):
        #定义一个日志收集器my_logger
        my_logger = logging.getLogger('interface')

        #设置收集日志的级别，不设置的话，默认收集warning以上的日志
        my_logger.setLevel('DEBUG')

        #设定日志输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        #创建我们自己的输出渠道（输出也要设定级别，否则也默认输出warning及以上级别的日志）
        fh = logging.FileHandler(test_logger_path)
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        #将收集和输出对接，指定输出渠道
        my_logger.addHandler(fh)

        #收集日志
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.debug(msg)
        elif level == 'WARNING':
            my_logger.debug(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        #关闭渠道（日志收集器）否则会重复收集、重复输出
        my_logger.removeHandler(fh)


    def debug(self,msg):
        self.mylog(msg,'DEBUG')

    def info(self,msg):
        self.mylog(msg,'INFO')

    def warning(self, msg):
        self.mylog(msg, "WARNING")

    def error(self, msg):
        self.mylog(msg, "ERROR")

    def critical(self, msg):
        self.mylog(msg, "CRITICAL")

