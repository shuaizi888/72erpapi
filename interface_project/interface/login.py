#coding:utf-8
#Author:sgao
import json
import requests
# from interface_project.base.basepage import BaseConfig

class loginClass(object):
    url = "http://api.erp.36solo.com/dd/testLogin?"
    # url = "http://api.erp.32solo.com/dd/testLogin?"
    # url = "http://api.erp.inno72.com/dd/testLogin?"
    payload = 'phone=18811420137&name=高帅分身'
    # payload = 'phone=18811420138&name=高帅'
    headers = {
        'Content-Type':"application/x-www-form-urlencoded",
        'cache-control': "no-cache",
    }


    def __init__(self):
        # self.baseUrl = BaseConfig().base_url
        self.url = self.url


    # def token(self):
    #     self.token = BaseConfig().base_token
    #     headers = {
    #         'Content-Type': "application/x-www-form-urlencoded",
    #         'cache-control': "no-cache",
    #     }
    #     headers['lf-None-Matoh'] = self.token
    #     return headers

    #登录
    @property
    def login(self):
        res = requests.request("POST",self.url,data=self.payload,headers=self.headers)
        if res.status_code ==200:
            ldata = res.json()
            logindata = ldata['data']['token']
            return logindata


        else:
            return {"errcode": 9001, "errmsg": str(res)}

if __name__=="__main__":
    print json.dumps(loginClass().login).decode('unicode-escape')