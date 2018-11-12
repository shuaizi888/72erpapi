#coding:utf-8
#Author:sgao

import requests
import json
import time


url = "http://api.game.36solo.com/inno72/service/open"
headers = {
    'Cache-Control': "no-cache",
    'Content-Type': "application/json",
    'Postman-Token': "d8aea2f5-df7b-49b4-88d7-94d06b6e3162"
    }

urlnew = "http://api.game.36solo.com/api/getSamplingNew"
headersnew = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache",
    'Content-Type': "application/form-data",
    'Postman-Token': "ddf12478-bc34-45c6-ab69-6a531d6b1a83"
    }
print '----------------------------------------------互动登录-----------------------------------------------'

print '------查看活动资源-----'

payload = "{\n\"serviceName\": \"standardFindActivity\",\n\n\"version\": \"1.0.0\",\n\"params\": {\n\"machineId\": \"18335598\",\n\"planId\": \"\",\n\"version\": \"\",\n\"versionInno72\": \"\"\n}\n}"
response = requests.request("POST", url, data=payload, headers=headers)
activity= response.json()
print json.dumps(activity).decode('unicode-escape')
res = activity
machineCode = res['data']['machineCode']
activityPlanId = res['data']['activityPlanId']
activityId = res['data']['activityId']
channelId = res['data']['channelId']
activityType = res['data']['activityType']
print 'machineCode: ' + machineCode + '  ' + 'activityPlanId: ' + activityPlanId + '  ' + 'activityId: ' + activityId + '  ' + 'channelId: ' + channelId

print'-------查看商品信息-------'

payload = "\n{\n\"serviceName\": \"getSampling\",\n\n\"version\": \"1.0.0\",\n\"params\": {\n\"machineCode\": \"18335598\"\n\n}\n}"
newpayload = json.loads(payload)
newpayload['params']['machineCode'] = machineCode
payload = json.dumps(newpayload)
response = requests.request("POST", url, data=payload, headers=headers)
samp= response.json()
print json.dumps(samp).decode('unicode-escape')

print '------------查看商品-------------'
payload = "{\n    \"serviceName\": \"findGoods\",\n    \"version\": \"1.0.0\",\n    \"params\": {\n        \"sessionUuid\": \"18335598\"\n    }\n}"
newpayload = json.loads(payload)
newpayload['params']['sessionUuid'] = machineCode
payload = json.dumps(newpayload)
response = requests.request("POST", url, data=payload, headers=headers)
samp= response.json()
print json.dumps(samp).decode('unicode-escape')
#
# print '预登录'
#
# payload = "{\"serviceName\": \"standardPrepareLogin\",\"version\": \"1.0.0\",\n\"params\": {\"machineCode\": \"18335598\",\n\t\t\t\"loginType\": 0,\n\t\t\t\"operType\":\"1\",\n\"ext\": {\"isVip\":1,\"itemId\": \"\",\"sessionKey\": \"6102622e6fb5de17af88c7be97eb0b10b488a33bbf793431589666223\",\"goodsCode\": \"576510091613\"}}}"
# response = requests.request("POST", url, data=payload, headers=headers)
#
# login= response.json()
# print json.dumps(login).decode('unicode-escape')

print'-------登录信息--------'


payload = "{\n\"serviceName\": \"standardSessionPolling\",\n\"version\": \"1.0.0\",\n\"params\": {\n\t\"sessionUuid\": \"18335598\"\n}\n}"
newpayload = json.loads(payload)
newpayload['params']['sessionUuid'] = machineCode
payload = json.dumps(newpayload)
response = requests.request("POST", url, data=payload, headers=headers)

sessionpolling= response.json()
print json.dumps(sessionpolling).decode('unicode-escape')
res =sessionpolling
userNick = res['data']['userNick']
canOrder = res['data']['canOrder']
goodsId = res['data']['goodsId']
goodsCode = res['data']['goodsCode']
isScanned = res['data']['isScanned']
countGoods = res['data']['countGoods']
sessionUuid = res['data']['sessionUuid']
sellerId = res['data']['sellerId']
print userNick
print canOrder
print goodsId
print goodsCode
print isScanned
print countGoods
print '商户code:   '+str(sellerId)
print '-------下单-------'


