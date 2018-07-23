#coding:utf-8
#Author:sgao
import os,sys

global globalPath #global包路径
global configPath #config包路径
global dataPath #Data路径
global dataScenarioPath #场景路径
global tcodePath #t-code路径
global reportPath #报告路径
global configFile
global debugFile

PATH =lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

globalPath = os.path.abspath(os.path.dirname(__file__)) #不可以加\\，否则取上一级会出错
configPath = os.path.join(os.path.dirname(globalPath),'config')
dataPath = os.path.join(PATH(os.path.dirname(globalPath)),'data')
dataScenarioPath = os.path.join(dataPath,'Scenario')
tcodePath = os.path.join(dataPath,'TCode')
reportPath = os.path.join(os.path.dirname(globalPath),'report')
configFile = os.path.join(configPath,'config.yaml')
debugFile = os.path.join(reportPath,'logging.log')

if __name__=="__main__":
    print globalPath
    print configPath
    print dataPath
    print dataScenarioPath
    print tcodePath
    print reportPath
    print configFile
    print debugFile