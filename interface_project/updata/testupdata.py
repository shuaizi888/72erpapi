# -*- coding: utf-8 -*-
import requests,json,time
from interface_project.base.basepage import BaseConfig
from Queue import Queue
import time
q = Queue()


def starttime():
    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return times

def endtime():
    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return times

def tokens():
    token = BaseConfig().base_token
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
    }
    headers['lf-None-Matoh'] = token
    return headers
def tokensnew():
    token = BaseConfig().base_token
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
    }
    headers['lf-None-Matoh'] = token
    return headers

def auit_Count(q):
    PASSED_COUNT =0
    FAILED_COUNT =0
    while True:
        if not q.empty():
            v = str(q.get()).split('-')
            if v[0] =='p':
                PASSED_COUNT+=1
            if v[0] =='f':
                FAILED_COUNT+=1
        else:
            q.all_tasks_done
            break
    return PASSED_COUNT,FAILED_COUNT

success_arr = []
failed_arr = []
def updataAPP(Url,machineId,appPackageName,appurl,versionCode):
    data = {"machineId": machineId, "appPackageName": appPackageName, "url": appurl,"versionCode": versionCode}
    res = requests.request('POST', Url, data=data, headers=tokens())

    if res.status_code == 200:
        newres = res.json()
        i = 0
        if newres['code'] ==0:
            print  "升级成功机器编号："+ newmachineId +"   "+appPackageName
            q.put('p-%d'%i)
            success_arr.append(newmachineId)
        else:
            print  "升级失败机器编号："+newmachineId+"   "+appPackageName+ "   "+newres['msg'].encode("utf-8")
            q.put('f-%d' % i)
            failed_arr.append(newmachineId)
    else:
        return {"errcode": 8888, "errmsg": str(res)}

    # print success_arr
    # print failed_arr


def jiepin(Url,machineId,updateStatus):
    data = {"machineId": machineId, "updateStatus": updateStatus}
    res = requests.request('POST', Url, data=data, headers=tokens())
    if res.status_code == 200:
        newres = res.json()
        i = 0
        if newres['code'] ==0:
            print "截屏成功机器编号："+newmachineId
            q.put('p-%d' % i)
        else:
            print "截屏失败机器编号："+newmachineId + "   "+newres['msg'].encode("utf-8")
            q.put('f-%d' % i)
    else:
        return {"errcode": 9001, "errmsg": str(res)}

def cutapp(Url,machineId,cutdata):
    data = {"machineId": machineId, "appPackageName": cutdata}
    res = requests.request('POST', Url, data=data, headers=tokens())
    if res.status_code == 200:
        newres = res.json()
        i = 0

        if newres['code'] ==0:
            print "切换成功机器编号："+newmachineId
            q.put('p-%d' % i)
        else:
            print "切换失败机器编号："+newmachineId + "   "+newres['msg'].encode("utf-8")
            q.put('f-%d' % i)
    else:
        return {"errcode": 9001, "errmsg": str(res)}
def push(Url,machineId):
    a = {"alias": "18047652","machineCode": "18047652","title": "1","text": "1","pushType":1,"msgInfo": {
        "apps": [{
            "url": "http://inno72.oss.72solo.com/apk/prod/prod_monitor.apk",
            "startStatus": 1,
            "appPackageName": "com.inno72.monitorapp",
            "versionCode": 9
        }]
    }
     }
    a['alias'] = machineId
    a['machineCode'] = machineId
    datanew = a
    newdata = json.dumps(datanew)
    res = requests.request('POST',Url,data=newdata,headers= tokensnew())
    if res.status_code == 200:
        newres = res.json()
        i = 0
        if newres['code']==0:
            print "push成功机器编号"+newmachineId
            q.put('p-%d' % i)
        else:
            print "push失败机器编号" +newmachineId + "    "+newres['msg'].encode("utf-8")
    else:
        return {"errcode":9001,"errmsg":str(res)}

