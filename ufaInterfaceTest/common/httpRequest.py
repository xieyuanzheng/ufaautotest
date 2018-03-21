# -*- coding:utf-8 -*-
import requests
import json

class ConfigHttp():
    def __init__(self):
        print("this is configHttp.py constructor function")

    #define http get method
    def getHttp(self):
        try:
            response = requests.get("https://www.sojson.com/open/api/weather/json.shtml?", params={"city":"东莞"})
            return response.text
        except TimeoutError:
            print("it is timeout")
            return "hello get"

    #define http post method
    def postHttp(self):
        try:
            response = requests.post("https://www.sojson.com/open/api/weather/json.shtml?", data={"city":"东莞"})
            return response.text
        except TimeoutError:
            print("it is timeout")
            return "hello post"

    #define get result value by key
    def getResultValue(self,result,data):
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

if __name__ == "__main__":
    configHttp = ConfigHttp()
    print("***********")
    result = configHttp.getHttp()
    result_json = json.dumps(result)
    data = ["status","shidu"]
    value1 = configHttp.getResultValue(result,data)
    print("-----------")