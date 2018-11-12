#coding:utf-8
#Author:sgao


import requests
import xlrd
import json

def getauto(file_name):
    file_d = xlrd.open_workbook(file_name)
    # 获得第一个页签对象
    select_sheet = file_d.sheets()[0]

    machineCode = ""
    # 获取总共的行数
    rows_num = select_sheet.nrows
    # 得到行数
    # print rows_num

    for row in xrange(rows_num):
        first_code = select_sheet.cell(row,0).value
        machineCode=machineCode+","+first_code


    machineCode= json.dumps(machineCode)
    return machineCode[2:-1]


machineCode =getauto('active1105.xls')
print machineCode
print '下载请求开始------'

sellerIdnew = ['2793765980','94298837','519286239','392147177']


URL = 'http://api.game.inno72.com/newretail/exportShop?machineCodes=18866930,18167346,18855618,18142657,18477194,18185926,18077290,18036898,18997043,18549893,18311559,18686817,18825970,18949928,18723031,18102837,18836352,18644680,18023296,18190436,18259962,18306847,18794266,18465285,18286294,18708176,18464240,18275232,18672381,18047652,18878893,18887734,18473549,18044540,18471129,18427348,18814458,18393177,18552411,18592730,18927056,18731990,18920857,18861049,18653932,18544784,18247254,18702260,18088910,18204066,18449573,18167928,18972441,18814458,18542418,18687884,18927898,18028352,18609882,18892484,18321918,18216922,18047652,18312420,18935831,18303435,18759062,18360377,18839548,18102392,18871694,18737283,18741576,18747736,18841088,18237675,18610184,18617242,18052968,18411944,18047652,18373894,18915513,18947581,18254891,18780812,18712774,18608492,18199442,18117790,18689796&sellerId=392147177'


oldsellerId =  URL.split('=')
oldmachineCode = oldsellerId[1].split('&')


with open('count1102.xls','wb') as code:
    for temp in sellerIdnew:
        new_url = oldsellerId[0] + '=' + machineCode+'&'+oldmachineCode[1] + "=" + temp
        print new_url
        r = requests.get(url=URL)
        code.write(r.content)


