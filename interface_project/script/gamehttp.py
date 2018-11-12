#_*_coding:utf-8_*_
import requests,json
from interface_project.base.basepage import BaseConfig
from interface_project.script.scripts import getYamlfield
from interface_project.script.scripts import retry
from interface_project.script import gl

class HttpWebRequest(object):
    Url = ""
    # http://api.game.prod.32solo.com/inno72/service/open
    payload = ""
    # {\"serviceName\":\"createQrCode\",\"params\":{\"machineId\":\"18237422\"},\"version\":\"1.0.0\"}
    headers = {
        'Cache-Control': "no-cache",
        'Content-Type': "application/json",
        # 'Postman-Token': "6d05cd7d-1e3b-4292-b4ae-1e282f39f943"
    }

    def __init__(self):
        pass

    #post方法
    @property
    @retry(reNum=getYamlfield(gl.configFile)['RETRY']['ReNum'])
    def post(self):
        self.Url = self.Url
        #发送post请求
        res = requests.request("POST",self.Url,data=self.payload,headers=self.headers)
        if res.status_code ==200:
            return res.json()
            # print a['data']['sessionUuid']
        else:
            return {"errcode": 9001, "errmsg": str(res)}

class HttpWebRequests(object):
    Url = "http://api.game.36solo.com/api/getSamplingNew"
    # http://api.game.prod.32solo.com/inno72/service/open
    payload = {"machineCode": "18383061"}
    # {\"serviceName\":\"createQrCode\",\"params\":{\"machineId\":\"18237422\"},\"version\":\"1.0.0\"}
    headers = {
        'Cache-Control': "no-cache",
        'Content-Type': "application/x-www-form-urlencoded",
        # 'Postman-Token': "6d05cd7d-1e3b-4292-b4ae-1e282f39f943"
    }

    def __init__(self):
        pass

    #post方法
    @property
    @retry(reNum=getYamlfield(gl.configFile)['RETRY']['ReNum'])
    def post(self):
        self.Url = self.Url
        #发送post请求
        res = requests.request("POST",self.Url,data=self.payload,headers=self.headers)
        if res.status_code ==200:
            return res.json()
            # print a['data']['sessionUuid']
        else:
            return {"errcode": 9001, "errmsg": str(res)}


class HttpWebRequestget(object):
    Url = "http://api.game.36solo.com/api/getSamplingNew"
    # http://api.game.prod.32solo.com/inno72/service/open
    payload = '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"machineCode\"\r\n\r\n18383061\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--'
    # print type(payload)
    # {\"serviceName\":\"createQrCode\",\"params\":{\"machineId\":\"18237422\"},\"version\":\"1.0.0\"}
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'Cache-Control': "no-cache",
        'Content-Type': "application/form-data",
        # 'Postman-Token': "6d05cd7d-1e3b-4292-b4ae-1e282f39f943"
    }

    def __init__(self):
        pass

    #post方法
    @property
    @retry(reNum=getYamlfield(gl.configFile)['RETRY']['ReNum'])
    def post(self):
        self.Url = self.Url
        #发送post请求
        res = requests.request("POST",self.Url,data=self.payload,headers=self.headers)
        if res.status_code ==200:
            return res.json()
            # print a['data']['sessionUuid']
        else:
            return {"errcode": 9001, "errmsg": str(res)}

class HttpWebRequestnew(object):
    Url = "http://api.game.36solo.com/inno72/service/open"
    # http://api.game.prod.32solo.com/inno72/service/open
    payload = "{\n\"serviceName\": \"standardFindActivity\",\n\n\"version\": \"1.0.0\",\n\"params\": {\n\"machineId\": \"19294124\",\n\"planId\": \"\",\n\"version\": \"\",\n\"versionInno72\": \"\"\n}\n}"
    # {\"serviceName\":\"createQrCode\",\"params\":{\"machineId\":\"18237422\"},\"version\":\"1.0.0\"}
    headers = {
        'Cache-Control': "no-cache",
        'Content-Type': "application/json",
        # 'Postman-Token': "6d05cd7d-1e3b-4292-b4ae-1e282f39f943"
    }

    def __init__(self):
        pass

    #post方法
    @property
    @retry(reNum=getYamlfield(gl.configFile)['RETRY']['ReNum'])
    def post(self):
        self.Url = self.Url
        #发送post请求
        res = requests.request("POST",self.Url,data=self.payload,headers=self.headers)
        if res.status_code ==200:
            a = res.json()
            print a['data']['qrCodeUrl']
            return res.json()
        else:
            return {"errcode": 9001, "errmsg": str(res)}

if __name__=="__main__":
    print json.dumps(HttpWebRequestget().post).decode('unicode-escape')