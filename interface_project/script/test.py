# coding:utf-8
#Author:sgao
import sys
import yaml
# print sys.path
#
# class A(object):
#
#     @property
#     def d1(self):
#         print 'd1'
#
#     @property
#     def d2(self):
#         print 'd2'
#
#
# getattr(A(),'d%d'%2)
#

from interface_project.interface.login import loginClass
from interface_project.script import gl
from interface_project.script import scripts
import os
import unittest
import ddt
from interface_project.base.basepage import BaseConfig


# a = "75aaf91444d34fcfaa0bdf53fb9f4d6e"
# print type(a)
# b = '{{a}}'
# print b
#
# if b.startswith('{{') and b.endswith('}}'):
#     ret = eval(b.rsplit('}}')[0].split('{{')[1])
#     print ret


#
# a1 = loginClass().login
# print type(a1)
# print a1
#
# b1 = unicode.encode(a1)
# print type(b1)
# print b1
#
#
#
# c1 = '{{b1}}'
# print c1
# if c1.startswith('{{') and c1.endswith('}}'):
#     ret1 = eval(c1.rsplit('}}')[0].split('{{')[1])
#     print ret1


# print BaseConfig().base_token
# a = '123'
# print 'yes：'+a
# from interface_project.script.gamehttp import HttpWebRequestnew
#
#
# res = HttpWebRequestnew().post
# print res

#
# from interface_project.testscenario.gameservers.testgames import TestScenario
#
# TestScenario().testgameserver
# import json
# data ={"serviceName":"polling","params":{"sessionUuid":'tete'},"version":"1.0.0"}
# print type(data)
# Pdata = 'tete'
# print Pdata
# data ={"serviceName":"polling","params":{"sessionUuid":Pdata},"version":"1.0.0"}
# print type(data)
# datanew = json.dumps(data)
# print datanew


# a = 12
# # print a
# # print type(a)
# # print 'a'+a
#
# print 'a:'+str(a)
# import random
# a = random.randint(0,999999999)
# print a
# from interface_project.script import scripts
# c = 'abc'
# b = c + str(scripts.sjshu())
# print b

# import requests
#
# def jiami(datas):
#     URL = 'http://api.app.36solo.com/machine/encrypt'
#     headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
#     data = datas
#     jiami = requests.request('post',url=URL,headers=headers,data=datas)
#     print jiami.text
#
#
# jiami({"channelJson":[{"code":1,"volumeCount":11,"workStatus":0},{"code":2,"volumeCount":11,"workStatus":0},{"code":3,"volumeCount":11,"workStatus":0},{"code":4,"volumeCount":11,"workStatus":0},{"code":5,"volumeCount":11,"workStatus":0},{"code":6,"volumeCount":11,"workStatus":0},{"code":7,"volumeCount":11,"workStatus":0},{"code":8,"volumeCount":11,"workStatus":0},{"code":11,"volumeCount":11,"workStatus":0},{"code":12,"volumeCount":11,"workStatus":0},{"code":13,"volumeCount":11,"workStatus":0},{"code":14,"volumeCount":11,"workStatus":0},{"code":15,"volumeCount":11,"workStatus":0},{"code":16,"volumeCount":11,"workStatus":0},{"code":17,"volumeCount":11,"workStatus":0},{"code":18,"volumeCount":11,"workStatus":0},{"code":21,"volumeCount":11,"workStatus":0},{"code":23,"volumeCount":11,"workStatus":0},{"code":25,"volumeCount":11,"workStatus":0},{"code":27,"volumeCount":11,"workStatus":0},{"code":31,"volumeCount":11,"workStatus":0},{"code":32,"volumeCount":11,"workStatus":0},{"code":33,"volumeCount":11,"workStatus":0},{"code":34,"volumeCount":11,"workStatus":0},{"code":35,"volumeCount":11,"workStatus":0},{"code":36,"volumeCount":11,"workStatus":0},{"code":37,"volumeCount":11,"workStatus":0},{"code":38,"volumeCount":11,"workStatus":0},{"code":41,"volumeCount":11,"workStatus":0},{"code":42,"volumeCount":11,"workStatus":0},{"code":43,"volumeCount":11,"workStatus":0},{"code":44,"volumeCount":11,"workStatus":0},{"code":45,"volumeCount":11,"workStatus":0},{"code":46,"volumeCount":11,"workStatus":0},{"code":51,"volumeCount":11,"workStatus":0},{"code":52,"volumeCount":11,"workStatus":0},{"code":53,"volumeCount":11,"workStatus":0},{"code":54,"volumeCount":11,"workStatus":0},{"code":55,"volumeCount":11,"workStatus":0},{"code":56,"volumeCount":11,"workStatus":0}],"machineCode":"18865687","bluetoothAddress":""})

