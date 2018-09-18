#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author      patrick
# created on  2018/9/17

import urllib
import urllib2
import json
import xlrd
import xlwt


def connectJsonHttp(url, data, header={}):
    header['Content-type'] = 'application/json'

    data = json.dumps(data)
    request = urllib2.Request(url, data, headers=header)
    opener = urllib2.build_opener()
    connector = opener.open(request)
    ret = connector.read()
    connector.close()
    return ret


def connectFormHttp(url, data, header={}, isPost=False):
    header['Content-type'] = 'application/x-www-form-urlencoded'
    if isPost:
        if data is not None:
            data = urllib.urlencode(data)
        request = urllib2.Request(url, data, headers=header)
    else:
        if data is not None:
            url = ("%s?%s")%(url, urllib.urlencode(data))
        request = urllib2.Request(url, headers=header)

    opener = urllib2.build_opener()
    connector = opener.open(request)
    ret = connector.read()
    connector.close()
    return ret



standardInfos = {

    'monitor-app': {'versionCode':12, 'url':'http://inno72.oss.72solo.com/apk/prod/prod_monitor1.1.2.apk',
     'appPackageName':'com.inno72.monitorapp'},
    # 'installerApp': {'versionCode':4, 'url':'http://inno72.oss.72solo.com/apk/prod/prod_installer1.0.3.apk',
    #  'appPackageName':'com.inno72.installer'},
    # 'detection': {'versionCode':9, 'url':'http://inno72.oss.72solo.com/apk/prod/prod_detection.apk', #
    #  'appPackageName':'com.inno72.detection'},
    # 'Dc': {'versionCode':6, 'url':'http://inno72.oss.72solo.com/apk/prod/prod_72dc1.1.0.apk',
    #  'appPackageName':'com.inno72.dc'},
    # 'demons': {'versionCode':4, 'url':'http://inno72.oss.72solo.com/apk/prod/prod_demons1.0.3.apk',# finnal
    #  'appPackageName':'com.inno72.demons'},
    # 'upload':{'versionCode':4, 'url':'http://inno72.oss.72solo.com/apk/prod/prod_upload1.0.3.apk',#
    #  'appPackageName':'com.inno72.upload'},
    # 'app': {'versionCode':4, 'url':'http://inno72.oss.72solo.com/apk/prod/prod_app0.0.4.apk',#
    #  'appPackageName':'com.tmall.hudong.worldinpot'},
    #'72App':{ 'versionCode':5, 'url':'http://inno72.oss.72solo.com/apk/prod/prod_72app.apk',
    #'appPackageName':'com.inno72.app'},
}

code2mid = {}
code2mid2 = {}


def pingApp():
    #with open("aaaa.txt") as f:
        # for url in f:
        #     ret = connectFormHttp(url, None, header={'lf-None-Matoh':'0b3591c929b940dbb0072b063ffc3fcc'})
        #     print ret
    loadCode2Mid()

    for key in code2mid.keys():
        #print code2mid[key]
        ret = connectFormHttp("http://api.erp.inno72.com/machine/machine/updateInfo?machineId=%s&updateStatus=2"%code2mid[key], None, header={'lf-None-Matoh': 'ce466c85860b43fd9ffccce36f11b1e6'})
        print ret


def loadCode2Mid():
    ExcelFile = xlrd.open_workbook(r'mid2code.xls')
    sheet = ExcelFile.sheet_by_index(0)

    rows = sheet.get_rows()
    for row in rows:
        code2mid[str(row[1].value)] = row[0].value

def loadCode2Mid2():
    ExcelFile = xlrd.open_workbook(r'mid2code2.xls')
    sheet = ExcelFile.sheet_by_index(0)

    rows = sheet.get_rows()
    for row in rows:
        code2mid2[str(row[1].value)] = {
            'ID':row[0].value,
            'name' : row[2].value,
            'net': int(row[3].value),

        }

def findMid(code):
    return code2mid[code]


