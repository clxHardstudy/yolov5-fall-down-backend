#!/usr/bin/python3
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def generate_verification_code():
    # 生成一个6位随机验证码
    code = ''.join(random.choices('0123456789', k=6))
    return code


def send_email(email):
    sender = 'clx20020905@foxmail.com'
    receivers = [email]  # 接收邮箱
    auth_code = "vujkrnexykzvfcfd"  # 授权码

    # 生成验证码
    verification_code = generate_verification_code()

    # 创建一个多部分消息对象
    message = MIMEMultipart()
    message['From'] = Header("Sender<%s>" % sender)  # 发送者
    message['To'] = Header("Receiver<%s>" % receivers[0])  # 接收者
    subject = '绑定邮箱验证码'
    message['Subject'] = Header(subject, 'utf-8')
    # 添加文本消息
    text = MIMEText('您的验证码是：%s' % verification_code, 'plain', 'utf-8')
    message.attach(text)

    server = smtplib.SMTP_SSL('smtp.qq.com', 465)
    server.login(sender, auth_code)
    server.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
    server.close()
    return verification_code


# send_email('2050669795@qq.com')
