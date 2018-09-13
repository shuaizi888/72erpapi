#_*_coding:utf-8_*_
import unittest,os,ddt,json
from interface_project.script import gl
from interface_project.script import HTMLTESTRunnerCN
from interface_project.script import scripts
from interface_project.script.http import HttpWebRequest
from interface_project.script.https import HttpWebRequests
@ddt.ddt
class TestActicityPlan(unittest.TestCase):
    """项目排期管理-活动排期管理接口"""
    @classmethod
    def setUpClass(cls):
        pass



    #---------------------------------------LOCALE START-------------------------------------------#
    @ddt.data(*(scripts.loadDdtData(filename='activityplan.yaml',caseflag='ACTIVITYPLAN_CASE1')))
    def testlist(self,data):
        '''活动排期管理接口:查询活动排期列表#/project/activityPlan/list'''

        #查询活动排期列表
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['List'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言


    @ddt.data(*(scripts.loadDdtData(filename='activityplan.yaml',caseflag='ACTIVITYPLAN_CASE2')))
    def testgetlist(self,data):
        '''活动排期管理接口:查询活动排期不分页#/project/activityPlan/planMachineDetailList'''

        # 查询活动排期列表不分页
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['GetList'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])
        # self.assertTrue(res['res'],msg='查询列表为空为空res[]')


    @ddt.data(*(scripts.loadDdtData(filename='activityplan.yaml',caseflag='ACTIVITYPLAN_CASE3')))
    def testadd(self,data):
        '''活动排期管理接口:新添加活动排期#/project/activityPlan/add'''
        c = data['Add']['startTimeStr']
        b = data['Add']['endTimeStr']
        newstart = scripts.starttime()
        newend = scripts.endtime()
        data['Add']['startTimeStr'] = newstart
        data['Add']['endTimeStr'] = newend
        # 新添加活动排期
        res = scripts.loadtestInterface(
            instance=HttpWebRequests(),
            instance_pro='post',
            # data = '{"gameId": "8cbd9bad1829454c8672f97ff531385d","userMaxTimes": "100000","goods": [{"resultCode":"1","prizeId": "9a6d230c5e1643caa8ead174f3fe059e","resultRemark": "挑战成功掉货","prizeType": "0"}, {"resultCode":"2","resultRemark": "挑战成功掉货","prizeId": "9a6d230c5e1643caa8ead174f3fe059e","prizeType": "1"}],"activityId": "8c9d37f5481d42d08d0221a4119bc5c2","startTimeStr":"2018-08-16 15:04","endTimeStr":"2018-08-31 15:04","machines": [{"machineCode": "18205961","machineId": "c67742623b7d492a84ea88be206c6708","state": "0"}]}',
            data=json.dumps(data['Add']),
            desc=data['Desc'],
            url=data['Url']

        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])


    @ddt.data(*(scripts.loadDdtData(filename='activityplan.yaml',caseflag='ACTIVITYPLAN_CASE4')))
    def testdetail(self,data):
        '''活动排期管理接口:查看活动排期详细#/project/activityPlan/detail'''

        # 查看活动排期详细
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['Detail'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])


    @ddt.data(*(scripts.loadDdtData(filename='activityplan.yaml',caseflag='ACTIVITYPLAN_CASE5')))
    def testupdate(self,data):
        '''活动排期管理接口:更新活动排期信息#/project/activityPlan/update'''

        # 更新活动排期信息
        res = scripts.loadtestInterface(
            instance=HttpWebRequests(),
            #data = '{"activityId":"8c9d37f5481d42d08d0221a4119bc5c2","activityName":"自动化测试活动08","startTimeStr":"2018-08-10 15:04","endTimeStr":"2018-08-31 15:04","gameId":"8cbd9bad1829454c8672f97ff531385d","userMaxTimes":"10000","dayUserMaxTimes":"10000","goods":[{"key":0,"name":"自动化测试","prizeId":"9a6d230c5e1643caa8ead174f3fe059e","prizeType":"1","resultCode":1,"resultRemark":"挑战成功掉货"},{"key":1,"name":"自动化测试","prizeId":"9a6d230c5e1643caa8ead174f3fe059e","prizeType":"1","resultCode":2,"resultRemark":"挑战成功掉货更新"}],"coupons":[],"machines":[{"machineCode":"18205961","machineId":"c67742623b7d492a84ea88be206c6708","state":0}],"id":"849790f5f8424e5ca0d5e3bf46170b72"}',
            data = json.dumps(data['Updata']),
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])

    @ddt.data(*(scripts.loadDdtData(filename='activityplan.yaml',caseflag='ACTIVITYPLAN_CASE6')))
    def testdetele(self,data):
        '''活动排期管理接口:删除活动排期信息#/project/activityPlan/delete'''

        # 删除活动排期
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['detele'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])

    @ddt.data(*(scripts.loadDdtData(filename='activityplan.yaml', caseflag='ACTIVITYPLAN_CASE7')))
    def testselect(self, data):
        '''活动排期管理接口:选择机器#//project/activityPlan/selectAreaMachines'''

        # 选择机器
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['select'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        # 断言
        self.assertEqual(res['code'], 0, res['msg'])


        @classmethod
        def tearDownClass(cls):
            pass

if __name__=="__main__":

    suite = unittest.TestSuite()
    #tests =[TestLocale("testlist"),TestLocale("testgetlist"),TestLocale("testadd"),TestLocale("testdetail"),TestLocale("testupdate"),TestLocale("testdetele")]
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestActicityPlan)]
    suite.addTests(tests)
    #suite.addTest(TestLocale('testlist'))

    filePath = os.path.join(gl.reportPath, 'Report.html')  # 确定生成报告的路径
    print filePath

    with file(filePath, 'wb') as fp:
        runner = HTMLTESTRunnerCN.HTMLTestRunner(
            stream=fp,
            title=u'点72后台接口自动化测试报告',
            description=u'详细测试用例结果',  # 不传默认为空
            tester=u"sgao"  # 测试人员名字，不传默认为小强
        )
        # 运行测试用例
        runner.run(suite)
        fp.close()