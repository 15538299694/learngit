import requests
from urllib.parse import urlencode
password="123456"
username="富达长武"

url="http://47.97.51.50:8090/tms-ylpt-test/token/login"
headers1={
    "Accept": "application/json, text/plain, */*",
    "module": "login",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "120.26.77.215:1661",
    "terminal": "PC"
}
params={
    "username":username,
    "password":password,
    "terminal":"PC",
    "module":"login"
}
res=requests.post(url,data=params,headers=headers1)
token=res.json()['rows']['token']

def tuihuo(orderNo):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "8.136.132.172:8090",
        "Authorization": token,
        "terminal": "PC"
    }
    url='http://47.97.51.50:8090/tms-ylpt-test/orderReturn/selectOrderHdrByOrderNo'
    params1 = {
        "orderNo": orderNo,
        "terminal": "PC",
        "module": "orderReturn"
    }
    res = requests.post(url, headers, params=params1)
    print(res.json()["rows"])
    orderId=res.json()["rows"]["orderId"]
    print(orderId)


    urlth='http://47.97.51.50:8090/tms-ylpt-test/orderReturn/addOrderReturn'
    paramsth = {
        "returnOrderNo": orderNo,
        "returnNo": orderNo,
        "returnDeptId": "005058",
        "returnDeptName": '富达北徐一部',
        "applyReason": "11",
        "orderId": orderId,
        "terminal": "PC",
        "module": "orderReturn"

    }
    resth = requests.post(urlth, headers, params=paramsth)
    print(resth.json())
    print(resth.json()['msg'])
def shenhe(orderNo):
    token1='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsY0lkIjoiMzA1NyIsImludGVyY29ubmVjdENvbXBhbnlDb2RlIjoiIiwiZW1wSWQiOiI0QUU5RkU0MEZGNzI0MkQzOTEzOEZGNkU5RjNDMjk1MiIsImRlcHROYW1lIjoi5a-M6L6-5YyX5b6Q5LiA6YOoIiwiZW1wTW9iaWxlIjoiIiwicGFzc3dvcmRUaW1lIjp7Im5hbm9zIjowfSwiZ2VuZGVyIjoiIiwiaW5zVGltZSI6eyJuYW5vcyI6MH0sImNvbXBhbnlOYW1lIjoi6ZmV6KW_5a-M6L6-5LiH6YeM5L6b5bqU6ZO-566h55CG5pyJ6ZmQ5YWs5Y-4IiwibG9naW5Db2RlIjoi5a-M6L6-5YyX5b6Q5LiA6YOoIiwicmVtYXJrIjoiIiwiZGVwdE5vIjoiRkRORjAwNCIsImVtcFVwZFJvbGUiOiI1ODkwMSIsInByb3BvcnRpb25hbFNoYXJlIjoiNjk2MDIiLCJpc1NhYXNTeXN0ZW0iOiIwIiwiaW50ZXJjb25uZWN0Q29tcGFueUlkIjoiIiwidXBkVXNlciI6IkZEYWRtaW4iLCJhdHRySXNPcGVuIjoiMCIsInVwZFRpbWUiOnsibmFub3MiOjB9LCJlbXBOYW1lIjoi5YyX5b6Q5LiA6YOoIiwibG9naW5QYXNzd29yZCI6IjEyMzQ1NiIsImlzSW50ZXJjb25uZWN0IjoiMCIsImludGVyY29ubmVjdENvbXBhbnlOYW1lIjoiIiwiaWF0IjoxNjgyMDYyNTY3NzU4LCJiaWxsTGF5b3V0IjoiW3tcInhcIjowLFwieVwiOjAsXCJ3XCI6MTIsXCJoXCI6MS4yLFwiaVwiOlwiMFwiLFwibW92ZWRcIjpmYWxzZX0se1wieFwiOjQsXCJ5XCI6MS4yLFwid1wiOjEyLFwiaFwiOjMuMixcImlcIjpcIjFcIixcIm1vdmVkXCI6ZmFsc2V9LHtcInhcIjo0LFwieVwiOjQuNCxcIndcIjoxMixcImhcIjozLjYsXCJpXCI6XCIyXCIsXCJtb3ZlZFwiOmZhbHNlfSx7XCJ4XCI6NCxcInlcIjo4LFwid1wiOjEyLFwiaFwiOjYuOTUsXCJpXCI6XCIzXCIsXCJtb3ZlZFwiOmZhbHNlfSx7XCJ4XCI6NCxcInlcIjoxNC45NSxcIndcIjoxMixcImhcIjozLjUsXCJpXCI6XCI0XCIsXCJtb3ZlZFwiOmZhbHNlfV0iLCJhZGRyZXNzIjoiIiwiYXV0aExvZ2luIjoiMSIsImNvbXBhbnlUeXBlIjoiMTg0MDMiLCJkZXB0SWQiOiIwMDUwNTgiLCJkZXB0VHlwZUNvZGUiOiIxMjAwMSIsImFjdGl2ZSI6IjEiLCJsb2dpblN0YXR1cyI6IjEiLCJjb21wYW55SWQiOiIwMDU5IiwiZW1wQ29kZSI6IlNYRkQtMDA0IiwiZXhwaXJlIjoxNjgyMDY2MTY3NzU4LCJicmFuZElkIjoiMjA1NSIsImlkY2FyZCI6IiIsInRlbmFudElkIjoiMTAxIiwiaW5zVXNlciI6IkZEYWRtaW4ifQ.bQZzc4vPGXrJEF_6VpJAmn4unAPKSk_Yt9ND_cj4Q_Q'
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "8.136.132.172:8090",
        "Authorization": token1,
        "terminal": "PC"
    }
    urlcx='http://47.97.51.50:8090/tms-ylpt-test/orderReturn/selectOrderReturnByTrem'
    paramscx = {
        "orderNo": orderNo,
        "auditType": 0,
        "terminal": "PC",
        "module": "orderReturn"
    }
    resid=requests.post(urlcx, headers, params=paramscx)
    returnid=resid.json()["rows"][0]["returnId"]
    print(returnid)

    shenpiurl='http://47.97.51.50:8090/tms-ylpt-test/orderReturn/auditOrderReturn'
    paramssp={
        "returnId": returnid,
        "terminal": "PC",
        "module": "orderReturn"
    }
    ressp=requests.post(shenpiurl, headers, params=paramssp)
    print(ressp.json())
    print(ressp.json()['msg'])