# url = 'http://api.app.36solo.com/machine/decrypt'
# headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
# jiemi = requests.request('post',url=url,headers=headers,data=a)
# print jiemi.text
#
# from interface_project.script import encrypt
# from interface_project.script import decrypt
#
# a = '{"machineCode":"18865687"}'
# encrypt.jiami(a)
#
# b = '6a54f7c88ed80836fcaba17d5eb4c79d1c9da89f58b3f0afdef556daa80c198b51f10448829082ea86d5895f3441b391'
# decrypt.jiemi(b)

# a = {"code":0,"data":null,"msg":"??"}
# print type(a)
#
# def tokens(self):
#     self.token = BaseConfig().base_token
#     print self.token
#     headers = {
#         'Content-Type': "application/x-www-form-urlencoded",
#         'cache-control': "no-cache",
#     }
#     headers['lf-None-Matoh'] = self.token
#     return headers
#
# tokens()
#
# a = BaseConfig().base_token
# print a
# headers = {
#         'Content-Type': "application/x-www-form-urlencoded",
#         'cache-control': "no-cache",
#     }
# headers['lf-None-Matoh'] = a
# print headers


# list = ['1','2','3','d']
# test_str = "".join(list)
# print test_str
#
# list = [1,2,3,4,8]
# test_str = "  ".join([str(x)for x in list])
# print test_str


# str = '1234444'
# newstr =  list(str)
# print newstr
# import random
# def sjshu():
#     """
#     随机数生成
#     :return:
#     """
#     a = random.randint(1000,1111)
#     b = random.randint(10,30)
#     return str(a)+str(b)
#
# sjshu()
#
# a = 111
# b = 222
# print type(a)
# print type(b)
# print

import time
import datetime
# print time.localtime(time.time())
# print time.time()
# print time.strftime()


def timete():
    times = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    return times
timete()


# def endtime():
#     endtimes = (datetime.datetime.now() + datetime.timedelta(minutes=6)).strftime("%Y-%m-%d %H:%M")
#     return endtimes
# endtime()
#
#
# a =123
# b = 456
# print('{}{}'.format(a,b))
#
# import random
# def sjshu():
#     """
#     随机数生成
#     :return:
#     """
#     a = random.randint(1000,1111)
#     b = random.randint(10,30)
#     # return str(a)+str(b)
#     print ('{}{}'.format(a, b))
#
# sjshu()


# print("python", "tab", ".com", sep='')
# print "-------------------------------"
# print "一键升级共：55 台机器"
# print "一键升级成功：19 台机器"
# print "一键升级失败：36 台机器"

from Queue import Queue
import threading
import time
import datetime
q = Queue()

def timete():
    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print times
# timete()


def auit_Count(q):
    PASSED_COUNT =0
    FAILED_COUNT =0

    while True:
        if not q.empty():
            v = str(q.get()).split('-')
            if v[0] =='p':
                PASSED_COUNT+=1
            if v[0] =='f':
                FAILED_COUNT+=1
        else:
            q.all_tasks_done
            break
    return PASSED_COUNT,FAILED_COUNT

def updataApp(list_data):
    for i,v in enumerate(list_data):
        if v == 'pass':
            q.put('p-%d'%i)
        else:
            q.put('f-%d'%i)


# def updataAPP(Url,machineId,appPackageName,appurl,versionCode):
#     data = {"machineId": machineId, "appPackageName": appPackageName, "url": appurl,"versionCode": versionCode}
#     res = requests.request('POST', Url, data=data, headers=tokens())
#     if res.status_code == 200:
#         newres = res.json()
#         i = 0
#         if newres['code'] ==0:
#             print "升级成功机器编号："+ newmachineId +"   "+appPackageName
#             q.put('p-%d'%i)
#
#         else:
#             print "升级失败机器编号："+newmachineId+"   "+appPackageName+ "   "+newres['msg'].encode("utf-8")
#             q.put('f-%d' % i)
#     else:
#         return {"errcode": 9001, "errmsg": str(res)}




