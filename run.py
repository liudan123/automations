# -*- encoding:utf-8 -*-

from tools.http_requests import HttpRequest
from tools.test_http_request import TestHttpRequest
import unittest
import HTMLTestRunnerCN
from tools.project_path import *

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

with open(test_report_path,'wb') as file:
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title="单元测试报告",
        description="logo单元测试报告-第一次",
        tester="么么哒"
    )
    runner.run(suite)