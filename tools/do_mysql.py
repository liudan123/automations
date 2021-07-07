# -*- encoding:utf-8 -*-

import sys
import json
sys.setdefaultencoding('utf-8')
import mysql.connector
from project_path import *
from read_config import ReadConfig

class DoMysql:

    def do_mysql(self,query_sql,state = 'all'):   #query查询语句  state-->all  多条   one   一条
        db_config = eval(ReadConfig().get_config(case_config_path,'DB','db_config'))   #利用这个类从配置文件里面读取db info

        #创建数据库连接
        con = mysql.connector.connect(**db_config)

        #建立游标cursor
        cursor = con.cursor()

        #执行sql语句
        cursor.execute(query_sql)

        if state == 1:
            res = cursor.fetchone()  # 元组  只对一条数据

        else:
            res = cursor.fetchall()   #列表   多条数据

        #关闭游标
        cursor.close()

        #关闭连接
        con.close()
        return res

if __name__ == '__main__':
    from get_data import GetData
    # query_sql = 'SELECT Id FROM loan a WHERE MemberID=42551'
    query_sql = 'select max(Id) from loan where MemberID={0}'.format(getattr(GetData, 'loan_member_id'))

    res = DoMysql().do_mysql(query_sql)
    print res
    print (res[0][0])