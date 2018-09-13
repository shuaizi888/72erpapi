#_*_coding:utf-8_*_
import unittest,os,ddt,json
from interface_project.script import gl
from interface_project.script import HTMLTESTRunnerCN
from interface_project.script import scripts
from interface_project.script.http import HttpWebRequest
from interface_project.script.https import HttpWebRequests
from interface_project.script.httpss import HttpWebRequestss
from interface_project.script import encrypt
from interface_project.script import decrypt
@ddt.ddt
class TestMachine(unittest.TestCase):
    """机器后台-管理接口"""
    @classmethod
    def setUpClass(cls):
        pass


    @ddt.data(*(scripts.loadDdtData(filename='machine.yaml',caseflag='MACHINE_CASE1')))
    def testint(self,data):
        '''机器后台管理接口:初始化机器#/machine/initMachine'''
        intdata = json.dumps(data['int'])
        intnew = encrypt.jiami(intdata)

        #初始化机器
        res = scripts.loadtestInterface(
            instance=HttpWebRequestss(),
            data=intnew,
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        # print res
        res2 = json.loads(decrypt.jiemi(res))
        self.assertEqual(res2['code'],0)#断言


    @ddt.data(*(scripts.loadDdtData(filename='machine.yaml',caseflag='MACHINE_CASE2')))
    def testgetid(self,data):
        '''机器后台管理接口:获取机器ID#/machine/generateMachineId'''
        getiddata = json.dumps(data['getid'])
        getidnew = encrypt.jiami(getiddata)
        # 获取机器ID
        res = scripts.loadtestInterface(
            instance=HttpWebRequestss(),
            data=getidnew,
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        #断言
        res2 = json.loads(decrypt.jiemi(res))
        self.assertEqual(res2['code'],0)#断言


    @ddt.data(*(scripts.loadDdtData(filename='machine.yaml',caseflag='MACHINE_CASE3')))
    def testgetstatus(self,data):
        '''机器后台管理接口:获取机器状态#/machine/getMachineStatus'''
        getstatusdata = json.dumps(data['getstatus'])
        getstatusnew = encrypt.jiami(getstatusdata)
        # 获取机器状态
        res = scripts.loadtestInterface(
            instance=HttpWebRequestss(),
            instance_pro='post',
            data=getstatusnew,
            desc=data['Desc'],
            url=data['Url']

        )
        res2 = json.loads(decrypt.jiemi(res))
        self.assertEqual(res2['code'],0)#断言


    @ddt.data(*(scripts.loadDdtData(filename='machine.yaml',caseflag='MACHINE_CASE4')))
    def testupstatus(self,data):
        '''机器后台管理接口:更改机器状态#/machine/updateMachineStatus'''
        upstatusdata = json.dumps(data['upstatus'])
        upstatusnew = encrypt.jiami(upstatusdata)
        # 更改机器状态
        res = scripts.loadtestInterface(
            instance=HttpWebRequestss(),
            data=upstatusnew,
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        res2 = json.loads(decrypt.jiemi(res))
        self.assertEqual(res2['code'],0)#断言


    @ddt.data(*(scripts.loadDdtData(filename='machine.yaml',caseflag='MACHINE_CASE5')))
    def testgetlocale(self,data):
        '''机器后台管理接口:获取机器点位#/machine/getMachineLocale'''
        getlocaledata = json.dumps(data['getlocale'])
        getloaclenew = encrypt.jiami(getlocaledata)
        # 获取机器点位
        res = scripts.loadtestInterface(
            instance=HttpWebRequestss(),
            data = getloaclenew,
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )

        res2 = json.loads(decrypt.jiemi(res))
        self.assertEqual(res2['code'],0)#断言

    @ddt.data(*(scripts.loadDdtData(filename='machine.yaml',caseflag='MACHINE_CASE6')))
    def testgetapp(self,data):
        '''机器后台管理接口:获取机器上app#/app/getAppByBlong'''
        getappdata = json.dumps(data['getapp'])
        getappnew = encrypt.jiami(getappdata)
        # 获取机器上app
        res = scripts.loadtestInterface(
            instance=HttpWebRequestss(),
            data=getappnew,
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )

        res2 = json.loads(decrypt.jiemi(res))
        self.assertEqual(res2['code'],0)#断言

    @ddt.data(*(scripts.loadDdtData(filename='machine.yaml', caseflag='MACHINE_CASE7')))
    def testsetchannel(self, data):
        '''机器后台管理接口:合并拆分货道#//machine/setMachineChannel'''
        setchanneldata = json.dumps(data['setchannel'])
        setchannelnew = encrypt.jiami(setchanneldata)
        # 合并拆分货道
        res = scripts.loadtestInterface(
            instance=HttpWebRequestss(),
            data=setchannelnew,
            desc=data['Desc'],
            url=data['Url'],
            instance_pro='post'
        )
        res2 = json.loads(decrypt.jiemi(res))
        self.assertEqual(res2['code'],0)#断言


        @classmethod
        def tearDownClass(cls):
            pass

if __name__=="__main__":

    suite = unittest.TestSuite()
    #tests =[TestLocale("testlist"),TestLocale("testgetlist"),TestLocale("testadd"),TestLocale("testdetail"),TestLocale("testupdate"),TestLocale("testdetele")]
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestMachine)]
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