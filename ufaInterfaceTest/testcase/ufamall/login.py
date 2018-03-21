# -*- coding:utf-8 -*-

import unittest,os,sys,time,json,HTMLTestRunner
from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from ufaInterfaceTest.testcase.public import sendmail

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\tools\chromedriver.exe')
        self.base_url = 'http://sit.ufa.hk'
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        u"""UFA供应商登录"""
        browser = self.driver
        browser.get(self.base_url)
        browser.maximize_window()
        browser.find_element_by_class_name("htlnlLogin").click()
        browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/input").clear()
        browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/input").send_keys("15555555555")
        browser.find_element_by_xpath("//*[@id='lccPassword']").clear()
        browser.find_element_by_xpath("//*[@id='lccPassword']").send_keys("123456")
        browser.find_element_by_xpath("/html/body/div[2]/div/div/div[6]/span").click()
        time.sleep(1)

    def test_logout(self):
        #browser = self.driver
        #browser.quit()
        pass

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Login("test_login"))
    #suite.addTest(Login("test_logout"))
    filename="D:\\result.html"
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'UFA登录测试报告',description=u'测试用例执行情况:')
    #unittest.main(defaultTest="suite")
    runner.run(suite)
    fp.close()
    send = sendmail.Sendmail()
    send.sendMail(filename)