import requests
from urllib.parse import urlencode
password="123456"
username="admin"

url="http://47.97.51.50:8090/tms-ylpt-test-a/token/login"
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
# print(token)

def xinjianzhanghao(deptname,lgcode):

    url1='http://47.97.51.50:8090/tms-ylpt-test-a/department/selectDeptByNameDataPermission'
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "8.136.132.172:8090",
        "Authorization": token,
        "terminal": "PC"
    }

    params1 = {
        "deptName": deptname,
        "terminal": "PC",
        "module": "employee"
    }
    # params2=urlencode(params1)
    res=requests.post(url1,headers,params=params1)
    deptNo=res.json()["rows"][0]["deptNo"]
    deptId=res.json()["rows"][0]["deptId"]
    deptName1=res.json()["rows"][0]["deptName"]
    params2 = {
        "empName":lgcode,
        "loginCode":lgcode,
        "active":"1",
        "authLogin":"1",
        "empCode":lgcode,
        "deptNo":deptNo,
        "empUpdRole":"58901",
        "attrIsOpen":"0",
        "deptId":deptId,
        "roleIds":"shylcs",
        "roleNames":"上海蚁链-测试",
        "deptName": deptName1,
        "terminal": "PC",
        "module": "employee"
    }
    url2="http://47.97.51.50:8090/tms-ylpt-test-a/employee/addEmployee"
    resadd=requests.post(url2,headers,params=params2)
    print(resadd.json(),"新建账号")
def shanchu(lgcode):
    url3='http://47.97.51.50:8090/tms-ylpt-test-a/employee/selectEmployeesByConditions'
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "8.136.132.172:8090",
        "Authorization": token,
        "terminal": "PC"
    }
    params1 = {
        "loginCode": lgcode,
        "terminal": "PC",
        "module": "employee"
    }
    resbh=requests.post(url3,headers,params=params1)
    empId=resbh.json()["rows"][0]["empId"]
    # print(empId,"查询新增员工id")
    urlsc='http://47.97.51.50:8090/tms-ylpt-test-a/employee/deleteEmployeeByEmpId'
    paramssc = {
        "empIds":empId,
        "terminal": "PC",
        "module": "employee"
    }
    ressc=requests.post(urlsc,headers,params=paramssc)
    print(ressc.json(),"删除员工")
def tk2(lgcode):
    url = "http://47.97.51.50:8090/tms-ylpt-test-a/token/login"
    headers1 = {
        "Accept": "application/json, text/plain, */*",
        "module": "login",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "120.26.77.215:1661",
        "terminal": "PC"
    }
    params = {
        "username": lgcode,
        "password": "123456",
        "terminal": "PC",
        "module": "login"
    }
    res = requests.post(url, data=params, headers=headers1)
    token2 = res.json()['rows']['token']
    return token2
def shandan(token2,orderNo):
    url4 = 'http://47.97.51.50:8090/tms-ylpt-test-a/OrderDtl/selectOrderDtlList'
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "8.136.132.172:8090",
        "Authorization": token2,
        "terminal": "PC"
    }
    params4 = {
        "orderNo":orderNo,
        "terminal": "PC",
        "module": "waybillManger"
    }
    orderId=requests.post(url4,headers,params=params4)
    countzd=orderId.json()['total']
    orderBarNos = ''
    for i in range(0, countzd):  # 插入count条数据
        orderNos = orderId.json()['rows'][i]['orderBarNo']  # 拿到前几条运单数据
        orderBarNos = orderBarNos + orderNos + ','
    params5={
        "orderNo": orderNo,
        "orderBarNos":"",
        "orderRemark":"钉钉流程移库",
        "terminal": "PC",
        "module": "stockManage"
    }
    params5['orderBarNos'] = orderBarNos[:-1]
    url5='http://47.97.51.50:8090/tms-ylpt-test-a/stockManage/addOrderHdrMoveStock'
    # print(params5,"")
    yk=requests.post(url5,headers,params=params5)
    print(yk.json(),"移库")


    ids=orderId.json()["rows"][0]["orderId"]
    urlsd="http://47.97.51.50:8090/tms-ylpt-test-a/orderHdr/deleteOrderHdr"
    paramssd = {
        "ids": ids,
        "deleteReason":"钉钉流程删单",
        "terminal": "PC",
        "module": "waybillManger"
    }
    resd=requests.post(urlsd,headers,params=paramssd)
    print(resd.json(),"删单")
def ReadExceldata(Sheetname,x,y,z,ExcelPath):#读取excel数据
    import xlrd
    ExcelPath=ExcelPath
    Sheet=xlrd.open_workbook(ExcelPath).sheet_by_name(Sheetname)
    return str(Sheet.cell_value(x,y)),Sheet.cell_value(x,z)

    # return Sheet.cell_value(x,y)
def ReadExceldatarow():#读取excel数据
    import xlrd
    Sheetname = "Sheet1"
    ExcelPath = 'C:\\Users\\lenovo\\Desktop\\111111.xls'
    ExcelPath=ExcelPath
    Sheet=xlrd.open_workbook(ExcelPath).sheet_by_name(Sheetname)
    return Sheet.nrows
if __name__ == '__main__':
    row=ReadExceldatarow()
    for i in range(0,row):
        x = i
        y = 0
        z = 1
        Sheetname="Sheet1"
        ExcelPath='C:\\Users\\lenovo\\Desktop\\111111.xls'
        order,dpname=ReadExceldata(Sheetname,x,y,z,ExcelPath)
        deptname = dpname
        lgcode="dingdingshandan"
        orderNo=order
        print(dpname,order)
        xinjianzhanghao(deptname,lgcode)
        token2=tk2(lgcode)
        shandan(token2,orderNo)
        shanchu(lgcode)