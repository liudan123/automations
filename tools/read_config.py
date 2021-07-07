# -*- encoding:utf-8 -*-

import configparser
class ReadConfig:

    @staticmethod
    def get_config(file_path,section,option):
        cf = configparser.ConfigParser()  #创建实例
        # cf = configparser.RawConfigParser()
        cf.read(file_path)    #获取文件
        # return cf[section][option]
        return cf.get(section,option)
