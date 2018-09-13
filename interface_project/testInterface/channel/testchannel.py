#_*_coding:utf-8_*_
import unittest,os,ddt,json
from interface_project.script import gl
from interface_project.script import HTMLTESTRunnerCN
from interface_project.script import scripts
from interface_project.script.http import HttpWebRequest

@ddt.ddt
class TestChannel(unittest.TestCase):
    """项目管理-渠道管理接口"""
    @classmethod
    def setUpClass(cls):
        pass



    #---------------------------------------LOCALE START-------------------------------------------#
    @ddt.data(*(scripts.loadDdtData(filename='channel.yaml',caseflag='CHANNEL_CASE1')))
    def testlist(self,data):
        '''渠道管理接口:查询渠道列表#/project/channel/list'''

        #查询渠道列表
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['List'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言


    @ddt.data(*(scripts.loadDdtData(filename='channel.yaml',caseflag='CHANNEL_CASE2')))
    def testgetlist(self,data):
        '''渠道管理接口:查询渠道列表不分页#/project/channel/getlist'''

        # 查询渠道列表不分页
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


    @ddt.data(*(scripts.loadDdtData(filename='channel.yaml',caseflag='CHANNEL_CASE3')))
    def testadd(self,data):
        '''渠道管理接口:新添加渠道#/project/channel/add'''
        b = data['Add']['channelCode']
        print b
        newcode = b + str(scripts.sjshu())
        print newcode
        data['Add']['channelCode'] = newcode



        # 新添加渠道
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['Add'],
            desc=data['Desc'],
            url=data['Url']

        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])



    @ddt.data(*(scripts.loadDdtData(filename='channel.yaml',caseflag='CHANNEL_CASE4')))
    def testupdate(self,data):
        '''渠道管理接口:更新渠道信息#/project/channel/update'''

        # 更新渠道信息
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['Updata'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])

    @ddt.data(*(scripts.loadDdtData(filename='channel.yaml',caseflag='CHANNEL_CASE5')))
    def testdetele(self,data):
        '''渠道管理接口:删除渠道信息#/project/channel/delete'''

        # 删除渠道
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
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestChannel)]
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