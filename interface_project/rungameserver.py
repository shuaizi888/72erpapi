#coding:utf-8
#Author:sgao

import time
import unittest
from interface_project.script.log import LogDebug
from interface_project.script.HTMLTESTRunnerCN import HTMLTestRunner
from testscenario.gameservers.testgames import TestScenario
from interface_project.script import emailstmp
import os
from interface_project.script import gl
from interface_project.script import emailinno
from interface_project.script import HTMLTESTRunnerCN
from interface_project.script.gamehttp import HttpWebRequestnew
from interface_project.script import scripts
from time import sleep

@property
def create(self):




    Suuidcode = res['data']['qrCodeUrl']
    print "TMURL：" + Suuidcode
    SUuidtoken = res['data']['sessionUuid']
    print "Token：" + SUuidtoken
    SUuidtokenNew = unicode.encode(SUuidtoken)
    # 断言
    self.assertEqual(res['code'], 0, res['msg'])  # 断言

    sleep(30)


if __name__=="__main__":

    res = scripts.loadtestInterface(
        instance=HttpWebRequestnew(),
        instance_pro='post',
        data='{"serviceName":"createQrCode","params":{"machineId":"18335598"},"version":"1.0.0"}',
        desc='生成二维码',
        url='http://api.game.36solo.com/inno72/service/open'
    )

    create
    suite = unittest.TestSuite()
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestScenario)]
    suite.addTests(tests)



    filePath = os.path.join(gl.reportPath, 'Report.html')  # 确定生成报告的路径
    # print filePath

    with file(filePath, 'wb') as fp:
        runner = HTMLTESTRunnerCN.HTMLTestRunner(
            stream=fp,
            title=u'点72游戏服务接口自动化测试报告',
            description=u'详细测试用例结果',  # 不传默认为空
            tester=u"sgao"  # 测试人员名字，不传默认为小强
        )
        # 运行测试用例
        runner.run(suite)
        fp.close()
    LogDebug()
    emailinno.Emailinno().send