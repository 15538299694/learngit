# -*- coding: UTF-8 -*-
'''
总后台增加币种脚本
'''

from Tools.PythonHelpApi import FUBTAPI
import requests
Sheetname="Sheet1"
Elpath="C:\\Users\\Administrator.Sc-202007121657\\Desktop\\V网币种资料.xls"
URL="https://manager.rest.test.com/coin"
headers={
"authorization": "eyJhbGciOiJIUzI1NiJ9qweeyJyYW5kb20iOjUwNTAyMDU3OSwiaWQiOiIzNjE4NDM2ODc3MDcxMjM3MTIifQqwenRc5wprFkh6t2Cw5P5SuAQASJQIyEXLTLVtb_icLXQE"
}
Now = FUBTAPI().ReadExceldata(Sheetname, 0, 0, Elpath)[1]#获取Excel总行数
for i in range(8,int(Now)):
    name=FUBTAPI().ReadExceldata(Sheetname,i,1,Elpath)[0]
    ENname=FUBTAPI().ReadExceldata(Sheetname,i,2,Elpath)[0]
    CNname=FUBTAPI().ReadExceldata(Sheetname,i,3,Elpath)[0]
    print(name,ENname,CNname)
    if CNname=="":
        CNname=name
    params = {
            "englishName": ENname,
            "listedPrice": 1,
            "logo": "https://other-resources.hk.ufileos.com/8700f041-827e-404e-9992-f0e48d687c90",
            "method": "post",
            "name": name,
            "needTag": "false",
            "shortName": CNname,
            "virtualCurrencyType": "490225022544117760",
            "walletType": "472693925186895872"
        }
    res=requests.post(url=URL,headers=headers,json=params)
    print(res.json())