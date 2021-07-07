# -*- encoding:utf-8 -*-

from automations.testcase.test_http_request import TestHttp
import unittest
import HTMLTestRunnerCN
from tools.project_path import *

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttp))

with open(test_report_path,'wb') as file:
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title="单元测试报告",
        description="logo单元测试报告-第一次",
        tester="么么哒"
    )
    runner.run(suite)