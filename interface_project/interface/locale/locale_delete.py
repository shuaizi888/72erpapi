#coding:utf-8
#Author:sgao
import json
import requests
from interface_project.base.basepage import BaseConfig

class LocaleClass(object):
    url = "/machine/locale/delete"

    payload = 'id=1882'
    # headers = {
    #     'Content-Type':"application/x-www-form-urlencoded",
    #     'cache-control': "no-cache",
    #     'lf-None-Matoh':"d222c601032c4b36a4e950a1d41d5a8e"
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

    #删除点位
    @property
    def localeDetele(self):
        res = requests.request("POST",self.url,data=self.payload,headers=self.token())
        if res.status_code ==200:
            return res.json()
        else:
            return {"errcode": 9001, "errmsg": str(res)}

if __name__=="__main__":
    print json.dumps(LocaleClass().localeDetele).decode('unicode-escape')