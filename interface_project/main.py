#coding:utf-8
#Author:sgao

import time
import unittest
from interface_project.script.log import LogDebug
from interface_project.script.HTMLTESTRunnerCN import HTMLTestRunner
from testInterface.locale import testlocale
from testInterface.channel import testchannel
from testInterface.activity import testactivity
from testInterface.game import testgame
from testInterface.goods import testgoods
from testInterface.merchant import testmerchant
from testInterface.shops import testshops
from testInterface.activityplan import testactivityplan
from testInterface.machine import testmachine
from testInterface.checkerp import testerpcheck
from interface_project.script import emailstmp
from interface_project.script import emailinno
import os
from interface_project.script import gl

def loadTestsList():
    list = [testchannel, testmerchant, testshops, testactivity, testgame, testgoods, testactivityplan,testmachine,testerpcheck]

    tests = [unittest.TestLoader().loadTestsFromModule(testlocale)]
    for module in list:
        tests.append(unittest.TestLoader().loadTestsFromModule(module))
    return tests



if __name__=="__main__":

    suite = unittest.TestSuite()
    suite.addTests(loadTestsList())

    # suite = unittest.TestSuite()
    # # 给套件中添加用例，并且可以指定用例的执行顺序
    # tests = [unittest.TestLoader().loadTestsFromTestCase(TestLocale)]
    # suite.addTests(tests)


    filePath = os.path.join(gl.reportPath, 'Report.html')  # 确定生成报告的路径
    print filePath

    with file(filePath, 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title=u'点72后台接口自动化测试报告',
            description=u'详细测试用例结果',  # 不传默认为空
            tester=u"sgao"  # 测试人员名字，不传默认为小强
        )
        # 运行测试用例
        runner.run(suite)
        fp.close()
    LogDebug()
    emailinno.Emailinno().send