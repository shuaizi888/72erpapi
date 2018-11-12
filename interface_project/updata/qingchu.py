#coding:utf-8
#Author:sgao

import requests
import random
import json

url = "http://api.erp.inno72.com/project/game/update"


a = random.uniform(2,9)
num= round(a,1)
print num
name = 'name=宝洁游戏'
newversion= 'version='+str(num)
versionInno72 ='versionInno72='+str(num)
payload = "name=%E7%BE%8E%E7%9A%84%E6%B8%B8%E6%88%8F&version=2.3&versionInno72=2.3&minGoodsNum=1&maxGoodsNum=100&id=e8b6877e05eb473cb4247e3a1a7be50b"
newpayload= payload.split('&')
newpayload[0]=name
newpayload[1]=newversion
newpayload[2]=versionInno72
str ='&'
newpayload= str.join(newpayload)
data = {'name':'美的游戏','version':num,'versionInno72':num,'minGoodsNum':'1','maxGoodsNum':'100','id':'e8b6877e05eb473cb4247e3a1a7be50b'}
newdata = json.dumps(data)
# print newdata
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'lf-None-Matoh': "7d6230c680274140a5aa21301ae88c71",
    'Cache-Control': "no-cache",
    'Postman-Token': "673de9ad-f16b-4e3b-a3a7-333fd6c5b1ef"
    }

response = requests.request("POST", url, data=newpayload, headers=headers)