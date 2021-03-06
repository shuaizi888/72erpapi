#_*_coding:utf-8_*_
import unittest,os,ddt,json
from interface_project.script import gl
from interface_project.script import HTMLTESTRunnerCN
from interface_project.script import scripts
from interface_project.script.http import HttpWebRequest
@ddt.ddt
class TestActicity(unittest.TestCase):
    """项目管理-活动管理接口"""
    @classmethod
    def setUpClass(cls):
        pass



    #---------------------------------------LOCALE START-------------------------------------------#
    @ddt.data(*(scripts.loadDdtData(filename='activity.yaml',caseflag='ACTIVITY_CASE1')))
    def testlist(self,data):
        '''活动管理接口:查询活动列表#/project/activity/list'''

        #查询活动列表
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['List'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言


    @ddt.data(*(scripts.loadDdtData(filename='activity.yaml',caseflag='ACTIVITY_CASE2')))
    def testgetlist(self,data):
        '''活动管理接口:查询活动列表不分页#/project/activity/getlist'''

        # 查询活动列表不分页
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


    @ddt.data(*(scripts.loadDdtData(filename='activity.yaml',caseflag='ACTIVITY_CASE3')))
    def testadd(self,data):
        '''活动管理接口:新添加活动#/project/activity/add'''
        b = data['Add']['code']
        c = data['Add']['name']
        newcode = b + str(scripts.sjshu())
        newname = c + str(scripts.sjshu())
        data['Add']['code'] = newcode
        data['Add']['name'] = newname
        # 新添加活动
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['Add'],
            desc=data['Desc'],
            url=data['Url']

        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])


    @ddt.data(*(scripts.loadDdtData(filename='activity.yaml',caseflag='ACTIVITY_CASE4')))
    def testdetail(self,data):
        '''活动管理接口:查看活动详细#/project/activity/detail'''

        # 查看活动详细
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['Detail'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])


    @ddt.data(*(scripts.loadDdtData(filename='activity.yaml',caseflag='ACTIVITY_CASE5')))
    def testupdate(self,data):
        '''活动管理接口:更新活动信息#/project/activity/update'''

        # 更新活动信息
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['Updata'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])

    @ddt.data(*(scripts.loadDdtData(filename='activity.yaml',caseflag='ACTIVITY_CASE6')))
    def testdetele(self,data):
        '''活动管理接口:删除活动信息#/project/activity/delete'''

        # 删除活动信息
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['detele'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])

        @classmethod
        def tearDownClass(cls):
            pass

if __name__=="__main__":

    suite = unittest.TestSuite()
    #tests =[TestLocale("testlist"),TestLocale("testgetlist"),TestLocale("testadd"),TestLocale("testdetail"),TestLocale("testupdate"),TestLocale("testdetele")]
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestActicity)]
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