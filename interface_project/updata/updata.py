#_*_coding:utf-8_*_
import requests,json
from interface_project.base.basepage import BaseConfig
from interface_project.script.scripts import getYamlfield
from interface_project.script.scripts import retry
from interface_project.script import gl

class Httpupdata(object):
    #url信息
    Url = "/machine/machine/installApp"
    updataUrl = "/machine/machine/updateInfo"

    #机器信息
    machineId = ['c2f5a701a5244d158ceb5cbba8d8e16a','4b5ad3fc4afb4f09a3cadd1220b79781','decd4822d8d244bb8301de02a3fbcccb']
    for newmachineId in machineId:
        print newmachineId


    datas = {"appPackageName":"com.inno72.detection","url":"http://inno72.oss.72solo.com/apk/test/test_detection.apk","versionCode":"6"}

    datas = {"appPackageName":"com.inno72.installer","url":"http://inno72.oss.72solo.com/apk/test/prod_installer.apk","versionCode":"2"}

    datas = {"appPackageName":"com.inno72.monitor","url":"http://inno72.oss.72solo.com/apk/test/prod_monitor.apk","versionCode":"4"}

    datas = {"appPackageName":"com.inno72.upload","url":"http://inno72.oss.72solo.com/apk/test/prod_upload.apk","versionCode":"3"}

    #数据信息
    updatas = {"machineId":newmachineId,"updateStatus":"3"}
    payload = {"machineId":'c2f5a701a5244d158ceb5cbba8d8e16a',"appPackageName":datas['appPackageName'],"url":datas['url'],"versionCode":datas['versionCode']}


    def __init__(self):
        pass


    def tokens(self):
        self.token = BaseConfig().base_token
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }
        headers['lf-None-Matoh'] = self.token
        return headers

    #post方法
    @property
    @retry(reNum=getYamlfield(gl.configFile)['RETRY']['ReNum'])
    def post(self):
        #url拼接
        self.full_url = BaseConfig().base_url + self.Url

        #发送post请求
        res = requests.request("POST",self.full_url,data=self.payload,headers=self.tokens())
        if res.status_code ==200:
            return res.text
        else:
            return {"errcode": 9001, "errmsg": str(res)}

    @property
    def updata(self):
        #url拼接
        self.full_url = BaseConfig().base_url + self.updataUrl

        #发送post请求
        updatares = requests.request("POST",self.full_url,data=self.updatas,headers=self.tokens())
        if updatares.status_code ==200:
            return  updatares.text
        else:
            return {"errcode": 9001, "errmsg": str(updatares)}

if __name__=="__main__":
    print Httpupdata().post
    print Httpupdata().updata

