# -*- encoding:utf-8 -*-

# from automations.testcase.test_yiduiyi_request import TestHttp
from automations.testcase.test_manager_request import TestHttp
from automations.tools.project_path import *
import unittest

from HTMLTestRunner import HTMLTestRunner
from automations.tools.project_path import *

# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestHttp))
#




# 1、初始化testloader
testloader = unittest.TestLoader()

# 2、查找测试用例,加载
suite = testloader.discover(case_dir)

with open(test_report_path,'wb') as file:
    runner = HTMLTestRunner(
        stream=file,
        verbosity=2,
        title="单元测试报告",
        description="logo单元测试报告-第一次",
        tester="么么哒"
    )
    runner.run(suite)

