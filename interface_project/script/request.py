# _*_coding:utf-8_*_
import requests
from interface_project.base.basepage import BaseConfig
import json
from interface_project.script.scripts import retry
from requests.exceptions import ConnectionError,\
    ConnectTimeout,HTTPError,Timeout

class HttpWebRequest(object):

    url = "/machine/locale/list"

    payload = 'keword=&code=&pageNo='
    # headers = {
    #     'Content-Type':"application/x-www-form-urlencoded",
    #     'cache-control': "no-cache",
    #     'lf-None-Matoh':"d222c601032c4b36a4e950a1d41d5a8e"
    # }

    def __init__(self,url='/xxx/xxxx'):
        self.baseUrl  = BaseConfig().base_url
        self.url = self.baseUrl + str(url).strip()

    def token(self):
        self.token = BaseConfig().base_token
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }
        headers['lf-None-Matoh'] = self.token
        return headers


    # post请求
    @retry(reNum=3)
    def post(self):
        res = requests.request("POST",self.url,data=self.payload,headers=self.token())
        if res.status_code ==200:
            return res.json()
        else:
            return {"errcode": 9001, "errmsg": str(res)}


if __name__ == "__main__":
    print json.dumps(HttpWebRequest().post())\
        .decode('unicode-escape')


