# -*- coding:utf-8 -*-
import unittest,requests,json,sys,pymysql,HTMLTestRunner,os,time
from ufaInterfaceTest.common import httpRequest,configDB
from ufaInterfaceTest.testcase.testcase1 import startcase

class weather(unittest.TestCase):
    print("---------")

    def __int__(self):
        print()

    def setUp(self):
        print()

    def test_QueryHumidityDG(self):
        print("--Dongguan--")
        sql = "SELECT * from interfacetestcase.testcase;"
        db = pymysql.Connect("localhost", "jamko", "ufa123456", "interfacetestcase", charset='utf8')
        cursor = db.cursor()
        cursor.execute(sql)
        datas = cursor.fetchall()
        result_db = datas[0]
        shidu_expect = result_db[5]
        print("shidu_expect is : %s" % shidu_expect)

        runcase = startcase.Startcase()
        result = runcase.getTemDG()
        result_dict = json.loads(result)
        shidu_real = result_dict["data"]["shidu"]
        print(result)
        print("shidu_real is : %s" % shidu_real)
        if shidu_expect == shidu_real:
            sql_pass = "UPDATE interfacetestcase.testcase SET result=1,realResult=" + "'" + shidu_real + "'" + " where id=1;"
            try:
                cursor.execute(sql_pass)
                db.commit()
            except:
                db.rollback()
            print("testcase is succeful.%s" % sql_pass)
        else:
            sql_fail = "UPDATE interfacetestcase.testcase SET result=2,realResult=" + "'" + shidu_real + "'" + " where id=1;"
            try:
                cursor.execute(sql_fail)
                db.commit()
            except:
                db.rollback()
            print("testcase is fail.%s" % sql_fail)
        db.close()

    def test_QueryHumidityBJ(self):
        print("--Beijing--")
        sql = "SELECT * from interfacetestcase.testcase;"
        db = pymysql.Connect("localhost", "jamko", "ufa123456", "interfacetestcase", charset='utf8')
        cursor = db.cursor()
        cursor.execute(sql)
        datas = cursor.fetchall()
        result_db = datas[1]
        shidu_expect = result_db[5]
        print("shidu_expect is : %s" % shidu_expect)

        runcase = startcase.Startcase()
        result = runcase.getTemBJ()
        result_dict = json.loads(result)
        shidu_real = result_dict["data"]["shidu"]
        print(result)
        print("shidu_real is : %s" % shidu_real)
        if shidu_expect == shidu_real:
            sql_pass = "UPDATE interfacetestcase.testcase SET result=1,realResult=" + "'" + shidu_real + "'" + " where id=2;"
            try:
                cursor.execute(sql_pass)
                db.commit()
            except:
                db.rollback()
            print("testcase is succeful.%s" % sql_pass)
        else:
            sql_fail = "UPDATE interfacetestcase.testcase SET result=2,realResult=" + "'" + shidu_real + "'" + " where id=2;"
            try:
                cursor.execute(sql_fail)
                db.commit()
            except:
                db.rollback()
            print("testcase is fail.%s" % sql_fail)
        db.close()

    def tearDown(self):
        print()

if __name__ == "__main__":
    """
    # 定义一个测试容器
    testsuite = unittest.TestSuite
    # 将测试用例添加到容器
    testsuite.addTest(weather("test_QueryHumidityDG"))
    testsuite.addTest(weather("test_QueryHumidityBJ"))
    now = time.strptime("%Y-%m-%d_%H:%M:%S",time.localtime(time.time()))
    report_abspath = "d:/result.html"
    fp = open(report_abspath,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'接口自动化测试报告：', description=u'用例执行情况：')
    runner.run(testsuite)
    fp.close()
    
    weather = weather()
    print("--开始--")
    weather.test_QueryHumidityDG()
    print("--东莞--")
    weather.test_QueryHumidityBJ()
    print("--北京--")
    """
    unittest.main()