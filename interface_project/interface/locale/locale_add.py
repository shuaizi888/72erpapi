#coding:utf-8
#Author:sgao
import json
import requests
from interface_project.base.basepage import BaseConfig

class LocaleClass(object):
    url = "/machine/locale/add"

    payload = 'areaCode=1&name=1111&mall=1111&manager=1118&remark=1111&mobile=18833337777'

    # headers = {
    #     'Content-Type':"application/x-www-form-urlencoded",
    #     'cache-control': "no-cache",
    # }


    def __init__(self):
        self.baseUrl = BaseConfig().base_url
        self.url = self.baseUrl + self.url


    def token(self):
        self.token = BaseConfig().base_token
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }
        headers['lf-None-Matoh'] = self.token
        return headers

    #添加点位
    @property
    def localeAdd(self):
        res = requests.request("POST",self.url,data=self.payload,headers=self.token())
        if res.status_code ==200:
            return res.json()
        else:
            return {"errcode": 9001, "errmsg": str(res)}

if __name__=="__main__":
    print json.dumps(LocaleClass().localeAdd).decode('unicode-escape')