if __name__=="__main__":
    Url = BaseConfig().base_url + "/machine/machine/installApp"
    Urljiepin = BaseConfig().base_url + "/machine/machine/updateInfo"
    URLwang = BaseConfig().base_url + "/machine/machine/cutApp"
    URLpush =   "http://api.app.inno72.com/push/pushMsg"
    # machineId = ['1','2','3','0a90693915d945928ae037798f906506']
    # appname = ['com.inno72.app','com.inno72.dc','com.inno72.monitorapp','com.inno72.installer','com.inno72.detection','com.inno72.upload','com.inno72.demons']
    # appurl = ['http://inno72.oss.72solo.com/apk/prod/prod_72app.apk',
    #           'http://inno72.oss.72solo.com/apk/prod/prod_72dc.apk',
    #           'http://inno72.oss.72solo.com/apk/prod/prod_monitor.apk',
    #           'http://inno72.oss.72solo.com/apk/prod/prod_installer.apk',
    #           'http://inno72.oss.72solo.com/apk/prod/prod_detection.apk',
    #           'http://inno72.oss.72solo.com/apk/prod/prod_upload.apk',
    #           'http://inno72.oss.72solo.com/apk/prod/prod_demons.apk']
    # appversion = ['2','3','4','6','3','2','1']

    appname = ['com.inno72.dc']
    appurl = ['http://inno72.oss.72solo.com/apk/prod/prod_72dc.apk']
    appversion = ['6']
    machineId = ['0020f614256d4a0c95619b10805533e8','00b0965295f2427f8f45978d8e345762','00c79c17149f4d8fb372b6d37b084f33','01addff1d6c746b3984f7d40a104d34e','02d844e5c53b456d85228a423ad618b0','03ac00823ddf44c091f3732089b87d37','03eed0cd76434c51ae30dde0e1ec2105','043ea51fafac4d74a39a2dc6b1f527a2','04af5f62d32643bb8b4e03bcc43ba286','04ca279bfe1d418f8d4d3e9fadc6f467','069ded2aea874bedaca564feb5ec37e1','074bb12d76174fdfb883494ea6d40994','076503e9feab4793bdef24b1a2c1ae7d','07720607c5dc4a448d3db1b2a1c118f8','079bd77cfb554fe1a9bb1077ef678a8f','089b5aa5bf394b3f8581ab0041c02052','08a0004a78e74470933fef8afb45ca0a','0934c95a0e9a40dcaa9b4bd4d50fbf6f','0a90693915d945928ae037798f906506','0ad6d41452844e94be40651dd7931daa','0b7dcb1024e346309d15864742884ce1','0c5fcefdcc6749abb433313ea2453690','0ccd6d9c8f344bc69ad404895ee79624','0ccec842bdaf44699e2fc686314b616d','0da85acf48884bbe94c3ae3c95b90aa1','0e8b2fdd695b4ee58988a42af41e7b1a','0f5eec8955cd47348a2ac316c882b3ba','107f6f4e144345c68e1c6688c3067987','1150c6249576495dbf028c37c1f792ed','11a04f8398d9425d8a706e0792841fad','1236e7a1770a447184b0a2cd79824086','12585104286b4689833f48cd895829bf','1414c325c6b04a4f80af26566102bac8','145d4b5f6630404c89e0e313a8925e9c','147c1e462abd49bf852ffbe8fb78a79e','175d79ff275b4df7b9f5d6a123e9029c','17ec0227dbd84010828b50811e673eb5','17ee2d4ea80f440aa54886f8644442f5','1814e4178201478786ea1eece2c6e74b','1835e6a69ff24d7e875563c1f7d6e1ee','184458daeb0845a385fbdfa25255b02a','187e5e3931d34984be26dd06e87d9ceb','195ecfcf2acf472c884a603dc5d8285f','1995e080ae7647e89eb193b82d87addb','1a293daae5924124961a31cb76d2ee58','1ab76733da084fe384d1360a826ec664','1ad5529c4d1d465aa72f3f63d0a96dd7','1c1412cebb42475f909a5d44ab8359ca','1c7fa9c8b57448b895149f9df8cb4947','1ccf837f2536424e8cc8f5417a4a18e7','1ceb1ad2fecf4edea8e043d92073cbd8','1e2bc4d400234101986ea29935f45e56','1e5ab7c0712646ee8556055d7aadcb76','1e7fc249636a4132b4e6970bca3b801f','1fba3a5930154768ac84188872dcd604','20a45fd2674e421c9be8704cf40b3b49','22da3259fc094eefa905475a6a2ec983','232d436b1ff54915b12c922b2f160897','257d5bced896441f9c069003b0b1b405','26501eea09e64c328781daae81e0e5d3','27d0249f3f3344009636bf4e8091b0ba','28b9963785ac4261a2488a266baffc67','29c9943939484ae5baf495765a37715d','2a59b74b27fd46678639be0f7c84798b','2acbb147c60c40e7b7167ea3e6c25221','2b38b98812184dc487202cb07bf968cd','2b53baeef8f64c099e84a0c9bdfeee28','2bfcfe7184f84a5597bbfca9d9781574','2c9d5b9cbe884adf9f480e136c35e0f6','2d749debe8f34c08b963d7958c1e6b30','2f2216acf62b478e9c0e557b5d8965aa','2f343104b0754a5fbe8018bb4aae6d9b','3022486ee3974364a50f1dea465a8580','30d3166368c842cd908db63090f2f816','3108e0f544a44f08a645bed09db9abd3','310c4b37eeb54e54901f59db659c2ebf','3155cb8dd29e4f5fa0e1685e3a8bf3f1','32a7f5edce0f4ae4a44c3dfa36881b1b','32d867f9da1d4bb4b34a7c715d4c52b8','32f23bc4710f4d2da40da38b3a42fe5c','32f2c95378264799be343ae630c973fa','333bb28af017429e90c9e0e467391cb8','33568dd4dc6f4869bba6d16f8faeea75','34e09ec236c04597ae637ca1cef31f7d','350e4c611942429394980b5cbc81e10e','350fe1f053d145888e1f697748cd8447','3649f78a61e14b6aa6b3831ed580d2da','36b7f473d46f4adbbbfd7bf686b6efc0','38d9d32b10f145e48f54b420a1d16b42','397f547f3c0d4b229aa330bb2e3f39fc','3ba175bb7fbd4ced94bdd67391209dcd','3c04976296f74f68a8125f1c3e88dde7','3c40983a2e6b4166b26d436b3caca0c3','3e331afe50084e809d8ade35b403c22a','3e73a995ceb54210a555e32d8a8cd970','404de0491c124c0a8a029a9409f33cf9','406bc9ef4bd84f9e86d5c27895b39123','415389f766e0483a968a82b180eb1061','427288b2b857438c8a11bf8e87eb6029','430eb2e10c0146559141c139fc71b92e','4326094bbd6c49c091a7aab5a3073885','43b58909ba3c416fabb34761ca1add42','44e383f01b4a49828d9ee3024d327619','4506390038364757bffaf4dbd290c755','457d16ea785a42e59ff5f3b3bd8636f7','466b3c1f74244a6cb8e795d86d96142b','46c9cfc77b0d41a5931681eadcd35ed9','47439ceed00049b3a683347f14d9c6df','47efd08e4e444f129faacee4445aba62','483df1600fdb41e6a7d51a0d064a3eaf','485aef6c8cba4b0d8555be83cb8f3676','495fdf6de4544e97b047d92b0fc35f4c','4b189e1207d2424e8fb1201199299d6a','4ba9b3e5c4c34873918122a95e0ca870','4bf4185e87f64f5c95f3345d9a556fa9','4c0714daa2094adc82d1ecaac552f005','4ccb00866bc8447191b7b782b6bcc779','4d0d4cc40ca7445fa6325f9403cae2f6','4dcea24bd3ee42deacc5062b5accfcb9','4dd0cd91b63a473fb8626597acd7d988','4e19d5c2298944b3a9a80470c3129774','4e7f7139454f4bfcab2e9608b1e05eaa','4fb42153bb164cfe9b7f7ebbfc5a4933','504c601732e74ed794a7b35a56bebadc','509ee6f28ff648f5b6d04338cfb06c80','526760482d534d8797341ca20b10f4c8','52a1a658d5e04ae3bc59b96ce4d83d72','5347f639d679444eb6dc416daf7937dc','537ef81ee39646bdb590571b76a1911a','54831dbb7b02454e953959de5f7c8562','54ae96c9977e4b23b331855a9a5547dd','54d3c8283a534b24af61b405e75f2574','55898e58d7c44799b5c2a474b02aafe4','56a0c7a5801f466fb46be0031805995c','57fe55be375c499a8f59d8a0f4efb6a9','582847855589442891dc9b3429662c8e','583b6cc4080b47bea23a5bfa2f3f6317','58645510832b4683bf13285c7a0a1f9e','58770acf49824e72b84574d25d0ce3ee','587953ae5db14af1af6af01183296bda','58bd2b6f71984b6899229d73688efba4','596bf8dbacc8428db54e6a3b09c46f46','59e504ed81994a88af44ad8de24aadca','5bed55488e494814b5fcd4194ba15571','5bf0ef63ae1e42af9c5947f639e4abed','5d46fa28c9494435a12c76f273545f7f','5d80295b4b144fbbb55b15e6d1f22ac0','5e75e34786b747bebd907d5e9f9dd5f1','6042bdbe895e4a88a32862ceaa8491fa','61328a5b61c64398b5da330bfdffcd71','62eebe6bc7794013afa49d11576f9eef','62f1822d5d784a07aff43222f2142f3b','63b6caa2532e4cd1b60b18867e6eaf27','63ba5c481fc34384ad569237f5aace5f','64a139e20a0e4800b74262f2f1fb9453','67fe66fac519465c85fc356b33066385','6805de12e5404db787ccc0621887f705','680db97b1c1b44f8817b174171860fe3','69513aaf8fa54e6db51a2f570d941744','69c6e02a6e1e4e179d449425c78ed7c7','6a02268ed35e4ed7acbe9bb3aefab5f4','6a223467320942e69039f8e0661e772b','6a61e6db11c0438f801a73ba65621b0d','6b4da21d6ecc49848bb5a13460786ade','6c7f22e2cf2444c280a0f1caa0f6e347','6d3e3abbf7df48539cbff32a08c804e1','6edac30cd6e84bbcb50ebd4043dfa7cc','6f0f669e5d3443179dfabc92b7bcdaa7','6f889cac4a7a425b9ad45428e98d6381','70257f1b6d0c42249d43e2b64f0bcf51','702935e0add0446fa9c7e75c67e06b68','717991f012484d72a91ae5c4b40f6442','7256dd93774f4da790a63fd532ea6b8d','72ccf0f4e96045229de5f42263d30697','73903b410ff4473482a672fbb7ba210b','73c8a0502f2c415ebfa6922aa2cb8c32','753b029b1bc3432fbc012283be188966','7595f8f167ed48359c06830854bb66eb','7649a9f7cf04422eb4795da20f6b42e2','76771c3276b54ad0b995853356e35d3f','769ef96913174274a27948cb7d05ded4','76f8095cbfa746c5930d0668e080eb48','771243f7d8a24d729556e814f4aa7c3d','77411d521608470092d58d4c204b5952','77af8da0841d4fe983c6cea8158e6f83','786dc1b97ba54d408d1996259b9a7309','7a9fd3c0606740559e07465123bf1f97','7b238873c0044772bf6abf8bd96f0d52','7b7a52544e744b6dacf6daa923ef043e','7bf52fe37d3548b6b9e0a9905bb26cd3','7c3c1b8b08cf4397940536f8d9d623a4','7c9bccc377dd4eeb8d4d9dd476499dad','7d3a9b46120a4133bf991321f95459be','7d3da08be5664b689ac6387b02534a8a','7d67016072804adda9a1f2954d8a4f96','7dbd0ab412fd4579997ae7f40fd4686a','7fc8f8472815436683e299aec572d359','7fce6031bfb74901ae73e3e4535d8ee7','80c283f5bdc24a0e9f086de7a1985c74','811fec5992164dfcb1043e8b45e5c404','8167386e22b0417ca3aaf86e1fa28f39','81d87a74c4914a7f9fc47677883a2877','81e991cd7c49412682542daa7ede0118','8269ed91e4344553b696833f44b8e776','827b3b38588543d3822672b4abf81799','82a93ff02c9d40a9806a8aedf4ba1221','82f94690179a4cf1ab64f8059b605931','83276eaf363541fbb5677dade64ed2fa','847784c813bb4d80b41d8b9f4b23d3db','84988b61cf1f4140a4ea301271bb768c','851adae8e6e14730913adb06d51c158f','8673acefd936445e8ed032ae72299a15','87406d2af0344a1383c19a8249c060b9','8817f826875a433fb8c4c2316bd1ecdd','88d93c16fed942bb948894f65fc99d95','8982c5c2420e4f3db639c8f7b826a877','898f1c5f53c64e06991a5b508686f181','8aeb131045f34f84829b87fd423fa21c','8b28117232c9450086d00e500871a8b0','8bc327d0a69046979b49a4633e6831c8','8c642dabcf1046f2a03cd0ac22cfa7da','8d1c970ae59e472794b2b2f333fa2164','8d2f0c1a63584dc0a3af2913902ea4d0','8d4b0359caad420fb9687911002e3f90','8df2ac73f7d04175be3a4b69209b461b','8e9e1558a7ee4acab57eee683fdb2380','8f6521ff9b7a44c6b4a255a801987003','8f88dd41d89f4a379187eb7660af19ff','8fa7c4aec8324188ae471404b6aef280','901d089429c74f3abb60add52c81f4f7','90d0849e160540f5ac67605d11f0aa0e','910d04feac8e4d26907d1ba570caeb4f','9181121021d74c4bb2f1cd6d059229b9','92559d39aeb041a695ee741018972664','9269262b30ee4b319728d24f2fda4b15','937f16f5c06c46ee8d8055213adb3281','966d6f5f1e0549ac957cc4ed8c6d7f87','969547f831a54ca2851f7f40cecc8cd0','9832491a7a8c4dc7a8bdc6f66906aa5f','98dc2831feb84a29acc6e8de9aa8d273','98ec1a396b584c61aca8c2d118d23e69','9a3d0628ee4c427081238fdb9e59c692','9a3f5f5edd9a486294645e7d3a22cbc5','9acc653948b04d5b88fbee5f94401acc','9b9376c11361402cb2a2388e6f4bbebb','9be69e280fe34f67add699de452b0f49','9c35b343867e4caaa71f92a6592df0e8','9d7278b80eb542b9b0703e0246ae27cb','9de32b74797c412e9339d13cf5dba04a','9e0fe14534b24345919edb52e2ccd77e','9ef026fdbd4246578a4c13be695b466a','9ef2a60923584770a7e5e310596dc898','9f5e3a50090245cb9bdc69b6ba5b2bdc','9f8f3125e367459e9bc211524b1054c9','a0374598d7e04eddba66dd8b37903707','a0671e0773c342bb81cee6c1f8e8f654','a28f9d0feae6459d8e3cad3025225554','a2afe2b9422849c6a4c482d9fd4c2164','a4fe4cb783524dcf90daee78c29a924d','a6ea0238b7a44245b68863f967657357','a92a2633de8841bc9279b91635daae95','a9a412286f4248b58e6b90922f0d912d','a9ba65373599473eaa1c5ea06d1f8e3d','ab01b72625f541f1a18ac8084ac4033b','ac09c760a0a445f08076eb4b808c957f','ade79211303a4e7d813f94ef8cb2de82','adedbaf2a98b4c128c7cbf2a80fdfaa2','ae280bef2ff744d081efe97e352e6629','ae92331567e742a382f74f1e9cd25d89','af17489e075a46eb98e4bfc378dad8d7','af6dda1478f24148a5df31ab8b234339','b02662fdda674117b2c14a0c3c629990','b04cb335941e48d48a101bd5e3125978','b068959af8da4d8980437577350f39d4','b129252467274452ac0ef0d95b26408b','b17af9105d384f078a8e895f95fb2450','b5afcb8107814508a9197bb9a9153642','b6a97a9f119e4183b598d46e4af63cb2','b6abdeae61544994b615fa64d427a852','b750a8d38bc3475b8f5d6f55f4441d8b','b813e08af4794c49be962a4e0689b234','b9d83031c11d4c13b81cdf4539429fca','be50aaacbac74315a61a007096faf3cc','bec40ca94e4b41d684494c0138e44a68','bf210ac6d1a947b187bf7e5a1cc96ac4','c0835a7126d847338b3e6b3363586703','c08b17626f1d48eab3467e4479eb66eb','c098db5b8e974f559592684e1b2ce5c9','c09c89aa69744558925f32c3c9f072d9','c0a4848766694968a84f8b96af320b4c','c0a70cb059124ac790feb714c8abb96c','c11ef09837cc456da64c96aef0343bcd','c1335647ec224fd998809b34c980fe46','c1fbf386ff4e49979be7b6edf46fa1e4','c20e565e026745bfbe9115ad0e8b7e2e','c2c19ba85a2648e086da96953dcfc084','c312bcfa71e14ac485412778f458509e','c34c7fa4cfef404d8a59833b77790c3c','c3c4b7a39db547dabac20456db59ddbc','c447abf282d643fbb4efb7a86f5b2ed3','c4e921e61a3b43cba35088f535ca71a6','c57fbcd897a04dc58f6e1979ffef0961','c63171214ccd4fc89f64a60c61a98965','c6be3dc8b93e4f20b51c8092767d9cc2','c6f973f4827d4b90b9518a5d89c6315e','c7d35e48bd4840a68addcb3d6eb84f0f','c7fc7734c60243b3b72a66cc3cc74944','c83a4f65f9954040928fae6aff5108f9','c93d25b17d354bdf8d0bf4289c1affef','c9f1077f99b14e7abed7d03382dbe07b','cb00a5304e0547149707daa0c6789d6b','cb249104f29c49e1b6084bda30f072bb','cc324a14a64448f78b9cfdc3701b7d2d','cc46c4db01724520a79a2af135f5fd54','ccb3710004f044428eef187e754b48c3','cde6330143014c2bb9725d57944c4a10','ce04cb2534c147b3ac37f73803444bc1','ce066a56bba9459d9f8490ab994fc0ff','ce2c48a0cb144c43816bc62a758a871f','cffc05022adb48f2944f97a4d0943018','d05471e09cef4b29975649b9691bbc6c','d0aa0c0534bf4410b3716b87de176666','d1b396ce67ab4a7c9e3f6251bfd9fe51','d370b5bc148742ff8f659d071c533f60','d3d0e9e26b5b40ff91cf70de8d8bb4f5','d3ea111fdc6b4cd6bab5b3643a48259a','d4dbcbc83cf245879d9d76536d5b35e8','d57a63de18a342709a6eae407fedcb3c','d61ab04c07d945fda6c6d2cdc26301f2','d6236c8fd8df46fe94a4f3fb86e0dfbd','d69600c6de1f4632bbea7055a06885a4','d79df479610c4ac992a0fe84cbe216a4','d7caab9a2302437fa3738ce6d7e08730','d904dfbfcbfe4366af7942e53029ae2c','d96bf0adc4494af3bd43b8e7013feeeb','d9795c9bf2194bfea1e3d4601b43f615','d9bfc078be2443e8ae165c605d41c511','dc99799dbe67476e9f36a37b18c20181','ddfe0eb244b64927ad004120b2e369f4','de7738461cfe482f88d917bd03f703ff','df38940518d6415ca96152a28161f1a6','df57c8c82fc141c2b4ea2f619bd76691','e25295ac6ca34b7eba1ef6b0a0dc58f7','e2c1f5a9cdec42e8bf3b686a3a7f6c33','e31830ad3f4642459cf2bd038c83f8db','e58e1c4e57e74b7a96b732bd6415785e','e5a62583619e44959da5616b6f93933b','e5b215f460fb4775898666c40ef86e81','e749b258238a464391a9927971799490','e96b6ae6cc3c4503b53f39d705b685f4','e98a296707d3459bb9e7f7f0bd4b11a1','e9a93c3bc09a426c97567a543a0e4c14','e9af58b853bc402ea1e98a09d07e87e4','e9d35c5f4da04ee98c376aa891a24d1b','eaaaa40aba6a43f4a5a680924352a9ee','eb9d4b0fd1224b80a7a65bb7611ea60f','ebc660b67b5f466584c01006ac8ab777','ed6e23e1598043ecb36cc1c209b01686','edd886c0ada94d4b9414ad3997a5558e','edff2a89143a4bfb93700d939af273f3','ee9737e22396430eabbe6aa1fe70bdd4','f07c31f56ac8458b844a65aa6520d8cf','f07c46c1374e46f48f3b78b8a9dcd686','f07eb000df9e43b39159690157f37cda','f0a9041a874243d0b8eb949c338deef8','f1119d95b27e498fa2e61c45b5ec3d85','f1ab2d2b0dc44620b428b915fbd1899b','f1f87544ee2f4933a30cb47a088ec75a','f250702c36a54ce987f8a055897262ac','f27f00b5082b4d15974b3e31d4d9d3de','f4967b2c17584d4a83ea0e4cc88ad5d3','f4b2369e9d5d451aa2fb907146b13f04','f557010710654df8b6ed6344358b0f77','f6b302936c224708b97aad8b919a4970','f7be6208981f48be8a8aac990a590094','f94e82f71de74c07a91e4ba34006a6ad','f966f6cf71384efba0f85969db68d35d','fa39436e33bf462d8cbee23cc20cc966','fa8d73eda1024fa488dadd9608cc1088','fb1464b390a64c24b575b21df99ce44d','fb203d1936b24fa0a1f51f5c5028aa14','fcccea39f031431b968769e26e3000a2','fdd4af0dc9644830ba7f1f0404e7cae4','feaee7af54aa45e288fb2d35838d962b','feb38476a68e412bb1d9cb017e674cb6']
    # for newmachineId in machineId:
        # updataAPP(Url, newmachineId, "com.inno72.monitorapp", "https://inno72.oss.72solo.com/temp/20180824-3/prod_monitor.apk","7")

        # updataAPP(Url, newmachineId, "com.inno72.pingnetwork", "http://inno72.oss.72solo.com/apk/test/test_ping.apk","2")
        # updataAPP(Url, newmachineId, "com.inno72.pingnetwork", "http://inno72.oss.72solo.com/temp/20180825/app-ping.apk","2")
        # updataAPP(Url, newmachineId, "com.inno72.installer","https://inno72.oss.72solo.com/temp/20180824/prod_installer.apk", "3")
        # updataAPP(Url, newmachineId, "com.inno72.detection","http://inno72.oss.72solo.com/apk/prod/prod_detection_1.0.6.apk", "7")
        # time.sleep(2)
        # jiepin(Urljiepin,newmachineId,"3")
        # cutapp(URLwang,newmachineId,"com.tmall.hudong.worldinpot")
        # cutapp(URLwang, newmachineId, "com.inno72.pingnetwork")
        # cutapp(URLwang, newmachineId, "com.inno72.monitorapp")

    # for i in range(1):
    #     th = threading.Thread(target=updataApp, args=(list,))
    #     th.name = 'thread{}'.format(i)
    #     th.start()
    #     th.join()

    a = 0
    b = 0

    for a, b in enumerate(appname):
        starttime()
        newappnew = ('appname{}'.format(b))
        newappurl = ('appurl{}'.format(appurl[a]))
        newappversion = ('appversion{}'.format(appversion[a]))
        for newmachineId in machineId:
            # time.sleep(1)
            updataAPP(Url, newmachineId, b, appurl[a], appversion[a])
            # cutapp(URLwang, newmachineId, "com.inno72.detection")
            # push(URLpush,newmachineId)
            # time.sleep(2)
            # jiepin(Urljiepin, newmachineId, "3")

        time.sleep(2)
        print "---------------------------------------"
        print "---------------------------------------"
        print('升级成功机器编号:{}'.format(success_arr))
        print('升级失败机器编号:{}'.format(failed_arr))

    endtime()
    print "一键升级共：" + str(len(machineId)) +" 台机器"
    p, f = auit_Count(q)
    c = len(appname)
    p1 = p/c
    f1 = f/c
    print '一键升级成功:%d' % p1, '-----', '一键升级失败:%d' % f1