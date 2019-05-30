import requests
import json
import datetime
import time

def datetime_timestamp(dt):#将时间转换为unix时间戳
    time.strptime(dt, '%Y/%m/%d %H:%M:%S')
    s = time.mktime(time.strptime(dt, '%Y/%m/%d %H:%M:%S'))
    return int(s)

def http_post():
    nowTime = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')  # 现在的时间
    Nowtime = datetime_timestamp(nowTime)#将时间转换为时间戳
    a = json.dumps({'car_vh':'1G1BL52P7TR115520','start_time':1534370554,'end_time':1534631344})

    # print (a)
    # value = {"data":a, "type": "1"}
    headerdata = {'content-type': "application/json"}
    r = requests.post("http://127.0.0.1:5000/weekresults", data=a,headers = headerdata )
    # print (json.dumps(value))
    return r.text
result =http_post()
print (result)
print (json.dumps(value))