# from Queue import Queue
# import threading
# import time
# q = Queue()
#
#
#
# def auit_Count(q):
#     PASSED_COUNT =0
#     FAILED_COUNT =0
#
#     while True:
#         if not q.empty():
#             v = str(q.get()).split('-')
#             if v[0] =='p':
#                 PASSED_COUNT+=1
#             if v[0] =='f':
#                 FAILED_COUNT+=1
#         else:
#             q.all_tasks_done
#             break
#     return PASSED_COUNT,FAILED_COUNT
#
# def updataApp(list_data):
#     for i,v in enumerate(list_data):
#         if v == 'pass':
#             q.put('p-%d'%i)
#         else:
#             q.put('f-%d'%i)
#
# if __name__=="__main__":
#     list = ['pass','pass','fail','pass','pass','pass','fail','pass','pass','pass','fail','pass','pass','pass','fail','pass','pass','pass','fail','pass','pass','pass','fail','pass','pass','pass','fail','pass','pass','pass','fail','pass','pass','pass','fail','pass','pass','pass','fail','pass','pass','pass','fail','pass','pass','pass','fail','pass','pass','pass','fail','pass']
#     # print type(str(len(list)))
#     # 定义多线程
#     threads = []
#     starttime = int(time.time())
#     print starttime
#     for i in range(100):
#         th = threading.Thread(target=updataApp, args=(list,))
#         th.name = 'thread{}'.format(i)
#         threads.append(th)
#
#     for j, v in enumerate(threads):
#         threads[j].start()
#
#     for m, v in enumerate(threads):
#         threads[m].join()
#
#
#
#     # for i in range(2):
#     #     starttime = int(time.time())
#     #     print starttime
#     #     th = threading.Thread(target=updataApp,args=(list,))
#     #     th.name = 'thread{}'.format(i)
#     #     th.start()
#     #     th.join()
#     # time.sleep(2)
#     endtime = int(time.time())
#     print endtime
#     times = endtime-starttime
#     print times
#     p,f = auit_Count(q)
#     print '一共数据: '+str(len(list))
#     print '成功:%d' % p, '-', '失败:%d' % f
#
# import requests
# from interface_project.base.basepage import BaseConfig
#
# def tokens():
#     token = BaseConfig().base_token
#     headers = {
#         'Content-Type': "application/x-www-form-urlencoded",
#         'cache-control': "no-cache",
#     }
#     headers['lf-None-Matoh'] = token
#     return headers
#
# def updataAPP(Url,machineId,appPackageName,appurl,versionCode):
#     data = {"machineId": machineId, "appPackageName": appPackageName, "url": appurl,"versionCode": versionCode}
#     res = requests.request('POST', Url, data=data, headers=tokens())
#     if res.status_code == 200:
#         newres = res.json()
#         i = 0
#         if newres['code'] ==0:
#             print "升级成功机器编号："+ newmachineId +"   "+appPackageName
#             q.put('p-%d'%i)
#
#         else:
#             print "升级失败机器编号："+newmachineId+"   "+appPackageName+ "   "+newres['msg'].encode("utf-8")
#             q.put('f-%d' % i)
#     else:
#         return {"errcode": 9001, "errmsg": str(res)}
#
#
#
#
# if __name__ == 'main':
#     Url = BaseConfig().base_url + "/machine/machine/installApp"
    # machineId = ['5d80295b4b144fbbb55b15e6d1f22ac0', '123', '323']
    # appname = ['com.inno72.app', 'com.inno72.dc', 'com.inno72.monitorapp', 'com.inno72.installer',
    #            'com.inno72.detection', 'com.inno72.upload', 'com.inno72.demons']
    # appurl = ['http://inno72.oss.72solo.com/prod',
    #           'http://inno72.oss.72solo.com/prod',
    #           'http://inno72.oss.72solo.com/prod',
    #           'http://inno72.oss.72solo.com/prod',
    #           'http://inno72.oss.72solo.com/prod',
    #           'http://inno72.oss.72solo.com/prod',
    #           'http://inno72.oss.72solo.com/prod']
    # appversion = ['2', '3', '4', '6', '3', '2', '1']
    # print appname[0]
    # print appurl[0]
    # print appversion[0]
    # for a in range(len(appname)):
    #     pass


