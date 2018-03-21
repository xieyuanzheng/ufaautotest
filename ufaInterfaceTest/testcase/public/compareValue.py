# -*- coding:utf-8 -*-
import unittest,requests,json,sys,pymysql,HTMLTestRunner,os,time
from ufaInterfaceTest.common import httpRequest,configDB
from ufaInterfaceTest.testcase.testcase1 import startcase

class CompareValue():
    def compare(self,value1,value2):
        print()