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
import os
from interface_project.script import gl
import time

curDateTime = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print curDateTime
# 发件人地址，通过控制台创建的发件人地址
username = 'qa@mail.72solo.com'
# 发件人密码，通过控制台创建的发件人密码
password = 'mfl3Gy1fN0iiW8L'
# 自定义的回复地址
replyto = '***'
# 收件人地址或是地址列表，支持多个收件人，最多30个
#rcptto = ['***', '***']
rcptto = 'gaoshuai_888@163.com'
# 构建alternative结构
msg = MIMEMultipart('alternative')
msg['Subject'] = Header('点72接口自动化测试'.decode('utf-8')).encode()
msg['From'] = '%s <%s>' % (Header('接口自动化测试'.decode('utf-8')).encode(), username)
msg['To'] = rcptto
msg['Reply-to'] = replyto
msg['Message-id'] = email.utils.make_msgid()
msg['Date'] = email.utils.formatdate()
# 构建alternative的text/plain部分
# textplain = MIMEText('自定义TEXT纯文本部分', _subtype='plain', _charset='UTF-8')
# msg.attach(textplain)
# 构建alternative的text/html部分
texthtml = MIMEText('本次自动化测试结果，详情请见附件！', _subtype='html', _charset='UTF-8')
msg.attach(texthtml)

reportfile = os.path.join(gl.reportPath, 'Report.html')
#增加邮件内容为html
fp = open(reportfile, 'rb')
reportHtmlText = fp.read()
msg.attach(MIMEText(reportHtmlText,'html','utf-8'))
fp.close()

#增加附件

# 发送邮件
try:
    client = smtplib.SMTP()
    #python 2.7以上版本，若需要使用SSL，可以这样创建client
    #client = smtplib.SMTP_SSL()
    #SMTP普通端口为25或80
    client.connect('smtpdm.aliyun.com', 25)
    #开启DEBUG模式
    client.set_debuglevel(0)
    client.login(username, password)
    #发件人和认证地址必须一致
    #备注：若想取到DATA命令返回值,可参考smtplib的sendmaili封装方法:
    #      使用SMTP.mail/SMTP.rcpt/SMTP.data方法
    client.sendmail(username, rcptto, msg.as_string())
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