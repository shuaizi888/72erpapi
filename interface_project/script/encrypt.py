#_*_coding:utf-8_*_
import requests,json
from interface_project.base.basepage import BaseConfig
from interface_project.script.scripts import getYamlfield
from interface_project.script.scripts import retry
from interface_project.script import gl

# class HttpAppEncrypt(object):
#     Url = "/machine/encrypt"
#
#     payload = '{"machineCode":"18865687"}'
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
#         self.headers = {
#             'Content-Type': "application/json",
#             'Cache-Control': "no-cache"
#         }
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
#     # print json.dumps(HttpAppRequest().post).decode('unicode-escape')
#     print HttpAppEncrypt().post


import requests

def jiami(datas):
    URL = '/machine/encrypt'
    full_url = BaseConfig().app_url + URL
    headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
    data = datas
    jiami = requests.request('post',url=full_url,headers=headers,data=datas)
    return jiami.text

def checkjiami(datas):
    URL = '/machine/encrypt'
    full_url = BaseConfig().check_url + URL
    headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
    data = datas
    checkjiami = requests.request('post',url=full_url,headers=headers,data=datas)
    return checkjiami.text

# a = '{"channelJson":[{"code":1,"volumeCount":11,"workStatus":0},{"code":2,"volumeCount":11,"workStatus":0},{"code":3,"volumeCount":11,"workStatus":0},{"code":4,"volumeCount":11,"workStatus":0},{"code":5,"volumeCount":11,"workStatus":0},{"code":6,"volumeCount":11,"workStatus":0},{"code":7,"volumeCount":11,"workStatus":0},{"code":8,"volumeCount":11,"workStatus":0},{"code":11,"volumeCount":11,"workStatus":0},{"code":12,"volumeCount":11,"workStatus":0},{"code":13,"volumeCount":11,"workStatus":0},{"code":14,"volumeCount":11,"workStatus":0},{"code":15,"volumeCount":11,"workStatus":0},{"code":16,"volumeCount":11,"workStatus":0},{"code":17,"volumeCount":11,"workStatus":0},{"code":18,"volumeCount":11,"workStatus":0},{"code":21,"volumeCount":11,"workStatus":0},{"code":23,"volumeCount":11,"workStatus":0},{"code":25,"volumeCount":11,"workStatus":0},{"code":27,"volumeCount":11,"workStatus":0},{"code":31,"volumeCount":11,"workStatus":0},{"code":32,"volumeCount":11,"workStatus":0},{"code":33,"volumeCount":11,"workStatus":0},{"code":34,"volumeCount":11,"workStatus":0},{"code":35,"volumeCount":11,"workStatus":0},{"code":36,"volumeCount":11,"workStatus":0},{"code":37,"volumeCount":11,"workStatus":0},{"code":38,"volumeCount":11,"workStatus":0},{"code":41,"volumeCount":11,"workStatus":0},{"code":42,"volumeCount":11,"workStatus":0},{"code":43,"volumeCount":11,"workStatus":0},{"code":44,"volumeCount":11,"workStatus":0},{"code":45,"volumeCount":11,"workStatus":0},{"code":46,"volumeCount":11,"workStatus":0},{"code":51,"volumeCount":11,"workStatus":0},{"code":52,"volumeCount":11,"workStatus":0},{"code":53,"volumeCount":11,"workStatus":0},{"code":54,"volumeCount":11,"workStatus":0},{"code":55,"volumeCount":11,"workStatus":0},{"code":56,"volumeCount":11,"workStatus":0}],"machineCode":"18865687","bluetoothAddress":""})'
# print jiami(a)