# machineId = ['5d80295b4b144fbbb55b15e6d1f22ac0', '123', '323']
#
# appname = ['com.inno72.app', 'com.inno72.dc', 'com.inno72.monitorapp', 'com.inno72.installer',
#             'com.inno72.detection', 'com.inno72.upload', 'com.inno72.demons']
# appurl = ['http://inno72.oss.72solo.com/prod/prod_app.apk',
#           'http://inno72.oss.72solo.com/prod/prod_dc.apk',
#           'http://inno72.oss.72solo.com/prod/prod_monitor.apk',
#           'http://inno72.oss.72solo.com/prod/prod_installer.apk',
#           'http://inno72.oss.72solo.com/prod/prod_detection.apk',
#           'http://inno72.oss.72solo.com/prod/prod_upload.apk',
#           'http://inno72.oss.72solo.com/prod/prod_demons.apk']
# appversion = ['2', '3', '4', '6', '3', '2', '1']
#
#
#
# Url = BaseConfig().base_url + "/machine/machine/installApp"
# a = 0
# b = 0
# for a,b in enumerate(appname):
#     newappnew = ('appname{}'.format(b))
#     newappurl = ('appurl{}'.format(appurl[a]))
#     newappversion = ('appversion{}'.format(appversion[a]))
#     for newmachineId in machineId:
#         updataAPP(Url,newmachineId,b,appurl[a],appversion[a])




# for i,val in enumerate(appname):
#     print("序号:%s 值:%s" % (i + 1, val))
# for a,vala in enumerate(appurl):
#     print("序号:%s 值:%s" % (a + 1, vala))
# for b ,valb in enumerate(appversion):
#     print("序号:%s 值:%s" % (b + 1, valb))

# for a,b,c in zip(appname,appurl,appversion):
#     new = (a,b,c)
#     new1 =  list(new)
#     print(new1[::1])
# import time
# def starttime():
#     times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     print times
#
# def endtime():
#     times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     print times
#
# str(a) = starttime()
# time.sleep(5)
# str(b) = endtime()
# a = {"msg": "成功", "code": 0, "data": {"goods": [{"goodsNum": 22, "goodsId": "575183937392", "goodsRule": 0, "goodsCount": 0, "goodsName": "男用多功能洁面乳30ml小样", "channelIds": ["1", "2"]}], "canOrder": 'true'}}
# # print a['data']['goods'][0]['channelIds'][0]

# a = {
#     "code": 0,
#     "data": {
#         "id": "eade15523f244d929a9f822347cf16b4",
#         "machineCode": "19294124",
#         "machineName": 'null',
#         "localeId": "d42f6053ae8242038099dc6e849dee9f",
#         "tag": 'null',
#         "createId": "generateMachineId",
#         "updateId": "4d33f7d4ca6f4a919bea235cfc5843d6",
#         "createTime": "2018-09-11 16:40:36",
#         "updateTime": "2018-09-11 16:40:36",
#         "machineStatus": 4,
#         "netStatus": 4,
#         "deviceId": "66ffc278d2780761f2172957d1c194b7",
#         "address": "",
#         "bluetoothAddress": "02:00:00:00:00:00",
#         "openStatus": 1,
#         "inno72Games": {
#             "id": "4a5e3264d73a41518270dcdf48c215d8",
#             "name": "测试",
#             "version": "1.0.0",
#             "versionInno72": "1.0.0",
#             "remark": "kjasjglaslgjlsjglii uiu 呕呕呕呕呕呕呕呕呕呕呕呕呕呕",
#             "isDelete": 0,
#             "createId": "89dbe3bd836f44859114a19635ecc94a",
#             "createTime": "2018-08-30 20:48:30",
#             "updateId": "df81a0c49ad648eea4760eddf77a1b1d",
#             "updateTime": "2018-08-30 20:48:31"
#         },
#         "brandName": "小鹏汽车",
#         "planCode": "11",
#         "activityPlanId": "c1a05d6081a74515a02a43eaec5f63bb",
#         "activityId": "f204a1a9303645fb93778ac49b8e9575",
#         "channelId": "5d23462b048f4622ad87a4d2beff83ce",
#         "inno72ActivityPlan": {
#             "id": "c1a05d6081a74515a02a43eaec5f63bb",
#             "activityId": "f204a1a9303645fb93778ac49b8e9575",
#             "gameId": "4a5e3264d73a41518270dcdf48c215d8",
#             "prizeType": "100100",
#             "startTime": "2018-09-11 18:38:00",
#             "endTime": "2018-09-12 23:59:59",
#             "isDelete": 0,
#             "remark": "已选择1台机器，分别位于澳门特别行政区",
#             "createId": "df81a0c49ad648eea4760eddf77a1b1d",
#             "createTime": "2018-09-11 18:38:30",
#             "updateId": "df81a0c49ad648eea4760eddf77a1b1d",
#             "updateTime": "2018-09-11 18:38:30",
#             "userMaxTimes": 1,
#             "dayUserMaxTimes": 1
#         },
#         "prizeType": "100100",
#         "reload": 'true'
#     },
#     "msg": "成功"
# }
#
# b =  a['data']['machineCode']
# c =  a['data']['activityPlanId']
# print '测试：' + b +'   '+ c

