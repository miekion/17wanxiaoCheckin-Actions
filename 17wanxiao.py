import time
import datetime
import json
import requests


# 健康打卡的URL地址
check_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"

text = input()
deptId = eval(input())
address = input()
addtext = input()
code = input()
stuNum = input()
userName = input()
phoneNum = input()
userId = input()
emergency = input()
emergencyPhone = input()
sckey = input()


area = {'address': address, 'text': addtext, 'code': code}

areaStr = json.dumps(area, ensure_ascii=False)

# POST提交的json字段，根据自己的修改
jsons = {"businessType": "epmpics", "method": "submitUpInfo",
        "jsonData": {"deptStr": {"deptid": deptId, "text": text},
                     "areaStr": areaStr,
                     "reportdate": round(time.time()*1000), "customerid": "974", "deptid": deptId, "source": "app",
                     "templateid": "pneumonia", "stuNo": stuNum, "username": userName, "phonenum": phoneNum,
                     "userid": userId, "updatainfo": [{"propertyname": "temperature", "value": "35.4"},
                                                          {"propertyname": "symptom", "value": "无症状"},
                                                          {"propertyname": "isConfirmed", "value": "否"},
                                                          {"propertyname": "isdefinde", "value": "否.未隔离"},
                                                          {"propertyname": "isGoWarningAdress", "value": "否"},
                                                          {"propertyname": "isTouch", "value": "否"},
                                                          {"propertyname": "isTransitArea", "value": "否"},
                                                          {"propertyname": "homehealth", "value": "无症状"},
                                                          {"propertyname": "xinqing", "value": "健康"},
                                                          {"propertyname": "bodyzk", "value": "是"},
                                                          {"propertyname": "cxjh", "value": "否"},
                                                          {"propertyname": "isAlreadyInSchool", "value": "没有"},
                                                          {"propertyname": "ownPhone", "value": phoneNum},
                                                          {"propertyname": "emergencyContact", "value": emergency},
                                                          {"propertyname": "mergencyPeoplePhone",
                                                           "value": emergencyPhone}], "gpsType": 0}}

response = requests.post(check_url, json=jsons)
# 以json格式打印json字符串
res = json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False)
print(res)


SCKEY = sckey

now_time = datetime.datetime.now()
bj_time = now_time + datetime.timedelta(hours=8)

test_day = datetime.datetime.strptime('2020-12-19 00:00:00','%Y-%m-%d %H:%M:%S')
date = (test_day - bj_time).days
desp = f"""
------
### 现在时间：
```
{bj_time.strftime("%Y-%m-%d %H:%M:%S %p")}
```
### 打卡信息：
```
{res}
```
> 关于打卡信息
>
> 1、成功则打卡成功
>
> 2、系统异常则是打卡频繁

### ⚡考研倒计时:
```
{date}天
```

"""

headers = {
    "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
}

send_url = f"https://sc.ftqq.com/{SCKEY}.send"

params = {
    "text": f"完美校园健康打卡---{bj_time.strftime('%H:%M:%S')}",
    "desp": desp
}
    
# 发送消息
response = requests.post(send_url, data=params, headers=headers)
if response.json()["errmsg"] == 'success':
        print("Server酱推送服务成功")
else:
        print("Something Wrong")
