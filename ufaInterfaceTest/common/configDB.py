# -*- coding:utf-8 -*-
import pymysql

class configDB():
    host = "localhost"
    username = "jamko"
    password = "ufa123456"
    dbname = "interfacetestcase"
    def __init__(self):
        print("this is configDB.py constructor function")

    def queryData(self,sql):
        print("query some data from mysql")
        #db = pymysql.Connect(configDB.host, configDB.username, configDB.password, configDB.dbname)
        db = pymysql.Connect("localhost", "jamko", "ufa123456", "interfacetestcase")
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print("DataBase version is : %s" % data)
        cursor.execute("SELECT * from interfacetestcase.author")
        data2 = cursor.fetchone()
        print("author is : %s" % data2[2])
        db.close()

    def insertData(self):
        print("add data to mysql")

    def deleteData(self):
        print("remove data from mysql")

    def updateData(self):
        print("update data from mysql")

if __name__ == "__main__":
    print("this is main function.")