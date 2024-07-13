import smtplib # 邮件服务
from email.mime.text import MIMEText # 邮件内容

def sendmail():
    # 发送邮件，不可自定义信息
    msg = MIMEText('bobby') # 邮件内容
    msg['Subject'] = '设备发现异常'
    msg['From'] = '331664089@qq.com'
    msg['To'] = '331664089@qq.com'
    with smtplib.SMTP('smtp.qq.com',587) as s:
        s.starttls()
        s.login('331664089@qq.com','ggvybliyujazbhhd')
        s.sendmail('331664089@qq.com',
                   ['331664089@qq.com',],
                   msg.as_string())
        print('邮件已发送')

def sendmail_users(alist):
    # 发送邮件，不可自定义信息
    msg = MIMEText('bobby') # 邮件内容
    msg['Subject'] = '设备发现异常'
    msg['From'] = '331664089@qq.com'
    msg['To'] = '331664089@qq.com'
    with smtplib.SMTP('smtp.qq.com',587) as s:
        s.starttls()
        s.login('331664089@qq.com','ggvybliyujazbhhd')
        s.sendmail('331664089@qq.com',alist,
                   msg.as_string())
        print('邮件已发送')

def sendData(info):
    # 发送邮件，并自定义信息
    msg = MIMEText('bobby') # 邮件内容
    msg['Subject'] = info
    msg['From'] = '331664089@qq.com'
    msg['To'] = '331664089@qq.com'
    with smtplib.SMTP('smtp.qq.com',587) as s:
        s.starttls()
        s.login('331664089@qq.com','ggvybliyujazbhhd')
        s.sendmail('331664089@qq.com',
                   ['331664089@qq.com','82074623@qq.com'],
                   msg.as_string())
        print('邮件已发送')
        