payload = "{\n \"serviceName\": \"standardOrder\",\n \"version\": \"1.0.0\",\n \"params\": {\n    \"sessionUuid\": \"18335598\",\n\t\"report\":\"2\",\n\t\"umid\":\"HV01WAAZ0b016b3adb8da9a45bbecde20691c5ee\",\n\t\"ua\":\"112#qWG4B+4Wyp++44+5FcHeTAEPoz8pDkHWpnZwXbw7jJiNxkxwceGxv7n1a5pS5i2R4wr0h+ZGtnON1vPuFiIegJcAgREAbQmk/c7mfAlwU/1k4FRzAH3v//ky+XaU07FiTEYsZAtWYqZ78i1ErYJOHyP259hIoMv+t1Uw2NYKcSolXcbgT7IZ4tNOSkSrk+y6/CPWu/WehxmcJOOeY71nLufgmqO/bW4Tz5UQxV8JH++suu8f9+iAlDX0BhCafLFNyHA/4PveWeNu45K/TdJINkH4qcimKTUzVJ16fBkfwsMxnrQzqp3pBT/m5P/RQ3zitnwHGMx3QijsX+1OcaZqXDVijW4jqi1CUsT4mBdXwRmsOwESIsyIvWhD0J3nlSkqm2bhxnoc5ms+3HrTlD5Hlq9m+cK1C4HX\"\n }\n}"
newpayload = json.loads(payload)
newpayload['params']['sessionUuid'] = sessionUuid
payload = json.dumps(newpayload)

print payload
response = requests.request("POST", url, data=payload, headers=headers)

order= response.json()
print json.dumps(order).decode('unicode-escape')
res = order
channelIds = res['data']['goods'][0]['channelIds'][0]
payQrcodeImage = res['data']['payQrcodeImage']
print 'channelIds:' + channelIds
print 'payQrcodeImage: ' + payQrcodeImage
print '--------下单信息-------'


payload = "{\n\"serviceName\": \"standardOrderPolling\",\n\"version\": \"1.0.0\",\n\"params\": {\n\"sessionUuid\": \"18335598\",\n\"orderId\": \"\"\n\n}\n}"

newpayload = json.loads(payload)
newpayload['params']['sessionUuid'] = sessionUuid
payload = json.dumps(newpayload)
response = requests.request("POST", url, data=payload, headers=headers)
orderpolling= response.json()
print json.dumps(orderpolling).decode('unicode-escape')

print '-------出货----------'


payload = "{\n\"serviceName\": \"standardShipment\",\n\"version\": \"1.0.0\",\n\"params\": {\n\t\"machineCode\": \"18335598\",\n\t\"sessionUuid\":\"18335598\",\n\t\"channelId\":\"52\",\n\t\"failChannelIds\":\"\"\n\t}\n}"
newpayload = json.loads(payload)
newpayload['params']['machineCode'] = machineCode
newpayload['params']['sessionUuid'] = sessionUuid
newpayload['params']['channelId'] = channelIds
payload = json.dumps(newpayload)
print payload
response = requests.request("POST", url, data=payload, headers=headers)
shipment= response.json()
print json.dumps(shipment).decode('unicode-escape')



print '---------------------------------无需登录-------------------------------'

