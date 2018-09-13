#coding:utf-8
#Author:sgao
from interface_project.script import gl
from interface_project.script import scripts
import os
from interface_project.interface.login import loginClass

class BaseConfig(object):

    def __init__(self):
        self.yamlConfigPath = os.path.join(gl.configPath, 'config.yaml')

    @property
    def base_url(self):
        confData = scripts.getYamlfield(self.yamlConfigPath)
        return confData['BASE_URL']

    @property
    def app_url(self):
        confData = scripts.getYamlfield(self.yamlConfigPath)
        return confData['APP_URL']

    @property
    def check_url(self):
        confData = scripts.getYamlfield(self.yamlConfigPath)
        return confData['CHECK_URL']

    @property
    def base_token(self):
        #获取登录后的token值
        ltoken = loginClass().login
        ltokennew = unicode.encode(ltoken)
        return ltokennew
        #通过yaml使用变量读取出来
        # confData = scripts.getYamlfield(self.yamlConfigPath)
        # ytoken = confData['BASE_TOKEAN']
        # return  ytoken
        # # return ytoken
        # toknes = scripts.readVar(ytoken)
        # return toknes


if __name__=="__main__":
    print BaseConfig().base_url
    print BaseConfig().base_token
    print BaseConfig().app_url