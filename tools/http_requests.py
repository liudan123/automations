# -*- encoding:utf-8 -*-

import requests

class HttpRequest:

    def http_requset(self,url,data,method,cookie=None):

        if method == 'get':
            res = requests.get(url,data,cookies=cookie,verify=False)

        else:
            res =requests.post(url,data,cookies=cookie,verify=False)

        return res

if __name__ =='__main__':
    HttpRequest()
    