#
# print '----------查看活动资源-------'
#
# payload = "{\n\"serviceName\": \"standardFindActivity\",\n\n\"version\": \"1.0.0\",\n\"params\": {\n\"machineId\": \"18335598\",\n\"planId\": \"\",\n\"version\": \"\",\n\"versionInno72\": \"\"\n}\n}"
# response = requests.request("POST", url, data=payload, headers=headers)
# activity= response.json()
# print json.dumps(activity).decode('unicode-escape')
#
# print'--------查看商品信息---------'
#
# payload = "\n{\n\"serviceName\": \"getSampling\",\n\n\"version\": \"1.0.0\",\n\"params\": {\n\"machineCode\": \"18335598\"\n\n}\n}"
#
# response = requests.request("POST", url, data=payload, headers=headers)
# samp= response.json()
# print json.dumps(samp).decode('unicode-escape')
#
# print '----------预登录------'
#
# payload = "{\"serviceName\": \"standardPrepareLogin\",\"version\": \"1.0.0\",\n\"params\": {\"machineCode\": \"18335598\",\n\t\t\t\"loginType\": 1,\n\t\t\t\"operType\":\"1\",\n\"ext\": {\"isVip\":0,\"itemId\": \"\",\"sessionKey\": \"\",\"goodsCode\": \"\"}}}"
# response = requests.request("POST", url, data=payload, headers=headers)
#
# login= response.json()
# print json.dumps(login).decode('unicode-escape')
#
# print'-------登录信息---------'
#
#
# payload = "{\n\"serviceName\": \"standardSessionPolling\",\n\"version\": \"1.0.0\",\n\"params\": {\n\t\"sessionUuid\": \"18335598\"\n}\n}"
# response = requests.request("POST", url, data=payload, headers=headers)
#
# sessionpolling= response.json()
# print json.dumps(sessionpolling).decode('unicode-escape')
#
# print '-----------下单---------'
#
#
# payload = "{\n \"serviceName\": \"standardOrder\",\n \"version\": \"1.0.0\",\n \"params\": {\n    \"sessionUuid\": \"18335598\",\n\t\"report\":\"1\",\n\t\"umid\":\"HV01WAAZ0b016b3adb8da9a45bbecde20691c5ee\",\n\t\"ua\":\"112#qWG4B+4Wyp++44+5FcHeTAEPoz8pDkHWpnZwXbw7jJiNxkxwceGxv7n1a5pS5i2R4wr0h+ZGtnON1vPuFiIegJcAgREAbQmk/c7mfAlwU/1k4FRzAH3v//ky+XaU07FiTEYsZAtWYqZ78i1ErYJOHyP259hIoMv+t1Uw2NYKcSolXcbgT7IZ4tNOSkSrk+y6/CPWu/WehxmcJOOeY71nLufgmqO/bW4Tz5UQxV8JH++suu8f9+iAlDX0BhCafLFNyHA/4PveWeNu45K/TdJINkH4qcimKTUzVJ16fBkfwsMxnrQzqp3pBT/m5P/RQ3zitnwHGMx3QijsX+1OcaZqXDVijW4jqi1CUsT4mBdXwRmsOwESIsyIvWhD0J3nlSkqm2bhxnoc5ms+3HrTlD5Hlq9m+cK1C4HX\"\n }\n}"
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# order= response.json()
# print json.dumps(order).decode('unicode-escape')
#
# print '-------下单信息----------'
#
#
# payload = "{\n\"serviceName\": \"standardOrderPolling\",\n\"version\": \"1.0.0\",\n\"params\": {\n\"sessionUuid\": \"18335598\",\n\"orderId\": \"\"\n\n}\n}"
#
#
# response = requests.request("POST", url, data=payload, headers=headers)
# orderpolling= response.json()
# print json.dumps(orderpolling).decode('unicode-escape')
#
# print '--------出货----------'
#
#
# payload = "{\n\"serviceName\": \"standardShipment\",\n\"version\": \"1.0.0\",\n\"params\": {\n\t\"machineCode\": \"18335598\",\n\t\"sessionUuid\":\"18335598\",\n\t\"channelId\":\"52\",\n\t\"failChannelIds\":\"\"\n\t}\n}"
#
# response = requests.request("POST", url, data=payload, headers=headers)
# shipment= response.json()
# print json.dumps(shipment).decode('unicode-escape')
#

print '------------------------------------------登录入会校园派样--------------------------------------------------'

print '------查看活动资源---------'

