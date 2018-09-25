# -*- coding: utf-8 -*-
import requests,json,time
from interface_project.base.basepage import BaseConfig
from Queue import Queue
import time,datetime
q = Queue()
import xlrd


'''
# 实现app自动升级包括socket push 

'''

# 获取开始时间
def starttime():
    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return times

# 获取结束时间
def endtime():
    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return times

#登录token 每次更新
def tokens():
    token = BaseConfig().base_token
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
    }
    headers['lf-None-Matoh'] = token
    return headers

# 登录token 每次更json
def tokensnew():
    token = BaseConfig().base_token
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
    }
    headers['lf-None-Matoh'] = token
    return headers

# 队列统计
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


success_arr = []
failed_arr = []
# 通过socket升级
def updataAPP(Url,machineId,appPackageName,appurl,versionCode):
    data = {"machineId": machineId, "appPackageName": appPackageName, "url": appurl,"versionCode": versionCode}
    res = requests.request('POST', Url, data=data, headers=tokens())

    if res.status_code == 200:
        newres = res.json()
        i = 0
        if newres['code'] ==0:
            print  "升级成功机器编号："+ newmachineCode.encode('utf-8') +"   "+appPackageName
            q.put('p-%d'%i)
            success_arr.append(newmachineCode.encode('utf-8'))
        else:
            print  "升级失败机器编号："+newmachineCode.encode('utf-8')+"   "+appPackageName+ "   "+newres['msg'].encode("utf-8")
            q.put('f-%d' % i)
            failed_arr.append(newmachineCode.encode('utf-8'))
    else:
        return {"errcode": 8888, "errmsg": str(res)}

    # print success_arr
    # print failed_arr

# 截图功能
def jiepin(Url,machineId,updateStatus):
    data = {"machineId": machineId, "updateStatus": updateStatus}
    res = requests.request('POST', Url, data=data, headers=tokens())
    if res.status_code == 200:
        newres = res.json()
        i = 0
        if newres['code'] ==0:
            print "截屏成功机器编号："+newmachineCode.encode('utf-8')
            q.put('p-%d' % i)
        else:
            print "截屏失败机器编号："+ newmachineCode.encode('utf-8')+ "   "+newres['msg'].encode("utf-8")
            q.put('f-%d' % i)
    else:
        return {"errcode": 9001, "errmsg": str(res)}

# 切换app功能
def cutapp(Url,machineId,cutdata):
    data = {"machineId": machineId, "appPackageName": cutdata}
    res = requests.request('POST', Url, data=data, headers=tokens())
    if res.status_code == 200:
        newres = res.json()
        i = 0
        if newres['code'] ==0:
            print "切换成功机器编号："+newmachineCode.encode('utf-8')
            q.put('p-%d' % i)
        else:
            print "切换失败机器编号："+newmachineCode.encode('utf-8') + "   "+newres['msg'].encode("utf-8")
            q.put('f-%d' % i)
    else:
        return {"errcode": 9001, "errmsg": str(res)}

# 通过push升级
def push(Url,machineId,appurl,appPackageName,versionCode):
    a = {"alias": "18047652","machineCode": "18047652","title": "1","text": "1","pushType":1,"msgInfo": {
        "apps": [{
            "url": "http://inno72.oss.72solo.com/apk/prod/prod_monitor.apk",
            "startStatus": 1,
            "appPackageName": "com.inno72.monitorapp",
            "versionCode": 9
        }]
    }
     }
    a['msgInfo']['apps'][0]['url'] = appurl
    a['msgInfo']['apps'][0]['appPackageName'] = appPackageName
    a['msgInfo']['apps'][0]['versionCode'] = versionCode
    a['alias'] = machineId
    a['machineCode'] = machineId
    datanew = a
    newdata = json.dumps(datanew)
    res = requests.request('POST',Url,data=newdata,headers= tokensnew())
    if res.status_code == 200:
        newres = res.json()
        i = 0
        if newres['code']==0:
            print "push成功机器编号"+newmachineCode.encode('utf-8')
            q.put('p-%d' % i)
        else:
            print "push失败机器编号" +newmachineCode.encode('utf-8') + "    "+newres['msg'].encode("utf-8")
    else:
        return {"errcode":9001,"errmsg":str(res)}

# type。  1升级 2卸载 3 合并 4 拆分
# doType    1 socket 2 push
# appId  0出场app。1新版壶中介 2数据中心 3监控app 4安装器 5管理app 6蓝牙接收器 7壶中介 8上传app 9守护app
# 多任务多机器任务升级
def taskUpdata(Url,appId,versionCode,appurl,machineCode,machineId):
    a = {"type":1,
    "appId":"2",
    "appVersion":"10",
    "appUrl":"http://inno72.oss.72solo.com/apk/prod/prod_monitor.apk ",
    "doTimeStr":"2018-09-18 18:51",
    "doType":1,
    "machineList":[{"machineCode":"18047652","machineId":"5d80295b4b144fbbb55b15e6d1f22ac0"}]}

    a['appId'] = appId
    a['appVersion'] = versionCode
    a['appUrl'] = appurl
    a['doTimeStr'] = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M")
    a['machineList'][0]['machineId'] = machineId
    a['machineList'][0]['machineCode'] = machineCode
    datanew = a
    newdata = json.dumps(datanew)
    res = requests.request('POST',Url,data=newdata,headers= tokensnew())
    if res.status_code == 200:
        newres = res.json()
        i = 0
        if newres['code']==0:
            print "task任务成功机器编号"+str(newmachineCode)
            q.put('p-%d' % i)
        else:
            print "task任务失败机器编号" +str(newmachineCode) + "    "+newres['msg'].encode("utf-8")
    else:
        return {"errcode":9001,"errmsg":str(res)}