def yiku(orderNo):
    token2='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsY0lkIjoiMzA1NyIsImludGVyY29ubmVjdENvbXBhbnlDb2RlIjoiIiwiZW1wSWQiOiI0QUU5RkU0MEZGNzI0MkQzOTEzOEZGNkU5RjNDMjk1MiIsImRlcHROYW1lIjoi5a-M6L6-5YyX5b6Q5LiA6YOoIiwiZW1wTW9iaWxlIjoiIiwicGFzc3dvcmRUaW1lIjp7Im5hbm9zIjowfSwiZ2VuZGVyIjoiIiwiaW5zVGltZSI6eyJuYW5vcyI6MH0sImNvbXBhbnlOYW1lIjoi6ZmV6KW_5a-M6L6-5LiH6YeM5L6b5bqU6ZO-566h55CG5pyJ6ZmQ5YWs5Y-4IiwibG9naW5Db2RlIjoi5a-M6L6-5YyX5b6Q5LiA6YOoIiwicmVtYXJrIjoiIiwiZGVwdE5vIjoiRkRORjAwNCIsImVtcFVwZFJvbGUiOiI1ODkwMSIsInByb3BvcnRpb25hbFNoYXJlIjoiNjk2MDIiLCJpc1NhYXNTeXN0ZW0iOiIwIiwiaW50ZXJjb25uZWN0Q29tcGFueUlkIjoiIiwidXBkVXNlciI6IkZEYWRtaW4iLCJhdHRySXNPcGVuIjoiMCIsInVwZFRpbWUiOnsibmFub3MiOjB9LCJlbXBOYW1lIjoi5YyX5b6Q5LiA6YOoIiwibG9naW5QYXNzd29yZCI6IjEyMzQ1NiIsImlzSW50ZXJjb25uZWN0IjoiMCIsImludGVyY29ubmVjdENvbXBhbnlOYW1lIjoiIiwiaWF0IjoxNjgyMDYyNTY3NzU4LCJiaWxsTGF5b3V0IjoiW3tcInhcIjowLFwieVwiOjAsXCJ3XCI6MTIsXCJoXCI6MS4yLFwiaVwiOlwiMFwiLFwibW92ZWRcIjpmYWxzZX0se1wieFwiOjQsXCJ5XCI6MS4yLFwid1wiOjEyLFwiaFwiOjMuMixcImlcIjpcIjFcIixcIm1vdmVkXCI6ZmFsc2V9LHtcInhcIjo0LFwieVwiOjQuNCxcIndcIjoxMixcImhcIjozLjYsXCJpXCI6XCIyXCIsXCJtb3ZlZFwiOmZhbHNlfSx7XCJ4XCI6NCxcInlcIjo4LFwid1wiOjEyLFwiaFwiOjYuOTUsXCJpXCI6XCIzXCIsXCJtb3ZlZFwiOmZhbHNlfSx7XCJ4XCI6NCxcInlcIjoxNC45NSxcIndcIjoxMixcImhcIjozLjUsXCJpXCI6XCI0XCIsXCJtb3ZlZFwiOmZhbHNlfV0iLCJhZGRyZXNzIjoiIiwiYXV0aExvZ2luIjoiMSIsImNvbXBhbnlUeXBlIjoiMTg0MDMiLCJkZXB0SWQiOiIwMDUwNTgiLCJkZXB0VHlwZUNvZGUiOiIxMjAwMSIsImFjdGl2ZSI6IjEiLCJsb2dpblN0YXR1cyI6IjEiLCJjb21wYW55SWQiOiIwMDU5IiwiZW1wQ29kZSI6IlNYRkQtMDA0IiwiZXhwaXJlIjoxNjgyMDY2MTY3NzU4LCJicmFuZElkIjoiMjA1NSIsImlkY2FyZCI6IiIsInRlbmFudElkIjoiMTAxIiwiaW5zVXNlciI6IkZEYWRtaW4ifQ.bQZzc4vPGXrJEF_6VpJAmn4unAPKSk_Yt9ND_cj4Q_Q'
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "8.136.132.172:8090",
        "Authorization": token2,
        "terminal": "PC"
    }
    urlyk = 'http://47.97.51.50:8090/tms-ylpt-test/stockManage/addOrderHdrMoveStock'
    orderBarno='YF'+str(orderNo)+'001'
    orderBarno1='YF'+str(orderNo)+'002'
    paramsyk = {
        "orderNo": 'YF'+str(orderNo),
        "orderBarNos":orderBarno+','+orderBarno1,
        "orderRemark":"1",
        "terminal": "PC",
        "module": "orderReturn"
    }
    print(paramsyk)
    residyk=requests.post(urlyk, headers, params=paramsyk)
    print(residyk.json())


if __name__ == '__main__':
    for i in range(2304000035,2304000078):
        try:
            # tuihuo(i)
            # shenhe(i)
            yiku(i)
        except:
            continue






