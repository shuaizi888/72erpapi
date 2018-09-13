#_*_coding:utf-8_*_
import unittest,os,ddt,json
from interface_project.script import gl
from interface_project.script import HTMLTESTRunnerCN
from interface_project.script import scripts
from interface_project.script.http import HttpWebRequest

@ddt.ddt
class TestShops(unittest.TestCase):
    """项目管理-店铺管理接口"""
    @classmethod
    def setUpClass(cls):
        pass



    #---------------------------------------LOCALE START-------------------------------------------#
    @ddt.data(*(scripts.loadDdtData(filename='shops.yaml',caseflag='SHOPS_CASE1')))
    def testlist(self,data):
        '''项目管理接口:查询店铺列表#/project/shops/list'''

        #查询店铺列表
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['List'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言


    @ddt.data(*(scripts.loadDdtData(filename='shops.yaml',caseflag='SHOPS_CASE2')))
    def testgetlist(self,data):
        '''项目管理接口:查询店铺列表不分页#/project/shops/getlist'''

        # 查询店铺列表不分页
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


    @ddt.data(*(scripts.loadDdtData(filename='shops.yaml',caseflag='SHOPS_CASE3')))
    def testadd(self,data):
        '''店铺管理接口:新添加店铺#/project/shops/add'''
        b = data['Add']['shopCode']
        print b
        newcode = b + str(scripts.sjshu())
        print newcode
        data['Add']['shopCode'] = newcode
        # 新添加店铺
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['Add'],
            desc=data['Desc'],
            url=data['Url']

        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])


    @ddt.data(*(scripts.loadDdtData(filename='shops.yaml',caseflag='SHOPS_CASE4')))
    def testdetail(self,data):
        '''店铺管理接口:查看店铺#/project/shops/detail'''

        # 查看店铺详细
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['Detail'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])


    @ddt.data(*(scripts.loadDdtData(filename='shops.yaml',caseflag='SHOPS_CASE5')))
    def testupdate(self,data):
        '''店铺管理接口:更新店铺信息#/project/shops/update'''

        # 更新店铺信息
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['Updata'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])

    @ddt.data(*(scripts.loadDdtData(filename='shops.yaml',caseflag='SHOPS_CASE6')))
    def testdetele(self,data):
        '''店铺管理接口:删除店铺信息#/project/shops/delete'''

        # 删除店铺
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
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestShops)]
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