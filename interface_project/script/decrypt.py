#_*_coding:utf-8_*_
import requests,json
from interface_project.base.basepage import BaseConfig
from interface_project.script.scripts import getYamlfield
from interface_project.script.scripts import retry
from interface_project.script import gl
from interface_project.script import encrypt

# class HttpAppEncrypt(object):
#     Url = "/machine/decrypt"
#     payload = encrypt.HttpAppEncrypt().post
#
#     headers = {
#         'Content-Type': "application/json",
#         'Cache-Control': "no-cache"
#     }
#
#     def __init__(self):
#         pass
#
#
#     #post方法
#     @property
#     @retry(reNum=getYamlfield(gl.configFile)['RETRY']['ReNum'])
#     def post(self):
#         #url拼接
#         self.full_url = BaseConfig().app_url + self.Url
#
#         #发送post请求
#         res = requests.request("POST",self.full_url,data=self.payload,headers=self.headers)
#         return res.text
#         # if res.status_code ==200:
#         #     return res.json()
#         # else:
#         #     return {"errcode": 9001, "errmsg": str(res)}
#
# if __name__=="__main__":
#     print HttpAppEncrypt().post

import requests

def jiemi(datas):
    URL = '/machine/decrypt'
    full_url = BaseConfig().app_url + URL
    headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
    data = datas
    jiemi = requests.request('post',url=full_url,headers=headers,data=data)
    return jiemi.text

def checkjiemi(datas):
    URL = '/machine/decrypt'
    full_url = BaseConfig().check_url + URL
    headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
    data = datas
    checkjiemi = requests.request('post',url=full_url,headers=headers,data=data)
    return checkjiemi.text

# a = '6a54f7c88ed80836fcaba17d5eb4c79dd319c7a18157c7eb59d75e49eafda571b2836631799d7a1ee408b55f64d22de2'
# print jiemi(a)