#!/usr/bin/env python
# coding=utf-8

import requests
import time
import datetime
import threading

class url_request():
    times = []
    error = []

    def req(self):
        myreq = url_request()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
        url = 'http://172.22.50.134:8003/v1/api/attrs/?advertiser_id=130'
        r = requests.get(url, headers=headers)
        ResponseTime = float(r.elapsed.microseconds)/1000 #获取响应时间，单位ms
        myreq.times.append(ResponseTime)
        if r.status_code != 200:
            myreq.error.append('0')

if __name__ =='__main__':
    myreq = url_request()
    threads = []
    starttime = datetime.datetime.now()
    print "requst start time %s" %starttime
    nub = 50 #设置并发线程数
    ThinkTime = 0.5
    for i in range(1,nub+1):
        t = threading.Thread(target=myreq.req)
        threads.append(t)
    for t in threads:
        time.sleep(ThinkTime)
        t.setDaemon(True)
        t.start()
        t.join()
    endtime = datetime.datetime.now()
    print "requests end time %s" %endtime
    time.sleep(3)
    AverageTime = "{:.3f}".format(float(sum(myreq.times))/float(len(myreq.times)))
    print "Average Response Time %s ms" %AverageTime #打印平均响应时间
    usetime = str(endtime - starttime)
    hour = usetime.split(':').pop(0)
    minute = usetime.split(':').pop(1)
    second = usetime.split(':').pop(2)
    totaltime = float(hour)*60*60 + float(minute)*60 + float(second) #计算总的思考时间+请求时间
    print "Concurrent processing %s" %nub #打印并发数
    print "use total time %s s" %(totaltime-float(nub*ThinkTime)) #打印总共消耗的时间
    print "fail request %s" %myreq.error.count("0") #打印错误请求数

        
            
        