payload = "{\n\"serviceName\": \"standardFindActivity\",\n\n\"version\": \"1.0.0\",\n\"params\": {\n\"machineId\": \"18774616\",\n\"planId\": \"\",\n\"version\": \"\",\n\"versionInno72\": \"\"\n}\n}"
response = requests.request("POST", url, data=payload, headers=headers)
activity= response.json()
print json.dumps(activity).decode('unicode-escape')
res = activity
machineCode = res['data']['machineCode']
activityPlanId = res['data']['activityPlanId']
activityId = res['data']['activityId']
channelId = res['data']['channelId']
activityType = res['data']['activityType']
print 'machineCode: ' + machineCode + '  ' + 'activityPlanId: ' + activityPlanId + '  ' + 'activityId: ' + activityId + '  ' + 'channelId: ' + channelId

print'--------查看商品信息---------'

payload = "\n{\n\"serviceName\": \"getSampling\",\n\n\"version\": \"1.0.0\",\n\"params\": {\n\"machineCode\": \"18774616\"\n\n}\n}"
newpayload = json.loads(payload)
newpayload['params']['machineCode'] = machineCode
payload = json.dumps(newpayload)
response = requests.request("POST", url, data=payload, headers=headers)
samp= response.json()
print json.dumps(samp).decode('unicode-escape')

# print '预登录'
#
# payload = "{\"serviceName\": \"standardPrepareLogin\",\"version\": \"1.0.0\",\"params\": {\"machineCode\": \"18774616\",\"loginType\": 0,\"operType\":\"1\",\"ext\": {\"isVip\": 1,\"itemId\": \"67f0aaeb38944527b1db4a52e4b580be\",\"sessionKey\": \"6102622e6fb5de17af88c7be97eb0b10b488a33bbf793431589666223\"}}}"
# response = requests.request("POST", url, data=payload, headers=headers)
#
# login= response.json()
# print json.dumps(login).decode('unicode-escape')


print '------------查看商品-------------'
payload = "{\n    \"serviceName\": \"findGoods\",\n    \"version\": \"1.0.0\",\n    \"params\": {\n        \"sessionUuid\": \"18335598\"\n    }\n}"
newpayload = json.loads(payload)
newpayload['params']['sessionUuid'] = machineCode
payload = json.dumps(newpayload)
response = requests.request("POST", url, data=payload, headers=headers)
samp= response.json()
print json.dumps(samp).decode('unicode-escape')


print'-------登录信息-------'


payload = "{\n\"serviceName\": \"standardSessionPolling\",\n\"version\": \"1.0.0\",\n\"params\": {\n\t\"sessionUuid\": \"18774616\"\n}\n}"
response = requests.request("POST", url, data=payload, headers=headers)

sessionpolling= response.json()
print json.dumps(sessionpolling).decode('unicode-escape')
res = sessionpolling
userNick = res['data']['userNick']
canOrder = res['data']['canOrder']
goodsId = res['data']['goodsId']
goodsCode = res['data']['goodsCode']
isScanned = res['data']['isScanned']
countGoods = res['data']['countGoods']
sessionUuid = res['data']['sessionUuid']
sellerId = res['data']['sellerId']
print userNick
print canOrder
print goodsId
print goodsCode
print isScanned
print countGoods
print sessionUuid
print '商户code:   '+str(sellerId)
print '--------下单-------'
payload = "{\n \"serviceName\": \"standardOrder\",\n \"version\": \"1.0.0\",\n \"params\": {\n    \"sessionUuid\": \"18774616\",\n\t\"report\":\"\",\n\t\"umid\":\"HV01WAAZ0b016b3adb8da9a45bbecde20691c5ee\",\n\t\"ua\":\"112#qWG4B+4Wyp++44+5FcHeTAEPoz8pDkHWpnZwXbw7jJiNxkxwceGxv7n1a5pS5i2R4wr0h+ZGtnON1vPuFiIegJcAgREAbQmk/c7mfAlwU/1k4FRzAH3v//ky+XaU07FiTEYsZAtWYqZ78i1ErYJOHyP259hIoMv+t1Uw2NYKcSolXcbgT7IZ4tNOSkSrk+y6/CPWu/WehxmcJOOeY71nLufgmqO/bW4Tz5UQxV8JH++suu8f9+iAlDX0BhCafLFNyHA/4PveWeNu45K/TdJINkH4qcimKTUzVJ16fBkfwsMxnrQzqp3pBT/m5P/RQ3zitnwHGMx3QijsX+1OcaZqXDVijW4jqi1CUsT4mBdXwRmsOwESIsyIvWhD0J3nlSkqm2bhxnoc5ms+3HrTlD5Hlq9m+cK1C4HX\"\n }\n}"

