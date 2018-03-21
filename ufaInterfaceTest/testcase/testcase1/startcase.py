# -*- coding:utf-8 -*-

import unittest
import requests
from ufaInterfaceTest.common import httpRequest,configDB
import json
import sys
import HTMLTestRunner,os,time
import pymysql

class Startcase():
    host = "localhost"
    username = "jamko"
    password = "ufa123456"
    dbname = "interfacetestcase"
    def __init__(self):
        print("This is testcase1's startcase.")

    def getTemDG(self):
        try:
            response = requests.get("https://www.sojson.com/open/api/weather/json.shtml?", params={"city":"东莞"})
            return response.text
        except TimeoutError:
            print("it is timeout")
            return "hello get"

    def getTemBJ(self):
        try:
            response = requests.get("https://www.sojson.com/open/api/weather/json.shtml?",
                                    params={"city": "北京"})
            return response.text
        except TimeoutError:
            print("it is timeout")
            return "hello get"

            # define get result value by key

    def getResultValue(self, result, data):
        result_dict = json.loads(result)
        print("---------********")
        length = len(data)
        print(length)
        for i in range(length):
            print(data[i])
        print(result_dict)
        print(type(result_dict))
        print(result_dict["status"])
        print(result_dict["data"]["shidu"])

    def queryData(self,sql):
        print("query some data from mysql")
        db = pymysql.Connect("localhost", "jamko", "ufa123456", "interfacetestcase")
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print("DataBase version is : %s" % data)
        cursor.execute("SELECT * from interfacetestcase.author")
        data2 = cursor.fetchone()
        print("author is : %s" % data2[1])
        db.close()

    def queryDataBySQL(self,sql):
        db = pymysql.Connect("localhost", "jamko", "ufa123456", "interfacetestcase",charset='utf8')
        cursor = db.cursor()
        cursor.execute(sql)
        #data = cursor.fetchone()
        datas = cursor.fetchall()
        result_db = datas[0]
        shidu_expect = result_db[5]
        print("shidu_expect is : %s" % shidu_expect)
        db.close()
        runcase = Startcase()
        result = runcase.getTem()
        result_dict = json.loads(result)
        shidu = result_dict["data"]["shidu"]
        print(result)
        print("shidu_real is : %s" % shidu)

    def queryDataBySQL2(self,sql):
        db = pymysql.Connect("localhost", "jamko", "ufa123456", "interfacetestcase",charset='utf8')
        cursor = db.cursor()
        cursor.execute(sql)
        datas = cursor.fetchall()
        result_db = datas[0]
        shidu_expect = result_db[5]
        print("shidu_expect is : %s" % shidu_expect)

        runcase = Startcase()
        result = runcase.getTem()
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
            print("testcase is succeful.%s" %sql_pass)
        else:
            sql_fail = "UPDATE interfacetestcase.testcase SET result=2,realResult=" + "'" + shidu_real + "'" + " where id=1;"
            try:
                cursor.execute(sql_fail)
                db.commit()
            except:
                db.rollback()
            print("testcase is fail.%s" %sql_fail)
        db.close()

if __name__ == "__main__":
    """runcase = Startcase()
    result = runcase.getTem()
    result_dict = json.loads(result)
    shidu = result_dict["data"]["shidu"]
    print(result)
    print(shidu)"""
    runcase = Startcase()
    sql = "SELECT * from interfacetestcase.testcase;"
    runcase.queryDataBySQL2(sql)