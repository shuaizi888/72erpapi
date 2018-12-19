#_*_coding:utf-8_*_
import unittest,os,ddt,json
from interface_project.script import gl
from interface_project.script import HTMLTESTRunnerCN
from interface_project.script import scripts
from interface_project.script.http import HttpWebRequest
from interface_project.script.https import HttpWebRequests
@ddt.ddt
class TestERPCheck(unittest.TestCase):
    """后台巡检管理-巡检管理接口"""
    @classmethod
    def setUpClass(cls):
        pass



    #---------------------------------------ERPCHECK START-------------------------------------------#
    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml',caseflag='ERPCHECK_CASE1')))
    def testlist(self,data):
        '''后台巡检管理:  人员列表/check/user/list'''

        #巡检管理 人员列表
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['list'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言


    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml',caseflag='ERPCHECK_CASE2')))
    def testgetmachine(self,data):
        '''后台巡检管理:  查看机器/check/user/getUserMachinDetailList'''

        #巡检管理 人员列表
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['getmachine'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言


    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml',caseflag='ERPCHECK_CASE3')))
    def testadd(self,data):
        '''后台巡检管理:  添加人员#/check/user/add'''
        b = data['add']['cardNo']
        c = data['add']['phone']
        d = data['add']['name']
        newcode = b + str(scripts.sjshu())
        newphone = c + str(scripts.sjshu())
        newname = d + str(scripts.sjshu())
        # print newcode
        # print newphone
        # print newname
        data['add']['cardNo'] = newcode
        data['add']['phone'] = newphone
        data['add']['name'] = newname
        # 新添加商品
        res = scripts.loadtestInterface(
            instance=HttpWebRequests(),
            instance_pro='post',
            data=json.dumps(data['add']),
            desc=data['Desc'],
            url=data['Url']

        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])


    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml',caseflag='ERPCHECK_CASE4')))
    def testdetail(self,data):
        '''后台巡检管理:  查看人员详情/check/user/detail'''

        #巡检管理 查看人员详情
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['detail'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言


    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml',caseflag='ERPCHECK_CASE5')))
    def testupdata(self,data):
        '''后台巡检管理:  更新人员#/check/user/update'''
        b = data['updata']['cardNo']
        c = data['updata']['phone']
        d = data['updata']['name']
        newcode = b + str(scripts.sjshu())
        newphone = c + str(scripts.sjshu())
        newname = d + str(scripts.sjshu())
        print newcode
        print newphone
        print newname
        data['updata']['cardNo'] = newcode
        data['updata']['phone'] = newphone
        data['updata']['name'] = newname
        # 更新人员
        res = scripts.loadtestInterface(
            instance=HttpWebRequests(),
            instance_pro='post',
            data=json.dumps(data['updata']),
            desc=data['Desc'],
            url=data['Url']

        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])

    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml',caseflag='ERPCHECK_CASE6')))
    def testupdatastatus(self,data):
        '''后台巡检管理:  更新人员状态/check/user/updateStatus'''

        #巡检管理 查看人员详情
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['updatastatus'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        self.assertEqual(res['code'],0,res['msg'])#断言

    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml', caseflag='ERPCHECK_CASE7')))
    def testselectmachines(self, data):
        '''后台巡检管理:  选择机器/check/user/selectmachines'''

        # 巡检管理 选择机器
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['selectmachines'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        # 断言
        self.assertEqual(res['code'], 0, res['msg'])  # 断言

    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml', caseflag='ERPCHECK_CASE8')))
    def testdelete(self, data):
        '''后台巡检管理:  人员删除/check/user/delete'''

        # 巡检管理 人员删除
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['delete'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        # 断言
        self.assertEqual(res['code'], 0, res['msg'])  # 断言

    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml', caseflag='ERPCHECK_CASE9')))
    def testlistyuser(self, data):
        '''后台巡检管理:  故障类型列表/check/user/listyuser'''

        # 巡检管理 故障类型列表
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['listyuser'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        # 断言
        self.assertEqual(res['code'], 0, res['msg'])  # 断言

    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml', caseflag='ERPCHECK_CASE10')))
    def testaddfault(self, data):
        '''后台巡检管理:  新增类型/check/user/add'''
        b = data['addfault']['name']
        newcode = b + str(scripts.sjshu())
        print newcode
        data['addfault']['name'] = newcode
        # 巡检管理 新增类型
        res = scripts.loadtestInterface(
            instance=HttpWebRequests(),
            data=json.dumps(data['addfault']),
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        # 断言
        self.assertEqual(res['code'], 0, res['msg'])  # 断言

    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml', caseflag='ERPCHECK_CASE11')))
    def testlistfault(self, data):
        '''后台巡检管理:  故障类型列表/check/user/listfault'''

        # 巡检管理 故障类型列表
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['listfault'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        # 断言
        self.assertEqual(res['code'], 0, res['msg'])  # 断言

    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml', caseflag='ERPCHECK_CASE12')))
    def testdetailfault(self, data):
        '''后台巡检管理:  编辑页详情/check/faultType/detailfault'''

        # 巡检管理 编辑页详情
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['detailfault'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        # 断言
        self.assertEqual(res['code'], 0, res['msg'])  # 断言

    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml', caseflag='ERPCHECK_CASE13')))
    def testudpatafault(self, data):
        '''后台巡检管理:  更新类型/check/faultType/udpatafault'''
        b = data['udpatafault']['name']
        newcode = b + str(scripts.sjshu())
        data['udpatafault']['name'] = newcode
        # 巡检管理 更新类型
        res = scripts.loadtestInterface(
            instance=HttpWebRequests(),
            data=json.dumps(data['udpatafault']),
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        # 断言
        self.assertEqual(res['code'], 0, res['msg'])  # 断言

    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml', caseflag='ERPCHECK_CASE14')))
    def testsave(self, data):
        '''后台巡检管理:  新增工单/check/fault/save'''
        b = data['save']['remark']
        newcode = b + str(scripts.sjshu())
        data['save']['remark'] = newcode
        # 巡检管理 更新类型
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['save'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        # 断言
        self.assertEqual(res['code'], 0, res['msg'])  # 断言

    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml', caseflag='ERPCHECK_CASE15')))
    def testerplist(self, data):
        '''后台巡检管理:  工单列表接口/check/fault/erplist'''
        # 巡检管理 工单列表接口
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['erplist'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        # 断言
        self.assertEqual(res['code'], 0, res['msg'])  # 断言

    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml', caseflag='ERPCHECK_CASE16')))
    def testerpdetail(self, data):
        '''后台巡检管理:  工单详情/check/fault/erpdetail'''
        # 巡检管理 工单详情
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['erpdetail'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        # 断言
        self.assertEqual(res['code'], 0, res['msg'])  # 断言

    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml', caseflag='ERPCHECK_CASE17')))
    def testerpupdata(self, data):
        '''后台巡检管理:  工单状态操作/check/fault/erplist'''
        # 巡检管理 工单状态操作
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['erpupdata'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        # 断言
        self.assertEqual(res['code'], 0, res['msg'])  # 断言

    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml', caseflag='ERPCHECK_CASE18')))
    def testerpanswer(self, data):
        '''后台巡检管理:  工单列表接口/check/fault/erpanswer'''
        # 巡检管理 工单列表接口
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['erpanswer'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        # 断言
        self.assertEqual(res['code'], 0, res['msg'])  # 断言

    @ddt.data(*(scripts.loadDdtData(filename='erpcheck.yaml', caseflag='ERPCHECK_CASE19')))
    def testerpuserlist(self, data):
        '''后台巡检管理:  工单指派人员列表/check/fault/erpuserlist'''
        # 巡检管理 工单指派人员列表
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            data=data['erpuserlist'],
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        # 断言
        self.assertEqual(res['code'], 0, res['msg'])  # 断言

    @classmethod
    def tearDownClass(cls):
        pass

if __name__=="__main__":

    suite = unittest.TestSuite()
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestERPCheck)]
    suite.addTests(tests)

    filePath = os.path.join(gl.reportPath, 'Report.html')  # 确定生成报告的路径
    # print filePath

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