newpayload = json.loads(payload)
newpayload['params']['sessionUuid'] = machineCode
payload = json.dumps(newpayload)
print payload
response = requests.request("POST", url, data=payload, headers=headers)

order= response.json()
print json.dumps(order).decode('unicode-escape')
res = order
channelIds = res['data']['goods'][0]['channelIds'][0]
payQrcodeImage = res['data']['payQrcodeImage']
print 'channelIds:' + channelIds
print 'payQrcodeImage: ' + payQrcodeImage



print '--------下单信息-------'


payload = "{\n\"serviceName\": \"standardOrderPolling\",\n\"version\": \"1.0.0\",\n\"params\": {\n\"sessionUuid\": \"18774616\",\n\"orderId\": \"\"\n\n}\n}"
newpayload = json.loads(payload)
newpayload['params']['sessionUuid'] = sessionUuid
payload = json.dumps(newpayload)

response = requests.request("POST", url, data=payload, headers=headers)
orderpolling= response.json()
print json.dumps(orderpolling).decode('unicode-escape')

print '---------出货-------'


payload = "{\n\"serviceName\": \"standardShipment\",\n\"version\": \"1.0.0\",\n\"params\": {\n\t\"machineCode\": \"18774616\",\n\t\"sessionUuid\":\"18774616\",\n\t\"channelId\":\"12\",\n\t\"failChannelIds\":\"\"\n\t}\n}"
newpayload = json.loads(payload)
newpayload['params']['channelId'] = channelIds
newpayload['params']['sessionUuid'] = sessionUuid
newpayload['params']['machineCode'] = machineCode
payload = json.dumps(newpayload)
response = requests.request("POST", url, data=payload, headers=headers)
shipment= response.json()
print json.dumps(shipment).decode('unicode-escape')


print '----------------------------------------------登录新互派---------------------------------------------'


print '-------查看活动资源-------'

payload = "{\n\"serviceName\": \"standardFindActivity\",\n\n\"version\": \"1.0.0\",\n\"params\": {\n\"machineId\": \"18383061\",\n\"planId\": \"\",\n\"version\": \"\",\n\"versionInno72\": \"\"\n}\n}"
response = requests.request("POST", url, data=payload, headers=headers)
activity= response.json()
print json.dumps(activity).decode('unicode-escape')
res = activity
machineCode = res['data']['machineCode']
activityPlanId = res['data']['activityPlanId']
activityId = res['data']['activityId']
activityType = res['data']['activityType']
print activityType
print 'machineCode: ' + machineCode + '  ' + 'activityPlanId: ' + activityPlanId + '  ' + 'activityId: ' + activityId

print'------查看商品信息------'

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"machineCode\"\r\n\r\n18383061\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

response = requests.request("POST", urlnew, data=payload, headers=headersnew)
samp= response.json()
print json.dumps(samp).decode('unicode-escape')
res = samp
newgoodid = res['data'][0]['id']
newgoodcode = res['data'][0]['code']
newsellerid = res['data'][0]['sellerId']
newshopId = res['data'][0]['shopId']
newsessionKey = res['data'][0]['sessionKey']
newnum = res['data'][0]['num']
print newgoodid, newgoodcode, newsellerid, newshopId, newsessionKey, newnum


# print '预登录'
#
# payload = "{\"serviceName\": \"standardPrepareLogin\",\"version\": \"1.0.0\",\"params\": {\"machineCode\": \"18383061\",\"loginType\": 0,\"operType\":\"1\",\"ext\": {\"isVip\": 1,\"itemId\": \"bdaa0181cb9648b680ba6ca4c25d11c2\",\"sessionKey\": \"61013020f71ce7d140b192f3280c377b81e828b6ec9584c3098056950\",\"goodsCode\": \"\"}}}\n"
# response = requests.request("POST", url, data=payload, headers=headers)
#
# login= response.json()
# print json.dumps(login).decode('unicode-escape')

