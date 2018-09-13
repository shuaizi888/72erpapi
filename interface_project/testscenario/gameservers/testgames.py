#coding:utf-8
#Author:sgao
import os,time,unittest
import requests,yaml,json,ddt
from interface_project.script.excel import Excel
from interface_project.base import basepage
from interface_project.script import gl
from interface_project.script import scripts
from interface_project.script import HTMLTESTRunnerCN
from interface_project.script.gamehttp import HttpWebRequest
from interface_project.script.gamehttp import HttpWebRequestnew
from time import sleep
from interface_project.script import emailinno

'''
点72后台－API接口场景
'''
@ddt.ddt
class TestScenario(unittest.TestCase):#点72后台接口测试场景
    '''点72后台－API接口场景'''
    #初始化,setUp每个测试方法,执行一次;如果需要只执行一次使用setUpClass(cls)  需要classmethod修饰

    def setUp(self):
        self.configPath =  gl.configPath
        configyaml = os.path.join(self.configPath,'config.yaml')
        self.reportPath = gl.reportPath

    '''
        #生成二维码->获取登录信息->查看游戏列表->查看商品信息->下单->查看订单状态->出货后商品减量
    '''

    @unittest.skipIf(scripts.getRunFlag('testgameserver') == 'N', '验证执行配置')
    @ddt.data(*scripts.loadDdtData(Itype='s', filename='gameserver.yaml', caseflag='GameServer'))
    def testgameserver(self, data):
        '''生成二维码->获取登录信息->查看游戏列表->查看商品信息->下单->查看订单状态->出货后商品减量'''
        '''--------------------------生成二维码----------------------'''
        machineId = '19294124'
        # 整合数据，调用接口，获取返回结果
        #生成二维码接口
        # res = scripts.loadtestInterface(
        #     instance=HttpWebRequestnew(),
        #     instance_pro='post',
        #     data=data['CreateQrCodedata'],
        #     desc=data['Desc'],
        #     url=data['GameUrl']
        # )
        Suuidcode = res['data']['qrCodeUrl']
        print "TMURL："+Suuidcode
        SUuidtoken =  res['data']['sessionUuid']
        print "Token："+SUuidtoken
        SUuidtokenNew = unicode.encode(SUuidtoken)
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言


        sleep(30)
        '''--------------------------获取登录信息----------------------'''
        Pdata = SUuidtokenNew
        eval(data['Pollingdata'])['params']['sessionUuid'] = Pdata

        # 整合数据，调用接口，获取返回结果
        poll = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data =json.dumps({"serviceName":"polling","params":{"sessionUuid":Pdata},"version":"1.0.0"}),
            desc=data['Desc'],
            url=data['GameUrl'],
            instance_pro='post'
        )


        self.assertEqual(poll['code'], 0, poll['msg'])  # 断言

        '''--------------------------查看游戏列表----------------------'''

        # 整合数据，调用接口，获取返回结果

        gamelist = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            # data['FindGamedata']
            data=json.dumps({"serviceName":"findGame","params":{"machineId":machineId,"planId":"","version":"2.0","versionInno72":"2.2"},"version":"1.0.0"}),
            desc=data['Desc'],
            url=data['GameUrl'],
            instance_pro='post'
        )
        activeplanid = gamelist['data']['activityPlanId']
        print "activityPlanId：" + activeplanid
        activityPlanIdNew = unicode.encode(activeplanid)

        activityid = gamelist['data']['activityId']
        print "activityId：" + activityid
        activityIdNew = unicode.encode(activityid)

        channelid = gamelist['data']['channelId']
        print "channelId：" + channelid
        channelIdNew = unicode.encode(channelid)

        planCodeid = gamelist['data']['planCode']
        print "planCodeid：" + planCodeid
        # planCodeidNew = unicode.encode(planCodeid)


        self.assertEqual(gamelist['code'], 0, gamelist['msg'])  # 断言

        '''--------------------------查看商品信息----------------------'''
        Acdata = activityPlanIdNew
        eval(data['FindProductdata'])['params']['activityPlanId'] = Acdata

        Chdata = channelIdNew
        eval(data['FindProductdata'])['params']['channelId'] = Chdata

        # 整合数据，调用接口，获取返回结果

        product = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=json.dumps({"serviceName":"findProduct","params":{"sessionUuid":Pdata,"machineId":machineId,"activityPlanId":Acdata,"channelId":Chdata,"report":"1"},"version":"1.0.0"}),
            desc=data['Desc'],
            url=data['GameUrl'],
            instance_pro='post'
        )
        FgoodsId = product['data']['goods'][0]['goodsId']
        print "goodsId：" + FgoodsId
        FgoodsIdNew = unicode.encode(FgoodsId)

        goodsNumId = product['data']['goods'][0]['goodsNum']
        print "goodsNumId：" + str(goodsNumId)

        channelids = product['data']['goods'][0]['channelIds'][0]
        print 'channelids:' + channelids
        channelidsNew = unicode.encode(FgoodsId)

        self.assertEqual(product['code'], 0, product['msg'])  # 断言

        '''--------------------------下单----------------------'''

        Oactividata = activityIdNew
        eval(data['Orderdata'])['params']['activityId'] = Oactividata

        Ochdata = channelIdNew
        eval(data['Orderdata'])['params']['channelId'] = Ochdata

        Ogoods = FgoodsIdNew
        eval(data['Orderdata'])['params']['itemId'] = Ogoods
        # 整合数据，调用接口，获取返回结果

        order = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=json.dumps({"serviceName":"order","params":{"sessionUuid":Pdata,"machineId":machineId,"activityPlanId":Acdata,"activityId":Oactividata,"channelId":Ochdata,"itemId":Ogoods},"version":"1.0.0"}),
            desc=data['Desc'],
            url=data['GameUrl'],
            instance_pro='post'
        )
        PorderId = order['data']['time']
        print "PorderId：" + str(PorderId)
        # PorderIdNew = unicode.encode(PorderId)

        self.assertEqual(order['code'], 0, order['msg'])  # 断言

        '''--------------------------查看订单状态----------------------'''
        # Pdata = eval(data['OrderPollingdata'])['params']['sessionUuid']
        # Pdata = SUuidtokenNew

        Orderdata = PorderId
        eval(data['Orderdata'])['params']['orderId'] = Orderdata

        # 整合数据，调用接口，获取返回结果

        orderpoll = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=json.dumps({"serviceName":"orderPolling","params":{"sessionUuid":Pdata,"orderId":Orderdata},"version":"1.0.0"}),
            desc=data['Desc'],
            url=data['GameUrl'],
            instance_pro='post'
        )
        self.assertEqual(orderpoll['code'], 0, orderpoll['msg'])  # 断言

        '''--------------------------出货后商品减量----------------------'''
        # Pdata = eval(data['ShipmentReportdata'])['params']['sessionUuid']
        # Pdata = SUuidtokenNew

        # 整合数据，调用接口，获取返回结果

        # channelids = channelidsNew
        # eval(data['ShipmentReportdata'])['params']['channelId'] = channelids

        shipreport = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            # data=data['ShipmentReportdata'],
            data=json.dumps({"serviceName":"shipmentReport","params":{"machineId":machineId,"channelId":channelids,"sessionUuid":Pdata,"orderId":Orderdata},"version":"1.0.0"}),
            desc=data['Desc'],
            url=data['GameUrl'],
            instance_pro='post'
        )
        self.assertEqual(shipreport['code'], 0, shipreport['msg'])  # 断言



if __name__=="__main__":

    suite = unittest.TestSuite()
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestScenario)]
    suite.addTests(tests)
    res = scripts.loadtestInterface(
        instance=HttpWebRequestnew(),
        instance_pro='post',
        data='{"serviceName":"createQrCode","params":{"machineId":"19294124"},"version":"1.0.0"}',
        desc='生成二维码',
        url='http://api.game.36solo.com/inno72/service/open'
    )

    filePath = os.path.join(gl.reportPath, 'gameReport.html')  # 确定生成报告的路径
    # print filePath

    with file(filePath, 'wb') as fp:
        runner = HTMLTESTRunnerCN.HTMLTestRunner(
            stream=fp,
            title=u'点72游戏服务接口自动化测试报告',
            description=u'详细测试用例结果',  # 不传默认为空
            tester=u"sgao"  # 测试人员名字，不传默认为小强
        )
        # 运行测试用例
        runner.run(suite)
        fp.close()
    emailinno.Emailinno().send