# a = {"serviceName": "standardPrepareLogin","version": "1.0.0","params": {"machineCode": "192941247","loginType": 1}}
# b =  str(a)
# c = type(b)
# print c
# # print dict(c)
#
# print c['params']['machineCode']
#
# a='abcdef'
# print a[0]\

# a = []
#
# for i in range(9):
#     if i == 3:
#         a.append(i)
#         print  a
# a = ['123','344','4444']
# falied = []
# for b in a:
#     falied.append(b)
#
# print falied

success_arr = []
failed_arr = []

# def update(i):
#     if i:
#         success_arr.append('机器编号1')
#     else:
#         failed_arr.append('机器编号2')
#
# update(True)
#
# print(success_arr)
# print(failed_arr)

# import requests
# success_arr = []
# failed_arr = []
# def updataAPP(Url,machineId,appPackageName,appurl,versionCode):
#     data = {"machineId": machineId, "appPackageName": appPackageName, "url": appurl,"versionCode": versionCode}
#     res = requests.request('POST', Url, data=data, headers=tokens())
#
#     if res.status_code == 200:
#         newres = res.json()
#         i = 0
#         if newres['code'] ==0:
#             # print ("升级成功机器编号："+ newmachineId +"   "+appPackageName)
#             q.put('p-%d'%i)
#             success_arr.append(newmachineId)
#         else:
#             # print ("升级失败机器编号："+newmachineId+"   "+appPackageName+ "   "+newres['msg'].encode("utf-8"))
#             q.put('f-%d' % i)
#             failed_arr.append(newmachineId)
#     else:
#         return {"errcode": 8888, "errmsg": str(res)}


# appname = ['com.inno72.monitorapp']
# appurl = ['http://inno72.oss.72solo.com/apk/prod/prod_monitor1.1.0.apk']
# appversion = ['10']
# machineId = ['123','344','555']
#
# a=0
# b=0
# for a, b in enumerate(appname):
#     #starttime()
#     newappnew = ('appname{}'.format(b))
#     newappurl = ('appurl{}'.format(appurl[a]))
#     newappversion = ('appversion{}'.format(appversion[a]))
#     for newmachineId in machineId:
#         # time.sleep(1)
#         updataAPP(Url, newmachineId, b, appurl[a], appversion[a])
#
#
# print('升级成功机器编号:{}'.format(success_arr))
# print('升级失败机器编号:{}'.format(failed_arr))

# a = 1
# print '测试'+ str(a)
# import time
# print time.strftime("%Y-%m-%d %H:%M", time.localtime())
#
# a = {"type": 1,
#      "appId": "3",
#      "appVersion": "10",
#      "appUrl": "http://inno72.oss.72solo.com/apk/prod/prod_monitor.apk ",
#      "doTimeStr": "2018-09-18 18:51",
#      "doType": 1,
#      "machineList": [{"machineCode": "18047652", "machineId": "5d80295b4b144fbbb55b15e6d1f22ac0"}]}
#
# print a['machineList'][0]['machineCode']
# print a['machineList'][0]['machineId']
#
# machine = {'18047652': '5d80295b4b144fbbb55b15e6d1f22ac0','123':'23'}
# print len(machine)
# def endtime():
#     endtimes = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M")
#     print endtimes
# endtime()
#
#
# a = u'18851456'
# print type(a)
#
# print "测试" + a.encode('utf-8')


