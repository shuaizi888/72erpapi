#_*_coding:utf-8_*_
import unittest,os,ddt,json
from interface_project.script import gl
from interface_project.script import HTMLTESTRunnerCN
from interface_project.script import scripts
from interface_project.script.http import HttpWebRequest

@ddt.ddt
class TestGoods(unittest.TestCase):
    """项目管理-商品管理接口"""
    @classmethod
    def setUpClass(cls):
        pass



    #---------------------------------------LOCALE START-------------------------------------------#
    @ddt.data(*(scripts.loadDdtData(filename='goods.yaml',caseflag='GOODS_CASE1')))
    def testlist(self,data):
        '''项目管理接口:查询商品列表#/project/goods/list'''

        #查询商品列表
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['List'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言


    @ddt.data(*(scripts.loadDdtData(filename='goods.yaml',caseflag='GOODS_CASE2')))
    def testgetlist(self,data):
        '''项目管理接口:查询商品列表不分页#/project/goods/getlist'''

        # 查询商品列表不分页
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


    @ddt.data(*(scripts.loadDdtData(filename='goods.yaml',caseflag='GOODS_CASE3')))
    def testadd(self,data):
        '''项目管理接口:新添加商品#/project/goods/add'''
        b = data['Add']['code']
        print b
        newcode = b + str(scripts.sjshu())
        print newcode
        data['Add']['code'] = newcode
        # 新添加商品
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['Add'],
            desc=data['Desc'],
            url=data['Url']

        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])


    @ddt.data(*(scripts.loadDdtData(filename='goods.yaml',caseflag='GOODS_CASE4')))
    def testdetail(self,data):
        '''项目管理接口:查看商品详细#/project/goods/detail'''

        # 查看商品详细
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['Detail'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])


    @ddt.data(*(scripts.loadDdtData(filename='goods.yaml',caseflag='GOODS_CASE5')))
    def testupdate(self,data):
        '''项目管理接口:更新商品信息#/project/goods/update'''

        # 更新商品信息
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['Updata'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])

    @ddt.data(*(scripts.loadDdtData(filename='goods.yaml',caseflag='GOODS_CASE6')))
    def testdetele(self,data):
        '''项目管理接口:删除商品信息#/project/goods/delete'''

        # 删除商品信息
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
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestGoods)]
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