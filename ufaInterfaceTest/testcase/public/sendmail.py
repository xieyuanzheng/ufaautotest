# -*- coding:utf-8 -*-

import unittest,os,sys,time,json,HTMLTestRunner
from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Sendmail():
    def sendMail(self,resultname):
        sender = '121546683@qq.com'
        # receiver = '121546683@qq.com'
        receiver = ['yuanzheng.xie@ufa.hk']
        subject = 'python email test'
        smtpserver = 'smtp.qq.com'
        username = '121546683@qq.com'
        password = 'cmrmvwmpjrgjbiid'
        f_email = open(resultname, 'rb')
        email_body = f_email.read()
        f_email.close()
        msg = MIMEText(email_body, _subtype='html', _charset='utf-8')
        msg['Subject'] = u'UFA登录测试报告(测试版)'
        msg['date'] = time.strftime('%a,%d %b %Y %H:%M:%S %z')
        # smtp = smtplib.SMTP()
        # smtp.connect(smtpserver,465)
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()