# a = {"alias": "18047652", "machineCode": "18047652", "title": "1", "text": "1", "pushType": 1, "msgInfo": {
#     "apps": [{
#         "url": "http://inno72.oss.72solo.com/apk/prod/prod_monitor.apk",
#         "startStatus": 1,
#         "appPackageName": "com.inno72.monitorapp",
#         "versionCode": 9
#     }]
# }
#      }
#
# print a['msgInfo']['apps'][0]['url']
# print a['msgInfo']['apps'][0]['appPackageName']
# print a['msgInfo']['apps'][0]['versionCode']


# a = ['1','a']
# b = ['2','b']
# print list(enumerate(a))
# data = {"machineCode": '123', "msg": {"type": 3,
#                                           "data": {"className": "com.inno72.seventytwo.openapi.SeventyTwoApi",
#                                                    "methonName": "setShipFailCountLock", "paramList": [9]}}}
# print data['machineCode']
# print data['msg']['type']
# print data['msg']['data']
# print data['msg']['data']['className']
# print data['msg']['data']['methonName']
# print data['msg']['data']['paramList'][0]
# print type(data)


#
# import requests
# import json
# url = "http://api.monitor.inno72.com/sendMsgToClient/sendMsgStr"
#
# payload = "{\n    \"machineCode\":\"123\",\n    \"msg\":{\n        \"type\":3,\n        \"data\":{\n            \"className\":\"com.inno72.seventytwo.openapi.SeventyTwoApi\",\n            \"methonName\":\"setShipFailCountLock\",\n            \"paramList\":[\n                9\n            ]\n        }\n    }\n}"
# headers = {
#     'Content-Type': "application/json",
#     'lf-None-Matoh': "7e91454ec997430fb9b2a29c85982aba",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "3b0e2971-6a94-4798-8354-506a0561a36c"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# # print(response.text)
# a = response.json()
# print type(a)
# print a['data']['123']
# # c= json.loads(a)
# # d= c['data']
# # print json.dumps(a).encode('utf-8')
# # b= a.encode('utf-8')
# # print b
#
#
# n = {"data":{"123":"发送失败"}}
# print type(n)
# print n['data']['123']

# import random
#
# a = random.uniform(2,9)
# print round(a,1)

# import requests
# import json
#
# url = "http://api.game.36solo.com/inno72/service/open"
# headers = {
#     'Cache-Control': "no-cache",
#     'Content-Type': "application/json",
#     'Postman-Token': "d8aea2f5-df7b-49b4-88d7-94d06b6e3162"
#     }
# url = "http://api.game.36solo.com/api/getSamplingNew"
#
# payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"machineCode\"\r\n\r\n18383061\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
# print type(payload)
# headers = {
#     'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
#     'Cache-Control': "no-cache",
#     'Content-Type': "application/form-data",
#     'Postman-Token': "2c094024-cbe0-4843-8e7e-941ef125ab96"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print '------查看活动资源-----'
#
# payload = "{\n\"serviceName\": \"standardFindActivity\",\n\n\"version\": \"1.0.0\",\n\"params\": {\n\"machineId\": \"18335598\",\n\"planId\": \"\",\n\"version\": \"\",\n\"versionInno72\": \"\"\n}\n}"
# response = requests.request("POST", url, data=payload, headers=headers)
#
# activity= response.json()
# print json.dumps(activity).decode('unicode-escape')
# res = activity
# msg = res['data']['msg']
# code = res['data']['code']
# machineCode = res['data']['machineCode']
# activityPlanId = res['data']['activityPlanId']
# activityId = res['data']['activityId']
# channelId = res['data']['channelId']
# activityType = res['data']['activityType']
# print 'machineCode: ' + machineCode + '  ' + 'activityPlanId: ' + activityPlanId + '  ' + 'activityId: ' + activityId + '  ' + 'channelId: ' + channelId

