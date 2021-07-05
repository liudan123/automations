# -*- encoding:utf-8 -*-

import unittest
from http_requests import HttpRequest

class TestHttpRequest(unittest.TestCase):

    def test_logo(self):

        url = 'http://insurance.jr.sina.com.cn/web/index.php/api/getLogo'
        data = {'channel_id':1}
        method = 'get'

        res = HttpRequest().http_requset(url,data,method)

        print res
        return res
