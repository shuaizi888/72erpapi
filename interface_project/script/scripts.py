#_*_coding:utf-8_*_
from log import LogDebug
import time,os
import yaml,json
from interface_project.script import gl
from requests.exceptions import ConnectTimeout,ConnectionError,Timeout,HTTPError


'''
#日期时间串
'''
def rndTimeStr():
    """
    随机字符串
    :return: 日期时间
    """
    time.sleep(1)
    curTimeStr = str(time.strftime('%Y%m%d%H%M%S', time.localtime()).encode('utf-8'))
    #LogDebug().info('生成日期时间串%s'%curTimeStr)
    return curTimeStr.decode('utf-8')

@property
def timeStamp():
    """
    秒级时间戳
    :return: 时间戳
    """
    return int(time.time())

'''
写yaml内容
'''
def writeYmal(yamlPath,data):
    """
    写yaml文件
    :param yamlPath: yaml文件路径
    :param data: 数据内容
    :return: 无
    """
    with open(yamlPath,'wb') as fp:
        yaml.dump(data,fp)
        fp.close()



'''
读yaml文件
'''
def getYamlfield(yamlpath):
    """
    获取yaml配置内容
    :param yamlpath: yaml文件路径
    :return: 返回字典所有内容
    """
    with open(yamlpath,'rb') as fp:
        cont = fp.read()
        fp.close()
    ret = yaml.load(cont)
    return ret



#raw multipart form-data #格式不可动
def MultipartFormData(data,appid ='dp1svA1gkNt8cQMkoIv7HmD1',sig=1,ts=1):
    """
    按特定格式生成接口测试数据
    :param data: 主体数据
    :param appid: 特殊数据
    :param sig: 特殊数据
    :param ts: 特殊数据
    :return: 生成的完整数据
    """
    data = json.dumps(data).decode('unicode-escape')
    LogDebug().info('------------------START----------------')
    LogDebug().info('请求数据:{0}'.format(data))
    LogDebug().info('请求Appid:{0}'.format(appid))
    payload = '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"req\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"appid\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ts\"\r\n\r\n%d\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"sig\"\r\n\r\n%d\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"v\"\r\n\r\n2.0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--' % (data,appid,ts,sig)

    return payload


#获取配置文件中,运行标记
def getRunFlag(scenarioKey):
    """
    获取配置文件中执行标记
    :param scenarioKey: 场景字段
    :return: 标记值;Y or N
    """
    yamldict = getYamlfield(os.path.join(gl.configPath,'config.yaml'))
    flagRet = yamldict['RUNING'][scenarioKey]['Flag']
    LogDebug().info('{0}执行标记:{1}'.format(scenarioKey,flagRet))
    return flagRet


def loadDdtData(Itype='t', filename='Charge.yaml', caseflag='CHARGE_CASE1'):
    """
    从yaml加载ddt数据
    :param Itype: t:tcode; s:scenario
    :param filename: 'Charge.yaml'
    :param caseflag:  yaml中接口case的起始节点
    :return: ddt数据list
    """
    ddtData = []
    if Itype == 't':
        configDir = gl.tcodePath
    else:
        configDir = gl.dataScenarioPath

    yamfpath = os.path.join(configDir, filename)
    readYam = getYamlfield(yamfpath)

    dictCase = readYam[caseflag]
    for key in dictCase:
        ddtData.append(dictCase[key])

    return ddtData

'''
def loadtestInterface(instance, data_node, desc='Desc'):
    """
    加载测试接口
    :param instance: 接口类实例
    :param data_node: yaml中的data节点名
    :param appid: Appid的值
    :param desc: case描述
    :return:
    """
    OUT_TMPL = """用例描述-->{0}\r\n发送:\r\n{1}\r\nAppid:{2}\r\n返回:\r\n{3}"""

    # 储值记录详情
    view = instance
    data_node = str(data_node)

    # 获取case数据
    view.payload = MultipartFormData(eval(data_node))
    viewResult = instance.post()

    print OUT_TMPL.format(
        desc, data_node, json.dumps(viewResult).decode('unicode-escape'))

    return viewResult
'''

def loadtestInterface(**kwargs):
    """
    整理测试数据  加载测试接口
    :param kwargs: 接口相关数据
    instance=类实例
    instance_pro=接口方法属性
    url=接口相对url
    data=接口数据字典
    desc=接口描述
    :return: 接口返回结果
    """
    OUT_TMPL = """用例描述-->{0}\r\n发送:{4}\r\n{1}\r\n返回:\r\n{3}"""

    #实例
    view = kwargs['instance']
    view.url = kwargs['url']
    view.data = kwargs['data']

    # 获取case数据
    #view.payload = MultipartFormData(eval(data_node))
    view.payload = eval(kwargs['data'])

    #调用接口,需注意的是，aetatt，接口函数，必须@property装饰成属性
    viewResult = getattr(view, kwargs['instance_pro'])

    """报告输出，格式模版"""
    print OUT_TMPL.format(
        kwargs['desc'],
        kwargs['data'],
        json.dumps(viewResult).decode('unicode-escape'),
        kwargs['url']
    )

    return viewResult


def retry(**kw):
    """
    装饰器：http请求，出错重试功能
    :param arg: ()元组，异常类
    :param kw: reNum = n；n为重试次数
    :return: 函数本身
    """
    def wrapper(func):
        def _wrapper(*args,**kwargs):
            raise_ex = None
            for n in range(kw['reNum']):
                try:
                    return func(*args,**kwargs)
                except (ConnectTimeout,ConnectionError,Timeout,HTTPError) as ex:
                    raise_ex = ex
                LogDebug().warning('重新发送请求:第{0}次'.format(n))
            #raise raise_ex
        return _wrapper
    return wrapper



def rmDirsAndFiles(dirpath):
    """
    删除目标,目录下文件及文件夹
    :param dirpath: 目标目录
    :return: 无
    """
    listdir = os.listdir(dirpath)
    if listdir:
        for f in listdir:
            filepath = os.path.join(dirpath,f)
            if os.path.isfile(filepath):
                os.remove(filepath)
            if os.path.isdir(filepath):
                os.rmdir(filepath)





if __name__=="__main__":
    print json.dumps(getRunFlag('testCouponSendAndCancel')).decode('unicode-escape')

