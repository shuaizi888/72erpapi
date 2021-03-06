#coding:utf-8
#Author:sgao


import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.header import Header
from interface_project.script import gl
import time
import yaml,os,base64
from email import encoders
from interface_project.script import scripts



class Emailinno(object):


    @property
    def send(self):
        self.curDateTime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        print self.curDateTime
        self.config = scripts.getYamlfield(os.path.join(gl.configPath, 'config.yaml'))
        # 发件人地址，通过控制台创建的发件人地址
        self.username = self.config['EMAIL']['Smtp_Sender']
        # 发件人密码，通过控制台创建的发件人密码
        self.password = self.config['EMAIL']['Password']
        # 自定义的回复地址
        self.replyto = '***'
        # 收件人地址或是地址列表，支持多个收件人，最多30个
        # rcptto = ['***', '***']
        list = self.config['EMAIL']['Receivers']
        self.rcptto =', '.join(list)
        self.msg_title = self.config['EMAIL']['Msg_Title']
        # 构建alternative结构
        msg = MIMEMultipart('alternative')
        # msg['Subject'] = Header('点72接口自动化测试'.decode('utf-8')).encode()
        msg['Subject'] = Header('%s%s' % (self.msg_title, self.curDateTime), 'utf-8')
        msg['From'] = '%s <%s>' % (Header('接口自动化测试'.decode('utf-8')).encode(), self.username)
        msg['To'] = self.rcptto
        msg['Reply-to'] = self.replyto
        msg['Message-id'] = email.utils.make_msgid()
        msg['Date'] = email.utils.formatdate()
        # 构建alternative的text/plain部分
        textplain = MIMEText('自动化测试文本', _subtype='plain', _charset='UTF-8')
        msg.attach(textplain)
        # 构建alternative的text/html部分
        # texthtml = MIMEText('本次自动化测试结果，详情请见附件！', _subtype='html', _charset='UTF-8')
        # msg.attach(texthtml)

        reportfile = os.path.join(gl.reportPath, 'Report.html')
        # 增加邮件内容为html
        fp = open(reportfile, 'rb')
        reportHtmlText = fp.read()
        msg.attach(MIMEText(reportHtmlText, 'html', 'utf-8'))
        fp.close()

        ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        # 增加后台接口附件
        file = MIMEBase(maintype, subtype)
        file.set_payload(reportHtmlText)
        file.add_header('Content-Disposition', 'attachment', filename='Report.html')
        encoders.encode_base64(file)
        msg.attach(file)
        #增加游戏报告附件
        filegame = MIMEBase(maintype, subtype)
        filegame.set_payload(reportHtmlText)
        filegame.add_header('Content-Disposition', 'attachment', filename='gameReport.html')
        encoders.encode_base64(filegame)
        msg.attach(filegame)

        # 发送邮件
        try:
            client = smtplib.SMTP()
            # python 2.7以上版本，若需要使用SSL，可以这样创建client
            # client = smtplib.SMTP_SSL()
            # SMTP普通端口为25或80
            client.connect('smtpdm.aliyun.com', 25)
            # 开启DEBUG模式
            client.set_debuglevel(0)
            client.login(self.username, self.password)
            # 发件人和认证地址必须一致
            # 备注：若想取到DATA命令返回值,可参考smtplib的sendmaili封装方法:
            #      使用SMTP.mail/SMTP.rcpt/SMTP.data方法
            client.sendmail(self.username, self.rcptto, msg.as_string())
            client.quit()
            print '邮件发送成功！'
        except smtplib.SMTPConnectError, e:
            print '邮件发送失败，连接失败:', e.smtp_code, e.smtp_error
        except smtplib.SMTPAuthenticationError, e:
            print '邮件发送失败，认证错误:', e.smtp_code, e.smtp_error
        except smtplib.SMTPSenderRefused, e:
            print '邮件发送失败，发件人被拒绝:', e.smtp_code, e.smtp_error
        except smtplib.SMTPRecipientsRefused, e:
            print '邮件发送失败，收件人被拒绝:', e.smtp_code, e.smtp_error
        except smtplib.SMTPDataError, e:
            print '邮件发送失败，数据接收拒绝:', e.smtp_code, e.smtp_error
        except smtplib.SMTPException, e:
            print '邮件发送失败, ', e.message
        except Exception, e:
            print '邮件发送异常, ', str(e)

if __name__=="__main__":
    Emailinno().send