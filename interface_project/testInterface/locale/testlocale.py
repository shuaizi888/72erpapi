#_*_coding:utf-8_*_
import unittest,os,ddt,json
from interface_project.script import gl
from interface_project.script import HTMLTESTRunnerCN
from interface_project.interface.locale import locale_add,locale_list,locale_delete,locale_detail,locale_getList,locale_update
from interface_project.script import scripts
from interface_project.script.http import HttpWebRequest

@ddt.ddt
class TestLocale(unittest.TestCase):
    """货机管理-点位管理接口"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass



    #---------------------------------------LOCALE START-------------------------------------------#
    @ddt.data(*(scripts.loadDdtData(filename='locale.yaml',caseflag='LOCALE_CASE1')))
    def testlist(self,data):
        '''点位管理接口:查询点位列表#/machine/locale/list'''

        #查询点位列表
        # TList = locale_list.LocaleClass()
        #
        # res = scripts.loadtestInterface(
        #     TList, 'localeList', data['List'], desc=data['Desc'])
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['List'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言
        # self.assertTrue(res['res'],msg='查询列表为空res[]')


    # @ddt.data(*(scripts.loadDdtData(filename='locale.yaml',caseflag='LOCALE_CASE2')))
    # def testgetlist(self,data):
    #     '''点位管理接口:查询点位列表不分页#/machine/locale/getlist'''
    #
    #     # 查询点位列表不分页
    #     TGetList = locale_getList.LocaleClass()
    #
    #     res = scripts.loadtestInterface(
    #         TGetList, 'localeGetList', data['GetList'], desc=data['Desc'])
    #     #断言
    #     self.assertEqual(res['code'],0,res['msg'])
    #     # self.assertTrue(res['res'],msg='查询列表为空为空res[]')
    #
    #
    # @ddt.data(*(scripts.loadDdtData(filename='locale.yaml',caseflag='LOCALE_CASE3')))
    # def testadd(self,data):
    #     '''点位管理接口:新添加点位#/machine/locale/add'''
    #
    #     # 新添加点位
    #     TAdd = locale_add.LocaleClass()
    #
    #     res = scripts.loadtestInterface(
    #         TAdd, 'localeAdd', data['Add'], desc=data['Desc'])
    #     #断言
    #     self.assertEqual(res['code'],0,res['msg'])
    #
    #
    # @ddt.data(*(scripts.loadDdtData(filename='locale.yaml',caseflag='LOCALE_CASE4')))
    # def testdetail(self,data):
    #     '''点位管理接口:查看点位详细#/machine/locale/detail'''
    #
    #     # 新添加点位
    #     TDETAIL = locale_detail.LocaleClass()
    #
    #     res = scripts.loadtestInterface(
    #         TDETAIL, 'localeDetail', data['Detail'], desc=data['Desc'])
    #     #断言
    #     self.assertEqual(res['code'],0,res['msg'])
    #
    #
    # @ddt.data(*(scripts.loadDdtData(filename='locale.yaml',caseflag='LOCALE_CASE5')))
    # def testupdate(self,data):
    #     '''点位管理接口:更新点位信息#/machine/locale/update'''
    #
    #     # 新添加点位
    #     TUPDATA = locale_update.LocaleClass()
    #
    #     res = scripts.loadtestInterface(
    #         TUPDATA, 'localeUpdata', data['Updata'], desc=data['Desc'])
    #     #断言
    #     self.assertEqual(res['code'],0,res['msg'])


if __name__=="__main__":

    suite = unittest.TestSuite(TestLocale)
    #tests = [unittest.TestLoader().loadTestsFromTestCase(TestLocale)]
    #suite.addTests(tests)

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