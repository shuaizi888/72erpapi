#coding:utf-8
#Author:sgao
from interface_project.script import gl
from interface_project.script import scripts
import os

class BaseConfig(object):

    def __init__(self):
        self.yamlConfigPath = os.path.join(gl.configPath, 'config.yaml')

    @property
    def base_url(self):
        confData = scripts.getYamlfield(self.yamlConfigPath)
        return confData['BASE_URL']

    @property
    def base_token(self):
        confData = scripts.getYamlfield(self.yamlConfigPath)
        return confData['BASE_TOKEAN']


if __name__=="__main__":
    print BaseConfig().base_url
    print BaseConfig().base_token