#_*_coding:utf-8_*_
import requests,json
from interface_project.base.basepage import BaseConfig
from interface_project.script.scripts import getYamlfield
from interface_project.script.scripts import retry
from interface_project.script import gl

class HttpcheckRequest(object):
    Url = "/check/user/smsCode"

    payload = '80a0ded12abc20e5a332b6bc234ef20f1eb48ab77c5b8fc915e1fd892e418c85'
    #'keword=&code=&pageNo='
    # headers = {
    #     'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    #     'cache-control': "no-cache",
    #     'postman-token': "6eb8950f-4839-3857-15e9-91a14c7e1663"
    # }

    def __init__(self):
        pass


    def tokens(self):
        self.token = BaseConfig().base_token
        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
        }
        headers['lf-None-Matoh'] = self.token
        return headers

    #post方法
    @property
    @retry(reNum=getYamlfield(gl.configFile)['RETRY']['ReNum'])
    def post(self):
        #url拼接
        self.full_url = BaseConfig().check_url + self.Url

        #发送post请求
        res = requests.request("POST",self.full_url,data=self.payload,headers=self.tokens())
        return res.text
        # if res.status_code ==200:
        #     return res.json()
        # else:
        #     return {"errcode": 9001, "errmsg": str(res)}

if __name__=="__main__":
    print HttpcheckRequest().post