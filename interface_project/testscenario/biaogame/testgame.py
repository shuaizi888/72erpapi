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
点72后台－API标准游戏服务接口场景
'''
@ddt.ddt
class TestBGameScenario(unittest.TestCase):#点72后台接口测试场景
    '''点72后台－API接口场景'''
    #初始化,setUp每个测试方法,执行一次;如果需要只执行一次使用setUpClass(cls)  需要classmethod修饰

    def setUp(self):
        self.configPath =  gl.configPath
        configyaml = os.path.join(self.configPath,'config.yaml')
        self.reportPath = gl.reportPath

    '''
        #获得活动信息>>预登录接口>>>polling用户登录session信息>>>>下单接口>>polling订单支付状态>>>>出货接口
    '''

    @unittest.skipIf(scripts.getRunFlag('testbiaoserverwu') == 'N', '验证执行配置')
    @ddt.data(*scripts.loadDdtData(Itype='s', filename='biaogame.yaml', caseflag='GAMECASEWU'))
    def testbiaoserverwu(self, data):
        '''获得活动信息->预登录接口->polling用户登录session信息->下单接口->polling订单支付状态->出货接口'''
        '''--------------------------获得活动信息----------------------'''
        # 整合数据，调用接口，获取返回结果
        #获得活动信息
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardFindActivitydata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )
        #断言
        machineCode = res['data']['machineCode']
        activityPlanId = res['data']['activityPlanId']
        activityId = res['data']['activityId']
        channelId = res['data']['channelId']
        print '各数据信息：' +'machineCode: '+ machineCode+'  ' +'activityPlanId: '+ activityPlanId+'  ' +'activityId: '+activityId+'  ' +'channelId: '+channelId
        self.assertEqual(res['code'],0,res['msg'])#断言


        '''--------------------------预登录接口无需登录----------------------'''
        # 整合数据，调用接口，获取返回结果
        #预登录接口
        data['standardPrepareLogindata']['params']['machineCode'] = machineCode

        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardPrepareLogindata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )

        sessionUuid = res['data']['sessionUuid']
        print 'sessionUuid: ' + sessionUuid
        #断言
        self.assertEqual(res['code'],0,res['msg'])



        '''--------------------------polling用户登录session信息----------------------'''
        # 整合数据，调用接口，获取返回结果
        #polling用户登录session信息
        data['standardSessionPollingdata']['params']['sessionUuid'] = sessionUuid

        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardSessionPollingdata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )
        userNick = res['data']['userNick']
        print userNick
        #断言
        self.assertEqual(res['code'],0,res['msg'])



        '''--------------------------下单接口----------------------'''
        # 整合数据，调用接口，获取返回结果
        #下单接口
        data['standardOrderdata']['params']['sessionUuid'] = sessionUuid

        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardOrderdata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )
        channelIds = res['data']['goods'][0]['channelIds'][0]
        print 'channelIds：'+channelIds
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言
        self.assertEqual(res['data']['orderResult'],0,res['msg'])
        # self.assertEqual(res['data']['lotteryResult'], 0, res['msg'])


        '''--------------------------出货接口----------------------'''
        # 整合数据，调用接口，获取返回结果
        #出货接口
        data['standardShipmentdata']['params']['sessionUuid'] = sessionUuid
        data['standardShipmentdata']['params']['machineCode'] = machineCode
        data['standardShipmentdata']['params']['channelId'] = channelIds
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardShipmentdata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言




    @unittest.skipIf(scripts.getRunFlag('testbiaoserverlogin') == 'N', '验证执行配置')
    @ddt.data(*scripts.loadDdtData(Itype='s', filename='biaogame.yaml', caseflag='GAMECASELOGIN'))
    def testbiaoserverlogin(self, data):
        '''获得活动信息->预登录接口->polling用户登录session信息->下单接口->polling订单支付状态->出货接口'''
        '''--------------------------获得活动信息----------------------'''
        # 整合数据，调用接口，获取返回结果
        #获得活动信息
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardFindActivitydata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )
        #断言
        machineCode = res['data']['machineCode']
        activityPlanId = res['data']['activityPlanId']
        activityId = res['data']['activityId']
        channelId = res['data']['channelId']
        print '各数据信息：' +'machineCode: '+ machineCode+'  ' +'activityPlanId: '+ activityPlanId+'  ' +'activityId: '+activityId+'  ' +'channelId: '+channelId
        self.assertEqual(res['code'],0,res['msg'])#断言


        '''--------------------------预登录接口无需登录----------------------'''
        # 整合数据，调用接口，获取返回结果
        #预登录接口
        data['standardPrepareLogindata']['params']['machineCode'] = machineCode

        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardPrepareLogindata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )

        sessionUuid = res['data']['sessionUuid']
        print 'sessionUuid: ' + sessionUuid
        #断言
        self.assertEqual(res['code'],0,res['msg'])
        print res['data']['qrCodeUrl']

        sleep(30)

        '''--------------------------polling用户登录session信息----------------------'''
        # 整合数据，调用接口，获取返回结果
        #polling用户登录session信息
        data['standardSessionPollingdata']['params']['sessionUuid'] = sessionUuid

        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardSessionPollingdata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )
        #断言
        userNick = res['data']['userNick']
        canOrder = res['data']['canOrder']
        goodsId = res['data']['goodsId']
        goodsCode = res['data']['goodsCode']
        print userNick
        print canOrder
        print goodsId
        print goodsCode
        #断言
        self.assertEqual(res['code'],0,res['msg'])
        self.assertTrue(res['data']['userNick'])
        self.assertEqual(res['data']['canOrder'],'true',res['msg'])
        self.assertEqual(res['data']['logged'],'true',res['msg'])
        self.assertTrue(res['data']['goodsId'])
        self.assertTrue(res['data']['goodsCode'])


        '''--------------------------下单接口----------------------'''
        # 整合数据，调用接口，获取返回结果
        #下单接口
        data['standardOrderdata']['params']['sessionUuid'] = sessionUuid

        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardOrderdata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )
        channelIds = res['data']['goods'][0]['channelIds'][0]
        payQrcodeImage = res['data']['payQrcodeImage']
        print 'channelIds：'+channelIds
        print 'payQrcodeImage: '+payQrcodeImage
        #断言
        self.assertEqual(res['code'],0,res['msg'])
        self.assertEqual(res['data']['orderResult'],0,res['msg'])




        '''--------------------------polling订单支付状态----------------------'''
        # 整合数据，调用接口，获取返回结果
        #polling订单支付状态
        data['standardOrderdata']['params']['sessionUuid'] = sessionUuid

        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardOrderdata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )
        channelIds = res['data']['goods'][0]['channelIds'][0]
        print 'channelIds：'+channelIds
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言
        self.assertEqual(res['data']['model'],'true',res['msg'])

        '''--------------------------出货接口----------------------'''
        # 整合数据，调用接口，获取返回结果
        #出货接口
        data['standardShipmentdata']['params']['sessionUuid'] = sessionUuid
        data['standardShipmentdata']['params']['machineCode'] = machineCode
        data['standardShipmentdata']['params']['channelId'] = channelIds
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardShipmentdata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言



    @unittest.skipIf(scripts.getRunFlag('testbiaoserverhulogin') == 'N', '验证执行配置')
    @ddt.data(*scripts.loadDdtData(Itype='s', filename='biaogame.yaml', caseflag='GAMECASEPAI'))
    def testbiaoserverhulogin(self, data):
        '''获得活动信息->预登录接口->polling用户登录session信息->下单接口->polling订单支付状态->出货接口'''
        '''--------------------------获得活动信息----------------------'''
        # 整合数据，调用接口，获取返回结果
        #获得活动信息
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardFindActivitydata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )
        #断言
        machineCode = res['data']['machineCode']
        activityPlanId = res['data']['activityPlanId']
        activityId = res['data']['activityId']
        channelId = res['data']['channelId']
        print '各数据信息：' +'machineCode: '+ machineCode+'  ' +'activityPlanId: '+ activityPlanId+'  ' +'activityId: '+activityId+'  ' +'channelId: '+channelId
        self.assertEqual(res['code'],0,res['msg'])#断言


        '''--------------------------预登录接口无需登录----------------------'''
        # 整合数据，调用接口，获取返回结果
        #预登录接口
        data['standardPrepareLogindata']['params']['machineCode'] = machineCode

        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardPrepareLogindata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )

        sessionUuid = res['data']['sessionUuid']
        print 'sessionUuid: ' + sessionUuid
        #断言
        self.assertEqual(res['code'],0,res['msg'])
        print res['data']['qrCodeUrl']

        sleep(30)

        '''--------------------------polling用户登录session信息----------------------'''
        # 整合数据，调用接口，获取返回结果
        #polling用户登录session信息
        data['standardSessionPollingdata']['params']['sessionUuid'] = sessionUuid

        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardSessionPollingdata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )
        #断言
        userNick = res['data']['userNick']
        canOrder = res['data']['canOrder']
        print userNick
        print canOrder
        #断言
        self.assertEqual(res['code'],0,res['msg'])
        self.assertTrue(res['data']['userNick'])
        self.assertEqual(res['data']['canOrder'],'true',res['msg'])
        self.assertEqual(res['data']['logged'],'true',res['msg'])


        '''--------------------------下单接口----------------------'''
        # 整合数据，调用接口，获取返回结果
        #下单接口
        data['standardOrderdata']['params']['sessionUuid'] = sessionUuid

        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardOrderdata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )
        channelIds = res['data']['goods'][0]['channelIds'][0]
        payQrcodeImage = res['data']['payQrcodeImage']
        orderResult = res['data']['orderResult']
        lotteryResult  = res['data']['lotteryResult']
        print 'channelIds：'+channelIds
        print 'payQrcodeImage: '+payQrcodeImage
        print '商品结果' + str(orderResult)
        print '优惠券结果' + str(lotteryResult)
        #断言
        self.assertEqual(res['code'],0,res['msg'])
        self.assertEqual(res['data']['orderResult'],0,res['msg'])




        '''--------------------------polling订单支付状态----------------------'''
        # 整合数据，调用接口，获取返回结果
        #polling订单支付状态
        data['standardOrderdata']['params']['sessionUuid'] = sessionUuid

        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardOrderdata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )
        channelIds = res['data']['goods'][0]['channelIds'][0]
        print 'channelIds：'+channelIds
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言
        self.assertEqual(res['data']['model'],'true',res['msg'])

        '''--------------------------出货接口----------------------'''
        # 整合数据，调用接口，获取返回结果
        #出货接口
        data['standardShipmentdata']['params']['sessionUuid'] = sessionUuid
        data['standardShipmentdata']['params']['machineCode'] = machineCode
        data['standardShipmentdata']['params']['channelId'] = channelIds
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardShipmentdata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言






if __name__=="__main__":

    suite = unittest.TestSuite()
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestBGameScenario)]
    suite.addTests(tests)

    filePath = os.path.join(gl.reportPath, 'gameReport.html')  # 确定生成报告的路径
    # print filePath

    with file(filePath, 'wb') as fp:
        runner = HTMLTESTRunnerCN.HTMLTestRunner(
            stream=fp,
            title=u'点72标准游戏服务接口自动化测试报告',
            description=u'详细测试用例结果',  # 不传默认为空
            tester=u"sgao"  # 测试人员名字，不传默认为小强
        )
        # 运行测试用例
        runner.run(suite)
        fp.close()
    emailinno.Emailinno().send