# res = {"msg": "成功", "code": 0, "data": {"goods": [{"goodsNum": 233, "goodsId": "576402814187", "goodsRule": 0, "goodsCount": 0, "goodsName": "乔治卡罗尔男士洗面奶", "channelIds": ["53", "54", "55", "56", "52"]}], "payQrcodeImage": "", "orderResult": 0, "lotteryResult": 1, "time": 1539310267020, "needPay": 'false'}}
# # print type(res)
# #
# # channelIds = res['data']['goods'][0]['channelIds'][0]
# # payQrcodeImage = res['data']['payQrcodeImage']
# # print 'channelIds:'+channelIds
## print 'payQrcodeImage'+payQrcodeImage

# import json
# machineCode = '123'
# payload = "\n{\n\"serviceName\": \"getSampling\",\n\n\"version\": \"1.0.0\",\n\"params\": {\n\"machineCode\": \"machineCode\"\n\n}\n}"
# newpayload = json.loads(payload)
# newpayload['params']['machineCode'] = machineCode
# payload = json.dumps(newpayload)
# payload = "{\"serviceName\": \"standardPrepareLogin\",\"version\": \"1.0.0\",\"params\": {\"machineCode\": \"18383061\",\"loginType\": 0,\"operType\":\"1\",\"ext\": {\"isVip\": 0,\"itemId\": \"d447b60568a2437da806c235093f4239\",\"sessionKey\": \"6102622e6fb5de17af88c7be97eb0b10b488a33bbf793431589666223\",\"goodsCode\": \"\"}}}\n"
# response = requests.request("POST", url, data=payload, headers=headers)
#
# login= response.json()
# print json.dumps(login).decode('unicode-escape')

# payload = "{\n    \"serviceName\": \"findGoods\",\n    \"version\": \"1.0.0\",\n    \"params\": {\n        \"sessionUuid\": \"18335598\"\n    }\n}"
# response = requests.request("POST", url, data=payload, headers=headers)
#
# activity= response.json()
# print json.dumps(activity).decode('unicode-escape')
#
# res = activity
# print res['data'][0]['price']


# import requests
#
# url = "http://api.game.36solo.com/inno72/service/open"
#
# payload = "{\n \"serviceName\": \"standardOrder\",\n \"version\": \"1.0.0\",\n \"params\": {\n    \"sessionUuid\": \"18625038\",\n\t\"report\":\"\",\n\t\"umid\":\"HV02PAAZ0b0fa030db8da9a45bd9d1c006e6a51c100024\",\n\t\"ua\":\"113#wP+N6ffFfV/h3f4Au/p416F6bOu/pQ/hDskWk0inosbxbYVzk30t16M6KD4Fiu+9c/72naRbDsbkbsxYkW5D16fWbDbOs6FZDsD6x0vkG06DbsoOHDRo1Pf6bFoFsUTXDssWaIjwDXbxbYkyf1kAj9ryPypG6s4CCd2celaD1StvfvQ5+fkX9Rrlrs3G6YfcODYuNGvl9xw/c1U/PUCDYEW6bnlADj7ODEpMfdmvlrH1tpPJ8pvCM6qOwlNr45ZIOyA+KFCygXRmUXYEhueBYbw9vTwkWdPwKTqW3Z0KGi7xKDnt4gsp684l1EJsXLFgYcN2CYPiAW7M6ETZ5Stu3198Pw7m+6oWA2LafGEok3LLxl+w2LywY0YS60SESgla194ZtydlPuLU6ykIQwdfqAMUJPM3/qs7oRYNnYIuU4Lx5u3aaBZPcJl2e8HHLTP7U2pfcstEQAqZqJp2hsNKGViHHkDBzI47kMgXaBZ82k1XYtFV\"\n }\n}"
# headers = {
#     'Content-Type': "application/json",
#     'cache-control': "no-cache",
#     'Postman-Token': "c2aaf5d6-2b1d-4289-a5b2-199ab051e4ea"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)
#
#
# import requests
#
# url = "http://api.game.36solo.com/inno72/service/open"
#
# payload = "{\n\"serviceName\": \"standardShipment\",\n\"version\": \"1.0.0\",\n\"params\": {\n\t\"machineCode\": \"18625038\",\n\t\"sessionUuid\":\"18625038\",\n\t\"channelId\":\"54\",\n\t\"failChannelIds\":\"\"\n\t}\n}"
# headers = {
#     'Content-Type': "application/json",
#     'cache-control': "no-cache",
#     'Postman-Token': "a7a2274a-eb0c-4f79-b469-673d90d3b8f5"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)

