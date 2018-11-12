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
from interface_project.script.gamehttp import HttpWebRequests
from interface_project.script.gamehttp import HttpWebRequestget
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

    @unittest.skipIf(scripts.getRunFlag('testbiaoservernewhulogin') == 'N', '验证执行配置')
    @ddt.data(*scripts.loadDdtData(Itype='s', filename='biaogame.yaml', caseflag='GAMECASENEWHUPAI'))
    def testbiaoservernewhulogin(self, data):
        '''获得活动信息->预登录接口->polling用户登录session信息->下单接口->polling订单支付状态->出货接口'''

        '''--------------------------预登录接口需登录----------------------'''
        # 整合数据，调用接口，获取返回结果
        #预登录接口
        # data['standardPrepareLogindata']['params']['machineCode'] = machineCode
        #
        # res = scripts.loadtestInterface(
        #     instance=HttpWebRequest(),
        #     instance_pro='post',
        #     data=json.dumps(data['standardPrepareLogindata']),
        #     desc=data['Desc'],
        #     url=data['GameUrl']
        # )

        # sessionUuid = reslogin['data']['sessionUuid']
        # print 'sessionUuid: ' + sessionUuid
        # #断言
        # self.assertEqual(reslogin['code'],0,reslogin['msg'])
        # print reslogin['data']['qrCodeUrl']
        #
        sleep(30)


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
        activityType = res['data']['activityType']
        print activityType
        print '各数据信息：' +'machineCode: '+ machineCode+'  ' +'activityPlanId: '+ activityPlanId+'  ' +'activityId: '+activityId
        self.assertEqual(res['code'],0,res['msg'])#断言
        self.assertEqual(res['data']['activityType'], 1, res['msg'])


        '''--------------------------获取商品信息----------------------'''
        # 整合数据，调用接口，获取返回结果
        #下单接口
        # data['standardgetSamplingNew']['machineCode'] = machineCode

        res = scripts.loadtestInterface(
            instance=HttpWebRequestget(),
            instance_pro='post',
            data='------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"machineCode\"\r\n\r\n18383061\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--',
            desc=data['Desc'],
            url=data['GoodsUrl']
        )

        newgoodid = res['data'][0]['id']
        newgoodcode = res['data'][0]['code']
        newsellerid = res['data'][0]['sellerId']
        newshopId = res['data'][0]['shopId']
        newsessionKey = res['data'][0]['sessionKey']
        newnum = res['data'][0]['num']
        print newgoodid,newgoodcode,newsellerid,newshopId,newsessionKey,newnum
        #断言
        self.assertEqual(res['code'],0,res['msg'])

        '''--------------------------polling用户登录session信息----------------------'''
        # 整合数据，调用接口，获取返回结果
        #polling用户登录session信息
        data['standardSessionPollingdata']['params']['sessionUuid'] = machineCode

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
        isScanned = res['data']['isScanned']
        countGoods = res['data']['countGoods']
        sellerId = res['data']['sellerId']

        print userNick
        print canOrder
        print goodsId
        print goodsCode
        print isScanned
        print countGoods
        print sellerId
        #断言
        self.assertEqual(res['code'],0,res['msg'])
        self.assertTrue(res['data']['userNick'])
        self.assertEqual(res['data']['canOrder'],True,res['msg'])
        self.assertEqual(res['data']['countGoods'], True, res['msg'])
        self.assertEqual(res['data']['logged'],True,res['msg'])
        self.assertTrue(res['data']['goodsId'])
        self.assertTrue(res['data']['goodsCode'])
        self.assertTrue(res['data']['sellerId'])
        self.assertEqual(res['data']['isScanned'], True, res['msg'])


        '''--------------------------下单接口----------------------'''
        # 整合数据，调用接口，获取返回结果
        #下单接口
        data['standardOrderdata']['params']['sessionUuid'] = machineCode

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
        data['standardOrderPollingdata']['params']['sessionUuid'] = machineCode

        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=json.dumps(data['standardOrderPollingdata']),
            desc=data['Desc'],
            url=data['GameUrl']
        )
        # channelIds = res['data']['goods'][0]['channelIds'][0]
        # print 'channelIds：'+channelIds
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言
        self.assertEqual(res['data']['model'],True,res['msg'])

        '''--------------------------出货接口----------------------'''
        # 整合数据，调用接口，获取返回结果
        #出货接口
        data['standardShipmentdata']['params']['sessionUuid'] = machineCode
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
    '''--------------------------预登录接口需登录----------------------'''
    # 整合数据，调用接口，获取返回结果
    # 预登录接口

    reslogin = scripts.loadtestInterface(
        instance=HttpWebRequest(),
        instance_pro='post',
        data='{"serviceName": "standardPrepareLogin","version": "1.0.0","params": {"machineCode": "18383061","loginType": 0,"operType":"1","ext": {"isVip": 1,"itemId": "bdaa0181cb9648b680ba6ca4c25d11c2","sessionKey": "61013020f71ce7d140b192f3280c377b81e828b6ec9584c3098056950","goodsCode": ""}}}',
        desc='预登录接口需登录',
        url='http://api.game.36solo.com/inno72/service/open'
    )

    filePath = os.path.join(gl.reportPath, 'gameReportnewlogin.html')  # 确定生成报告的路径
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