# !/usr/bin/python3 只能发qq，用的是qq邮箱的授权码
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import GetPath
import os

mail_host = "smtp.qq.com"  # 设置服务器
from_address = "853573584@qq.com"  # 用户名
mail_pass = "xkoxcpyswmyubcie"  # 口令

to_address = ['gaoaolei@qimao.com', 'zhuguixin@qimao.com', 'shenyufan@qimao.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


def send_mail(content):
    """创建混合类型的邮件实例"""
    message = MIMEMultipart()

    """头部分"""
    message['From'] = Header("admin", 'utf-8')
    message['To'] = Header("广告测试组", 'utf-8')
    message['Subject'] = Header('广告回归监控(正式环境)', 'utf-8')

    """内容部分"""
    textpart = MIMEText(content)

    """附件部分"""
    path = os.path.join(GetPath.get_Path(), 'result', 'report.html')
    attachpart = MIMEText(open(path, 'rb').read(), "base64", "gb2312")
    attachpart["Content-Type"] = "application/octet-stream"
    attachpart["Content-Disposition"] = "attachment;filename='TestReport.html'"

    message.attach(textpart)
    message.attach(attachpart)

    try:
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(mail_host, 465)
        smtpObj.login(from_address, mail_pass)
        smtpObj.sendmail(from_address, to_address, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")


if __name__ == '__main__':
    content = "我是高傲雷"
    send_mail(content)