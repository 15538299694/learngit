import requests
import threading
import time
import random
from ceshi import configfile


# from cssg import configfile
class fc(threading.Thread):
    def __init__(self,num,count):
        threading.Thread.__init__(self)
        self.num = num
        self.count=count
    def run(self):
        if self.num<=0:
            self.num=1
        if self.count <= 0:
            self.count = random.randint(1, 10)
        print('发车开始，此次发车数量为%s辆'%self.num)
        for i in range(0,self.num):
            create(self.count)
        print('发车结束')
        # from project import zddc
        # zddc.zddc(configfile.daodaname)

def creUserId():
    now_time = '%.0f' % (time.time() * 1000)
    t1 = now_time[:5]
    t2 = now_time[-4:]
    t3 = now_time[5:-4]
    userId = t1 + t2 + t3
    return userId
def create(count):#发车---发车部门发到到达部门
    resid =  requests.post(configfile.idurl, data=configfile.idparams, headers=configfile.headers)#到达部门ID
    DDdeptId =  resid.json()["rows"][0]["deptId"]
    configfile.cparams["discPlaceId"]=DDdeptId
    # print(configfile.cparams)
    userId = creUserId()
    configfile.headers['userId']=userId
    rescc=requests.post(configfile.curl, data=configfile.cparams, headers=configfile.headers)#创建车次
    # print(rescc.json())
    voyageNo=rescc.json()['rows']['voyageNo']#拿到车次号
    print('创建车次，车次编号为:',voyageNo)

    voyageId=rescc.json()['rows']['voyageId']
    sparams = {
        "voyageId": voyageId,
        "searchZx": "0",
        "terminal": "PC",
        "module": "transportOutAdd"
    }
    ressl=requests.post(configfile.surl, data=sparams, headers=configfile.headers)#查询订单
    if ressl.json()['rows']==[]:
        print('无可用订单')
    yu=len(ressl.json()['rows'])-count

    orderBarNos = ''
    for i in range(0,count):#插入count条数据
        orderNos=ressl.json()['rows'][i]['orderBarNos']#拿到前几条运单数据
        print(orderNos)
        ziorderNos=",".join(orderNos)
        orderBarNos=orderBarNos+ziorderNos+','
    configfile.pparams['orderBarNos']= orderBarNos[:-1]
    configfile.pparams['voyageId']=voyageId

    userId = creUserId()
    configfile.headers['userId'] = userId
    respush=requests.post(configfile.purl, data=configfile.pparams, headers=configfile.headers)#推送运单
    print(respush.json()['msg'],'，配载数量为%s单，余%d单'%(count,yu))

    configfile.clparams["discPlaceId"] = DDdeptId
    rescl = requests.post(configfile.clurl, data=configfile.clparams, headers=configfile.headers)#查询车辆信息
    if rescl.json()['rows'][0]["truckTypeName"]=="牵引头":
        cph=rescl.json()['rows'][1]["truckCode"]
    else:
        cph=rescl.json()['rows'][0]["truckCode"]
    configfile.fparams['truckCode']=cph
    configfile.fparams['voyageId']=voyageId
    resfc=requests.post(configfile.furl, data=configfile.fparams, headers=configfile.headers)#发车出库
    print(resfc.json()['msg'])


#第一个参数为发多少车
#第二个参数为配载几件,0代表随机1-10单,配载均为所有子单
thread1=fc(40,1)
thread1.start()