print'------登录信息-------'


payload = "{\n\"serviceName\": \"standardSessionPolling\",\n\"version\": \"1.0.0\",\n\"params\": {\n\t\"sessionUuid\": \"18383061\"\n}\n}"
newpayload = json.loads(payload)
newpayload['params']['sessionUuid'] = machineCode
payload = json.dumps(newpayload)

response = requests.request("POST", url, data=payload, headers=headers)

sessionpolling= response.json()
print json.dumps(sessionpolling).decode('unicode-escape')
res = sessionpolling
userNick = res['data']['userNick']
canOrder = res['data']['canOrder']
canGame = res['data']['canGame']
goodsId = res['data']['goodsId']
goodsCode = res['data']['goodsCode']
isScanned = res['data']['isScanned']
countGoods = res['data']['countGoods']
sellerId = res['data']['sellerId']
print userNick
print canOrder
print goodsId
print goodsCode
print isScanned
print countGoods
print canGame
print '商户code:   '+str(sellerId)
print '----------下单--------'


payload = "{\n \"serviceName\": \"standardOrder\",\n \"version\": \"1.0.0\",\n \"params\": {\n    \"sessionUuid\": \"18383061\",\n\t\"report\":\"\",\n\t\"umid\":\"HV01WAAZ0b016b3adb8da9a45bbecde20691c5ee\",\n\t\"ua\":\"112#qWG4B+4Wyp++44+5FcHeTAEPoz8pDkHWpnZwXbw7jJiNxkxwceGxv7n1a5pS5i2R4wr0h+ZGtnON1vPuFiIegJcAgREAbQmk/c7mfAlwU/1k4FRzAH3v//ky+XaU07FiTEYsZAtWYqZ78i1ErYJOHyP259hIoMv+t1Uw2NYKcSolXcbgT7IZ4tNOSkSrk+y6/CPWu/WehxmcJOOeY71nLufgmqO/bW4Tz5UQxV8JH++suu8f9+iAlDX0BhCafLFNyHA/4PveWeNu45K/TdJINkH4qcimKTUzVJ16fBkfwsMxnrQzqp3pBT/m5P/RQ3zitnwHGMx3QijsX+1OcaZqXDVijW4jqi1CUsT4mBdXwRmsOwESIsyIvWhD0J3nlSkqm2bhxnoc5ms+3HrTlD5Hlq9m+cK1C4HX\"\n }\n}"

newpayload = json.loads(payload)
newpayload['params']['sessionUuid'] = machineCode
payload = json.dumps(newpayload)

print payload
response = requests.request("POST", url, data=payload, headers=headers)

order= response.json()
print json.dumps(order).decode('unicode-escape')
res = order
channelIds = res['data']['goods'][0]['channelIds'][0]
payQrcodeImage = res['data']['payQrcodeImage']
print 'channelIds:' + channelIds
print 'payQrcodeImage: ' + payQrcodeImage

print '----------------------'


print '--------下单信息---------'
payload = "{\n\"serviceName\": \"standardOrderPolling\",\n\"version\": \"1.0.0\",\n\"params\": {\n\"sessionUuid\": \"18383061\",\n\"orderId\": \"\"\n\n}\n}"
newpayload = json.loads(payload)
newpayload['params']['sessionUuid'] = machineCode
payload = json.dumps(newpayload)
response = requests.request("POST", url, data=payload, headers=headers)
orderpolling= response.json()
print json.dumps(orderpolling).decode('unicode-escape')

print '---------出货---------'


payload = "{\n\"serviceName\": \"standardShipment\",\n\"version\": \"1.0.0\",\n\"params\": {\n\t\"machineCode\": \"18383061\",\n\t\"sessionUuid\":\"18383061\",\n\t\"channelId\":\"1\",\n\t\"failChannelIds\":\"\"\n\t}\n}"
newpayload = json.loads(payload)
newpayload['params']['sessionUuid'] = machineCode
newpayload['params']['machineCode'] = machineCode
newpayload['params']['channelId'] = channelIds
payload = json.dumps(newpayload)
print payload
response = requests.request("POST", url, data=payload, headers=headers)
shipment= response.json()
print json.dumps(shipment).decode('unicode-escape')