def findNotCompleteMachine():
    loadCode2Mid2()
    ExcelFile = xlrd.open_workbook(r'ter_info.xls')
    sheet = ExcelFile.sheet_by_index(0)

    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet("数据")

    rows = sheet.get_rows()
    midInfos = []
    for row in rows:
        if row[0].value == 'createTime':
            continue
        midInfos.append({
            'mid': str(row[1].value),
            'time': str(row[0].value),
            'apps': eval(row[2].value),
        })


    worksheet.write(0, 0, "machine_code")
    worksheet.write(0, 1, "address")
    worksheet.write(0, 2, "net")

    j = 3
    for _, key in enumerate(standardInfos):
        worksheet.write(0, j, key)
        j +=1

    i=1
    j=0

    data = []

    for midInfo in midInfos:
        j = 0
        cur = []

        #worksheet.write(i, j, midInfo['mid'])

        j = j+1

        cur.append(midInfo['mid'])

        try:
            name = code2mid2[midInfo['mid']]['name']
        except KeyError:
            name = ""

        cur.append(name)

        #worksheet.write(i, j, name)
        j = j + 1

        try:
            net = code2mid2[midInfo['mid']]['net']
        except KeyError:
            net = 0

        cur.append(net)

        #worksheet.write(i, j, net)

        for _, key in enumerate(standardInfos):
            j = j + 1
            for app in midInfo['apps']:
                if standardInfos[key]['appPackageName'] == app['appPackageName'] and app['versionCode'] < standardInfos[key]['versionCode']:
                    #worksheet.write(i, j, app['versionCode'])
                    cur.append(app['versionCode'])
                    break
                    #print "not upgrade success mid:%s appPackageName:%s versionCode:%s"%(midInfo['mid'], app['appPackageName'], app['versionCode'])
                elif standardInfos[key]['appPackageName'] == app['appPackageName']:
                    #worksheet.write(i, j, '')
                    cur.append('')
                    break
        i= i+1
        data.append(cur)

    finalData = []

    # for line in data:
    #     if line[3] == '' and line[4] == '' and line[5] == '' and line[6] == '' and line[7] == '' and line[8] == '' and line[9] == '':
    #         pass
    #     else:
    #         finalData.append(line)



    # for key in code2mid2.keys():
    #     isFound = False
    #     for one in data:
    #         if one[0] == key:
    #             isFound=True
    #             break
    #     if not isFound:
    #         finalData.append([key, code2mid2[key]['name'], code2mid2[key]['net'], '', '', '', '', '', '', ''])
    #
    # print finalData

    i = 1
    for line in data:
        j = 0
        for item in line:
            worksheet.write(i, j, item)
            j +=1
        i +=1


    workbook.save("not_complete.xls")






def upgrade(appName, isPush=False, toClient=False):

    loadCode2Mid()

    ExcelFile = xlrd.open_workbook(r'ter_info.xls')
    sheet = ExcelFile.sheet_by_index(0)

    rows = sheet.get_rows()
    midInfos = []
    for row in rows:
        if row[0].value == 'createTime':
            continue
        midInfos.append({
            'mid': str(row[1].value),
            'apps': eval(row[2].value),
        })

    matchInfo = standardInfos[appName]

    errCode = []

    for midInfo in midInfos:

        if toClient:
            ret= connectJsonHttp("http://api.monitor.inno72.com/sendMsgToClient/sendMsgStr", {
                "machineCode": midInfo['mid'],
                "msg":
                    {"type": 1, "data": "pm install -r /sdcard/prod_installer1.0.3.apk"}})
            print ret
        else:
            for app in midInfo['apps']:
                if app['appPackageName'] == matchInfo['appPackageName'] and app['versionCode'] < matchInfo['versionCode']:

                    try:
                        mid = findMid(midInfo['mid'])
                    except KeyError:
                        errCode.append(midInfo['mid'])
                        continue


                    if not isPush:
                        print 'need upgrade installApp mid:%s appPackageName:%s versionCode:%s' % (
                            midInfo['mid'], app['appPackageName'], app['versionCode'])

                        ret = connectFormHttp('http://api.erp.inno72.com/machine/machine/installApp', {
                            'machineId':mid,
                            'appPackageName':app['appPackageName'],
                            'url':matchInfo['url'],
                            'versionCode': matchInfo['versionCode']
                        }, header={'lf-None-Matoh': '0b3591c929b940dbb0072b063ffc3fcc'})
                        print ret
                    else:
                        print 'need upgrade pushMsg mid:%s appPackageName:%s versionCode:%s' % (
                            midInfo['mid'], app['appPackageName'], app['versionCode'])

                        ret = connectJsonHttp('http://api.app.inno72.com/push/pushMsg', {
                            "alias": midInfo['mid'],
                            "machineCode": midInfo['mid'],
                            "title": "这是标题",
                            "text": "这是简介",
                            "pushType": 1,
                            "msgInfo": {
                                "apps": [{
                                    "url": matchInfo['url'],
                                    "startStatus": 1,
                                    "appPackageName": app['appPackageName'],
                                    "versionCode":matchInfo['versionCode']
                                }]
                            }

                        })
                        print ret
                elif app['appPackageName'] == matchInfo['appPackageName']:
                    print 'no upgrade mid:%s appPackageName:%s versionCode:%s' \
                          % (midInfo['mid'], app['appPackageName'], app['versionCode'])


    print "not match mid err_code %s"%errCode



import time

if __name__ == '__main__':

    # pingApp()
    # upgrade('installerApp', isPush=False)

    # keys = ['app','Dc', 'monitor-app', 'detection',  'upload',  'demons']
    keys = ['monitor-app']
    # while(True):
    #     for key in keys:
    #         print "******** %s begin ********"%key
    #         upgrade(key, isPush=True)
    #         if key != keys[-1]:
    #             print "******** %s end wait  ********" % key
    #             time.sleep(10 * 60)

    # print "******** ending   ********" % key

    findNotCompleteMachine()

    #upgrade("app", toClient=True)








