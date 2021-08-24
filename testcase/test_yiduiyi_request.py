# -*- encoding:utf-8 -*-

import unittest
from automations.tools.http_requests import HttpRequest
from ddt import ddt,data
from automations.tools.do_excel import DoExcel
from automations.tools.my_log import MyLog
from automations.tools.project_path import *


test_data = DoExcel(test_case_path,'yiduiyi').get_data()
my_logger = MyLog()
TestResult = None

@ddt()
class TestHttp(unittest.TestCase):

    def setUp(self):
        pass

    @data(*test_data)
    def test_api(self,item):
        global TestResult
        my_logger.info('开始执行测试用例{0}'.format(item['用例名称']))
        my_logger.info('..................开始http接口请求..................')

        res = HttpRequest().http_requset(item['url'],item['data'],item['method'])

        try:
            self.assertEqual(item['except'],res.json()['code'])
            TestResult = 'pass'  #成功
        except AssertionError as e:
            TestResult = 'Failed'   #失败
            raise e
        finally:
            DoExcel(test_case_path,'yiduiyi').write_back(item['case_id']+1,str(res.json()),TestResult)
            my_logger.debug('获取的结果是：{0}'.format(res.json()))


    def tearDown(self):
        pass