# import requests
#
# url = "http://api.game.32solo.com/inno72/service/open"
#
# payload = "{\n \"serviceName\": \"standardOrder\",\n \"version\": \"1.0.0\",\n \"params\": {\n    \"sessionUuid\": \"18028123\",\n\t\"report\":\"\",\n\t\"umid\":\"HV01WAAZ0bb69a5ddb8da9a55bd02502070c9229\",\n\t\"ua\":\"113#+Gc5PkfFfDR7Ka4AuxHn16F6bOVfuGDcDskWk0inosbxbYuhcDRD1oFoKFK4sPDOheVjhrb1oYbxbYxYkWRD16fWbFiYdPj8DsDNk6CJLy9xbsdWHD5o16FW10iOGok8DnDWkf4LoYikbdD4OyKCCoBtEUro1ShHHHrQUm0CajZvrh8rdZUBulQ9uEZD1mtv2kBH6qSMjthsMREIdnytHAg2dUpm6VRMgxlpfdmOVo/1tfnx8eB3xWqDgVF4HSs9feCnZf7EtJAWIt8I+VFfsMpyNskB3ehQE0n0XjRHbuI10eSc8WDc8+uxUgFTOQCZPM8wIUfheawc6CuDYHM4Bx9cV3xXuESuTvSP91Bj+RSR0H/qc9P/PTwtixYHCaHTxlQcbVRmEE7xvKH6ntwrkuXjDFgJvrp8RVue6dwsIr1t5c4IfIm+0CXqbcdaliBBl9OUBzb1N6ZZPvF=\"\n }\n}"
# headers = {
#     'Content-Type': "application/json",
#     'cache-control': "no-cache",
#     'Postman-Token': "32817f0a-2bbc-4b0a-b56e-e6ffbecc2f10"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)
#
# import requests
#
# url = "http://api.game.32solo.com/inno72/service/open"
#
# payload = "{\n\"serviceName\": \"standardShipment\",\n\"version\": \"1.0.0\",\n\"params\": {\n\t\"machineCode\": \"18028123\",\n\t\"sessionUuid\":\"18028123\",\n\t\"channelId\":\"56\",\n\t\"failChannelIds\":\"\"\n\t}\n}"
# headers = {
#     'Content-Type': "application/json",
#     'cache-control': "no-cache",
#     'Postman-Token': "a5ec6212-b60f-4c0d-9b40-5524d92a43b3"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)
#
#
# time.sleep(2)、


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DC_PATH = BASE_DIR + "districtcode.txt"

import random
import time
from datetime import datetime,timedelta,date


# 随机生成手机号码
def createPhone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
               "155", "156", "157", "158", "159", "186", "187", "188"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


# 随机生成身份证号
def getdistrictcode():
    with open(DC_PATH) as file:
        print DC_PATH
        data = file.read()
        print data
        districtlist = data.split('\n')
    for node in districtlist:
        # print node
        if node[10:11] != ' ':
            state = node[10:].strip()
        if node[10:11] == ' ' and node[12:13] != ' ':
            city = node[12:].strip()
        if node[10:11] == ' ' and node[12:13] == ' ':
            district = node[14:].strip()
            code = node[0:6]
            codelist.append({"state": state, "city": city, "district": district, "code": code})


def gennerator():
    global codelist
    codelist = []
    if not codelist:
        getdistrictcode()
    id = codelist[random.randint(0, len(codelist))]['code']  # 地区项
    id = id + str(random.randint(1930, 2013))  # 年份项
    da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
    id = id + da.strftime('%m%d')
    id = id + str(random.randint(100, 300))  # ，顺序号简单处理

    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                 '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
        count = count + int(id[i]) * weight[i]
        id = id + checkcode[str(count % 11)]  # 算出校验码
        return id


for i in range(10):
    print createPhone()

# getdistrictcode()



result = []
rows = mdb('inno72').MachineAppStatus.find()
for row in rows:
    found = False;
    if row['status'] is not None:
        for infos in row['status'] :
            if infos['appPackageName'] == 'com.inno72.zeusapp' or infos['appPackageName'] != 'com.inno72.monitorapp.tmall' :
                found = True;
    if not found:
        try:
            result.append([row['machineId']])
        except:
            pass