# 优惠券登录

# print '--------------优惠券登录--------------'
# payload = "{\"serviceName\": \"standardPrepareLogin\",\n  \"version\": \"1.0.0\",\n  \"params\": {\"machineCode\": \"18257189\",\n              \"loginType\": 0,\n               \"operType\":\"1\",\n               \"ext\": {\"isVip\": 0,\"itemId\": \"606eae77c9a140c2a23dd3b50a03948b\",\"sessionKey\": \"\",\"goodsCode\": \"\"}\n            }\n            \n\t\n}"
#
# response = requests.request("POST", url, data=payload, headers=headers)
# login= response.json()
# print json.dumps(login).decode('unicode-escape')
# res = login
# ysessionUuid = res['data']['sessionUuid']

print'------优惠券登录信息-------'


payload = "{\n\"serviceName\": \"standardSessionPolling\",\n\"version\": \"1.0.0\",\n\"params\": {\n\t\"sessionUuid\": \"18257189\"\n}\n}"

# newpayload = json.loads(payload)
# newpayload['params']['sessionUuid'] = ysessionUuid
# payload = json.dumps(newpayload)

response = requests.request("POST", url, data=payload, headers=headers)

sessionpolling= response.json()
print json.dumps(sessionpolling).decode('unicode-escape')
res = sessionpolling
userNick = res['data']['userNick']
canOrder = res['data']['canOrder']
canGame = res['data']['canGame']
goodsId = res['data']['goodsId']
goodsCode = res['data']['goodsCode']
isScanned = res['data']['isScanned']
countGoods = res['data']['countGoods']
sellerId = res['data']['sellerId']
ysessionUuid = res['data']['sessionUuid']
print userNick
print canOrder
print goodsId
print goodsCode
print isScanned
print countGoods
print canGame
print '商户code:   '+str(sellerId)
print '----------下单--------'


payload = "{\n \"serviceName\": \"standardOrder\",\n \"version\": \"1.0.0\",\n \"params\": {\n    \"sessionUuid\": \"18257189\",\n\t\"report\":\"\",\n\t\"umid\":\"HV01WAAZ0b016b3adb8da9a45bbecde20691c5ee\",\n\t\"ua\":\"112#qWG4B+4Wyp++44+5FcHeTAEPoz8pDkHWpnZwXbw7jJiNxkxwceGxv7n1a5pS5i2R4wr0h+ZGtnON1vPuFiIegJcAgREAbQmk/c7mfAlwU/1k4FRzAH3v//ky+XaU07FiTEYsZAtWYqZ78i1ErYJOHyP259hIoMv+t1Uw2NYKcSolXcbgT7IZ4tNOSkSrk+y6/CPWu/WehxmcJOOeY71nLufgmqO/bW4Tz5UQxV8JH++suu8f9+iAlDX0BhCafLFNyHA/4PveWeNu45K/TdJINkH4qcimKTUzVJ16fBkfwsMxnrQzqp3pBT/m5P/RQ3zitnwHGMx3QijsX+1OcaZqXDVijW4jqi1CUsT4mBdXwRmsOwESIsyIvWhD0J3nlSkqm2bhxnoc5ms+3HrTlD5Hlq9m+cK1C4HX\"\n }\n}"

newpayload = json.loads(payload)
newpayload['params']['sessionUuid'] = ysessionUuid
payload = json.dumps(newpayload)

print payload
response = requests.request("POST", url, data=payload, headers=headers)

order= response.json()
print json.dumps(order).decode('unicode-escape')
res = order
orderResult = res['data']['orderResult']
payQrcodeImage = res['data']['payQrcodeImage']
print 'orderResult:' + str(orderResult)
print 'payQrcodeImage: ' + payQrcodeImage