# type。  1升级 2卸载 3 合并 4 拆分
# doType    1 socket 2 push
# appId  0出场app。1新版壶中介 2数据中心 3监控app 4安装器 5管理app 6蓝牙接收器 7壶中介 8上传app 9守护app
# 单一任务多机器
def tasDuoUpdata(Url,appId,versionCode,appurl,machineList):
    a = {"type":1,
    "appId":"2",
    "appVersion":"10",
    "appUrl":"http://inno72.oss.72solo.com/apk/prod/prod_monitor.apk ",
    "doTimeStr":"2018-09-18 18:51",
    "doType":1,
    "machineList":[{"machineCode":"18047652","machineId":"5d80295b4b144fbbb55b15e6d1f22ac0"}]}

    a['appId']= appId
    a['appVersion'] = versionCode
    a['appUrl'] = appurl
    a['doTimeStr'] = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M")
    a['machineList']=machineList

    datanew = a
    newdata = json.dumps(datanew)
    res = requests.request('POST',Url,data=newdata,headers= tokensnew())
    if res.status_code == 200:
        newres = res.json()
        i = 0
        if newres['code']==0:
            print "task任务成功机器编号"+duomachineCode.encode('utf-8')
            q.put('p-%d' % i)
        else:
             print "task任务失败机器编号" +duomachineCode.encode('utf-8')+ "    "+newres['msg'].encode("utf-8")

    else:
        return {"errcode":9001,"errmsg":str(res)}

# 单机器多任务excel处理
def getreaddata(file_name):
    file_d = xlrd.open_workbook(file_name)
    # 获得第一个页签对象
    select_sheet = file_d.sheets()[0]

    machineId = []
    machineCode = []
    # 获取总共的行数
    rows_num = select_sheet.nrows
    # 得到行数
    # print rows_num

    for row in xrange(rows_num):
        first_id = select_sheet.cell(row, 0).value
        first_code = select_sheet.cell(row,1).value
        machineId.append(first_id)
        machineCode.append(first_code)

    return json.dumps(dict(zip(machineCode, machineId)))

# 多机器单一任务升级
def getreadduodata(file_name):
    file_d = xlrd.open_workbook(file_name)
    # 获得第一个页签对象
    select_sheet = file_d.sheets()[0]

    machineId = []
    machineCode = []
    # 获取总共的行数
    rows_num = select_sheet.nrows
    # 得到行数
    # print rows_num

    for row in xrange(rows_num):
        first_id = select_sheet.cell(row, 0).value
        first_code = select_sheet.cell(row,1).value
        machineId.append(first_id)
        machineCode.append(first_code)

    return json.dumps(list(zip(machineCode, machineId)))

if __name__=="__main__":
    # URL信息
    Url = BaseConfig().base_url + "/machine/machine/installApp"
    Urljiepin = BaseConfig().base_url + "/machine/machine/updateInfo"
    URLwang = BaseConfig().base_url + "/machine/machine/cutApp"
    URLpush =   "http://api.app.inno72.com/push/pushMsg"
    URLtask = 'http://api.erp.inno72.com/machine/task/add'
    # 数据信息
    appname = ['com.inno72.dc']
    appurl = ['http://inno72.oss.72solo.com/apk/prod/prod_72dc.apk','http://inno72.oss.72solo.com/apk/prod/prod_72dd.apk']
    appversion = ['7','6']
    appId = ['2','3']
    # 机器信息数据
    # machineId=json.loads(getreaddata('testexcel.xls'))
    machineId = json.loads(getreadduodata('testexcel.xls'))
    # 存数据
    resultmachineId = []
    # 处理选择多机器
    for item in machineId:
        c = {"machineCode": item[0], "machineId": item[1]}
        resultmachineId.append(c)
    # print(resultmachineId)
    for i in range(len(resultmachineId)):
        duomachineCode= resultmachineId[i]['machineCode']
    #处理多种app
    a = 0
    b = 0
    for a, b in enumerate(appurl):
        starttime()
        newappnew = ('{}'.format(b))
        newappurl = ('{}'.format(appurl[a]))
        newappversion = ('{}'.format(appversion[a]))
        newappid = ('{}'.format(appId[a]))
        # print type(newappurl)
        # print newappversion
        tasDuoUpdata(URLtask,newappid,newappversion,newappurl,resultmachineId)
        for newmachineCode in machineId:
            # socket升级
            # updataAPP(Url, machineId[newmachineCode], b, appurl[a], appversion[a])
            # 任务升级
            # taskUpdata(URLtask,newappid,newappversion,newappurl,newmachineCode, machineId[newmachineCode])
            # push升级
            # push(URLpush,machineId[newmachineCode],newappurl,newappnew,newappversion)
            # 切换app
            # cutapp(URLwang, machineId[newmachineCode], "com.inno72.detection")
            time.sleep(1)
            # 截图
            # jiepin(Urljiepin, machineId[newmachineCode], "3")

        # time.sleep(2)
        print "---------------------------------------"
        print "---------------------------------------"
        print('升级成功机器编号:{}'.format(success_arr))
        print('升级失败机器编号:{}'.format(failed_arr))

    endtime()
    print "一键升级共：" + str(len(machineId)) +" 台机器"
    p, f = auit_Count(q)
    c = len(appname)
    p1 = p/c
    f1 = f/c
    print '一键升级成功:%d' % p1, '-----', '一键升级失败:%d' % f1