# -*- coding: utf-8 -*-
import requests,json,time
from interface_project.base.basepage import BaseConfig
from Queue import Queue
import time,datetime
q = Queue()
import xlrd,xlwt


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
    print data
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



# 截图功能3/更新app信息2
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
    "appId":"19",
    "appVersion":"1",
    "appUrl":"http://inno72.oss.72solo.com/apk/prod/prod_monitor.apk ",
    "doTimeStr":"2018-11-06 18:51",
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
            print "task任务成功机器编号"+newmachineCode.encode('utf-8')
            q.put('p-%d' % i)
        else:
             print "task任务失败机器编号" +newmachineCode.encode('utf-8')+ "    "+newres['msg'].encode("utf-8")

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

success_send = []
failed_send = []
# 清除锁机
def sendfalseShip(Url,machineCode):
    data = {
    "machineCode":"123",
    "msg":{
        "type":3,
        "data":{
            "className":"",
            "methonName":"",
            "paramList":[
               9
            ]
        }
    }
}
    data['machineCode'] = machineCode
    data['msg']['type'] = 3
    data['msg']['data']['className'] = 'com.inno72.seventytwo.openapi.SeventyTwoApi'
    data['msg']['data']['methonName'] = 'setShipFailCountLock'
    data['msg']['data']['paramList'][0] = 9
    newdata = json.dumps(data)
    res = requests.request('POST', Url, data=newdata, headers=tokensnew())
    if res.status_code == 200:
        newres = res.json()
        i = 0
        fzhi =newres['data'][newmachineCode.encode('utf-8')].encode("utf-8")
        if fzhi =='发送成功':
            print "取消锁机成功："+newmachineCode.encode('utf-8')
            q.put('p-%d' % i)
            success_send.append(newmachineCode.encode('utf-8'))
        else:
            print "取消锁机失败："+newmachineCode.encode('utf-8')
            q.put('f-%d' % i)
            failed_send.append(newmachineCode.encode('utf-8'))
    else:
        return {"errcode": 9001, "errmsg": str(res)}

#处理机器code
def getcode(file_name):
    file_d = xlrd.open_workbook(file_name)
    # 获得第一个页签对象
    select_sheet = file_d.sheets()[0]

    machineCode = []
    # 获取总共的行数
    rows_num = select_sheet.nrows
    # 得到行数
    # print rows_num

    for row in xrange(rows_num):
        first_code = select_sheet.cell(row, 0).value
        machineCode.append(first_code)

    return machineCode

#写入excel数据
def write(file_name,passdata,failedata):
    file_d = xlwt.Workbook()
    sheet =file_d.add_sheet('sheet1')
    for i in range(0,len(failedata)):
        sheet.write(i,0,failedata[i])
    for i in range(0,len(passdata)):
        sheet.write(i,1,passdata)
    file_d.save(file_name)

# 切换app
def getcatapp(file_name):
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

    return  json.dumps(dict(zip(machineCode, machineId)))



if __name__=="__main__":
    # URL信息
    # 安装升级
    Url = BaseConfig().base_url + "/machine/machine/installApp"
    # 更新机器app信息2，截图3
    Urljiepin = BaseConfig().base_url + "/machine/machine/updateInfo"
    # 切换app
    URLwang = BaseConfig().base_url + "/machine/machine/cutApp"
    # push消息
    URLpush =   "http://api.app.inno72.com/push/pushMsg"
    # 添加任务升级
    URLtask = 'http://api.erp.inno72.com/machine/task/add'
    # 清除所机
    Shipurl = 'http://api.monitor.inno72.com/sendMsgToClient/sendMsgStr'
    # 数据信息
    appname = ['com.inno72.zeusapp']
    appurl = ['http://inno72.oss.72solo.com/apk/prod/prod_zeus1.0.1.apk']
    appversion = ['2']
    appId = ['19']
    # 机器信息数据
    # machineId=json.loads(getreaddata('testexcel.xls'))
    machineId = json.loads(getreadduodata('1120data.xls'))
    # machineId = json.loads(getcatapp('app1112.xls'))
    # machineId =getcode('app1112.xls')
    print machineId
    # # 存数据
    resultmachineId = []
    # 处理选择多机器
    for item in machineId:
        c = {"machineCode": item[0], "machineId": item[1]}
        resultmachineId.append(c)
        # print(resultmachineId)
    for i in range(len(resultmachineId)):
        newmachineCode= resultmachineId[i]['machineCode']
        newmachineId = resultmachineId[i]['machineId']
        # jiepin(Urljiepin, newmachineId, "2")

    # 处理多种app
    a = 0
    b = 0
    for a, b in enumerate(appurl):
        starttime()
        newappnew = ('{}'.format(b))
        newappname = ('{}'.format(appname[a]))
        newappurl = ('{}'.format(appurl[a]))
        newappversion = ('{}'.format(appversion[a]))
        newappid = ('{}'.format(appId[a]))
        tasDuoUpdata(URLtask,newappid,newappversion,newappurl,resultmachineId)
        # updataAPP(Url, newmachineId, appname[a], appurl[a], appversion[a])

    # for newmachineId in range(newmachineId):
        # sendfalseShip(Shipurl,newmachineCode)
        # jiepin(Urljiepin, newmachineId, "2")
        # time.sleep(1)
    # print('取消成功:{}'.format(success_send))
    # print('取消失败:{}'.format(failed_send))

    # for newmachineCode in machineId:
            # socket升级
            # updataAPP(Url, machineId[newmachineCode], b, appurl[a], appversion[a])
            # 任务升级
            # taskUpdata(URLtask,newappid,newappversion,newappurl,newmachineCode, machineId[newmachineCode])
            # push升级
            # push(URLpush,machineId[newmachineCode],newappurl,newappnew,newappversion)
            # 切换app
            # cutapp(URLwang, machineId[newmachineCode], "com.tmall.hudong.worldinpot")
            # 清除锁机
            # sendfalseShip(Shipurl,newmachineCode)
            # time.sleep(1)
            # 截图
            # jiepin(Urljiepin, machineId[newmachineCode], "3")

        # time.sleep(2)
        # print "---------------------------------------"
        # print "---------------------------------------"
        # print('成功机器编号:{}'.format(success_arr))
        # print('失败机器编号:{}'.format(failed_arr))

    endtime()
    print "一键共：" + str(len(machineId)) +" 台机器"
    p, f = auit_Count(q)
    c = len(appname)
    p1 = p/c
    f1 = f/c
    print '一键成功:%d' % p1, '-----', '一键失败:%d' % f1
    write('resultdata.xls',success_send,failed_send)

