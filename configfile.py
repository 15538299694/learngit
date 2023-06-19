import time
import requests

now_time = '%.0f' % (time.time() * 1000)

ipurl="http://47.97.51.50:8090/"
# ipurl="http://47.114.105.179:8080/"#生产
# test="ylpt-anhui"#安徽
test="tms-ylpt-test"
# test="tms-ylpt-test-a"
# test="tms-ylpt"#生产


url=ipurl+test+'/token/login'
curl=ipurl+test+'/voyage/addVoyageHdr'#创建车次
surl=ipurl+test+'/voyage/selectOrderAndPackageForLoad'#查询运单
purl=ipurl+test+'/voyage/loadOrderToVoyage'#推送运单
furl=ipurl+test+'/voyage/confirmVoyage'#发车出库
scurl=ipurl+test+'/arriveManage/selectVoyageHdrList'#查询车次
dcurl=ipurl+test+'/arriveManage/updateVoyageArrivedByVoyageId'#到车确认
qsurl=ipurl+test+'/arriveManage/arrivedSign'#到货签收确认
cxurl=ipurl+test+'/arriveManage/selectOrderSignListByVoyageIdAndIsArrived'#查询车上货物数据
clurl=ipurl+test+'/truck/selectTruckListByVoyage'#查询车辆信息

headers1={
    "Accept": "application/json, text/plain, */*",
    "module": "login",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "120.26.77.215:1661",
    "terminal": "PC"
}
username=input("请输入发车部门:")
daodaname=input("请输入到达部门:")

# username="丈子头网点"
password="123456"
# "username":"antchain",
# "password":"hypertext@2021",
# "password":"antchain2020",
params={
    "username":username,
    "password":password,
    "terminal":"PC",
    "module":"login"
}

res=requests.post(url,data=params,headers=headers1)
# print("1",res.json())
token=res.json()['rows']['token']
DQdeptId=res.json()['rows']['deptId']


headers={
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "8.136.132.172:8090",
    "Authorization":token,
    "terminal": "PC"
}

a=input("1为短驳：")
if a == "1":
    transportType = "19401"
    idurl = ipurl + test + '/department/selectDepartmentBySameCompany'  # 查询到达部门ID
else:
    transportType = "19403"
    idurl = ipurl + test + '/department/selectDepartmentOtherFb'  # 查询到达部门ID
cparams={
    "loadPlaceId": DQdeptId,#当前部门ID
    "discPlaceId": "discPlaceId",#到达部门ID
    "estimatedTimeOfArrival": now_time,
    "voyageMode": "23202",
    "orderDate": "NaN",
    "transportType": transportType,#干线 19403    短驳 19401
    "isActive": "true",
    "terminal": "PC",
    "module": "transportOutAdd"
}

pparams={
    "voyageId": "823888662180659200",
    "loadType": "1",
    "terminal": "PC",
    "module": "transportOutAdd"
}
fparams={
    "voyageId": "825018906560827392",
    "truckCode": "豫A34567",
    "driverId1": "820330633850527744",
    "driverName1": "张三",
    "driverMobile1": "16616616616",
    "estimatedTimeOfArrival": now_time,
    "totalOrder": "1",
    "totalQty": "1",
    "totalCbm": "1",
    "totalKgs": "1",
    "amountZcx": "0",
    "amountLdx": "0",
    "unloadType": "60402",
    "isForceLingDanXie": "false",
    "affixName": [],
    "terminal": "PC",
    "module": "transportOutAdd"
}

scparams={
    "voyageStatus": "11403",
    "transportTimeBegin": "1616774400000",
    "transportTimeEnd": now_time,
    "pageNum": "1",
    "pageSize": "100",
    "terminal": "PC",
    "module": "voyageHdr"
}
dcparams={
    "voyageIds":	"825394168221683712",
    "terminal":	"PC",
    "module":	"voyageHdr"
}

qsparams={
    "voyageId": "",
    "voyageDtlListJson": [],
    "transOrderDtlListJson": [],
    "terminal": "PC",
    "module": "signArrivalGoods"
}
cxparams={
    "voyageId": "825313457942585344",
    "isArrived": "13001",
    "terminal": "PC",
    "module": "signArrivalGoods"
}
clparams={
    "module": "truck",
    "loadPlaceId": DQdeptId,
    "discPlaceId": "discPlaceId",
    "truckCode": "豫A",
    # "truckCode": "豫K",
    # "truckCode": "皖A",
    "terminal": "PC"
}
idparams={
    "deptName": daodaname,
    "terminal": "PC",
    "module": "transportOutAdd"
}