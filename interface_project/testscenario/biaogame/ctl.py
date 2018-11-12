#coding:utf-8
#Author:sgao

import execjs
# ua: ctl.getUA(),
#         umid: ctl.getUmidToken(),


# ctx = execjs.compile('''function add(a,b){return a+b;}''')
# print (ctx.call('add',1,2))
# f = open('/Users/72cy-0101-01-0027/Desktop/work/script/erpapi/interface_project/testscenario/biaogame/js/hello.txt','r')
# print f.read()
# f1 = open('/Users/72cy-0101-01-0027/Desktop/work/script/erpapi/interface_project/testscenario/biaogame/js/ctl.js','r')
# print f1.read()

# 执行本地的js
def getua():
    ua = openjs()
    uactx = execjs.compile(ua) #加载JS文件
    return (uactx.call('getUA'))  #调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数

def getumid():
    umid = openjs()
    umidctx = execjs.compile(umid) #加载JS文件
    return (umidctx.call('getUmidToken'))  #调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数

def openjs():
    f = open("/Users/72cy-0101-01-0027/Desktop/work/script/erpapi/interface_project/testscenario/biaogame/js/ctl.js", 'r') # 打开JS文件
    line = f.read()
    print line


if __name__ == '__main__':
    print(getua())
    print(getumid())