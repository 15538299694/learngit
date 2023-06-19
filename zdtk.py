import requests
from cssg.PythonHelpApi import FUBTAPI

headers1={
    "terminal": "PC",
    "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsY0lkIjoiIiwiaW50ZXJjb25uZWN0Q29tcGFueUNvZGUiOm51bGwsImVtcElkIjoiOUQ0OTJDM0EyRTA0NDJCMjg4RDg2QkUyQzQwQjgyODIiLCJkZXB0TmFtZSI6IuiagemTvuaAu-mDqCIsImVtcE1vYmlsZSI6IjEzMjEzMDkxOTY3IiwicGFzc3dvcmRUaW1lIjp7Im5hbm9zIjowfSwiZ2VuZGVyIjoiIiwiY29tcGFueU5hbWUiOiLkuIrmtbfomoHpk77nianmtYEiLCJsb2dpbkNvZGUiOiJBRE1JTiIsInJlbWFyayI6IiIsIm1zZ1B1c2hSb2xlIjoiMjIxMzMiLCJkZXB0Tm8iOiJZTFpCIiwiZW1wVXBkUm9sZSI6IjU4OTA0IiwicHJvcG9ydGlvbmFsU2hhcmUiOiI2OTYwMSIsImlzU2Fhc1N5c3RlbSI6IjAiLCJpbnRlcmNvbm5lY3RDb21wYW55SWQiOm51bGwsInVwZFVzZXIiOiLlubPlj7DnrqHnkIblkZgiLCJhdHRySXNPcGVuIjoiMCIsInVwZFRpbWUiOnsibmFub3MiOjB9LCJlbXBOYW1lIjoi5bmz5Y-w566h55CG5ZGYIiwibG9naW5QYXNzd29yZCI6IjEyMzQ1NiIsImlzSW50ZXJjb25uZWN0IjpudWxsLCJpbnRlcmNvbm5lY3RDb21wYW55TmFtZSI6bnVsbCwiaWF0IjoxNjg2MDMzNjM2NzMzLCJiaWxsTGF5b3V0IjoiW3tcInhcIjowLFwieVwiOjAsXCJ3XCI6MTIsXCJoXCI6MS4yLFwiaVwiOlwiMFwiLFwibW92ZWRcIjpmYWxzZX0se1wieFwiOjQsXCJ5XCI6MS4yLFwid1wiOjEyLFwiaFwiOjMsXCJpXCI6XCIxXCIsXCJtb3ZlZFwiOmZhbHNlfSx7XCJ4XCI6NCxcInlcIjo0LjIsXCJ3XCI6MTIsXCJoXCI6NC40LFwiaVwiOlwiMlwiLFwibW92ZWRcIjpmYWxzZX0se1wieFwiOjQsXCJ5XCI6OC42MDAwMDAwMDAwMDAwMDEsXCJ3XCI6MTIsXCJoXCI6Ni45NSxcImlcIjpcIjNcIixcIm1vdmVkXCI6ZmFsc2V9LHtcInhcIjo0LFwieVwiOjE1LjU1LFwid1wiOjEyLFwiaFwiOjMuNSxcImlcIjpcIjRcIixcIm1vdmVkXCI6ZmFsc2V9XSIsImFkZHJlc3MiOiIiLCJhdXRoTG9naW4iOiIxIiwiY29tcGFueVR5cGUiOiIxODQwMSIsImRlcHRJZCI6IjAwMjA3MiIsImRlcHRUeXBlQ29kZSI6IjEyMDA1IiwiYWN0aXZlIjoiMSIsImxvZ2luU3RhdHVzIjoiMSIsImNvbXBhbnlJZCI6IjEwMDEiLCJlbXBDb2RlIjoiQURNSU4iLCJleHBpcmUiOjE2ODYwMzcyMzY3MzMsImJyYW5kSWQiOiIiLCJwYXJlbnRFbXBDb2RlIjoiIiwiaWRjYXJkIjoiIiwidGVuYW50SWQiOiIxMDEifQ.1YBEquE6h-EU57PWPDD5mlwAIJHea2zZpOTL0cjI6nY"
}
params={
    "refundAmt":"1",
    "orderId":"TZ23060500000321",
    "txnAmt":"1",
    "origCmbOrderId":"003223060517282050185300"
}
url="http://gatewaytest.yilian56.cn/sameboat/sameboat/pay/refund"
path="C:\\Users\\lenovo\\Desktop\\111111.xls"
sheetname="Sheet1"
R3=FUBTAPI().ReadExceldata(Sheetname=sheetname,x=0,y=0,ExcelPath=path)[1]
for i in range(0,R3):
    R1 = FUBTAPI().ReadExceldata(Sheetname=sheetname, x=i, y=0, ExcelPath=path)[0]

    R2 = FUBTAPI().ReadExceldata(Sheetname=sheetname, x=i, y=1, ExcelPath=path)[0]

    print(R1)
    TKres=requests.post(url,params,headers=headers1)
    print(TKres.json())