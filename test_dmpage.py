#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import MySQLdb

try:
    conn=MySQLdb.Connect(host='192.168.0.0000',user='test',passwd='test123',port=3306)
    cur=conn.cursor()
    cur.execute('select income from exp.summary_demographic')
    result=cur.fetchone()
    #print result
    arr='%s' % result
    print type(arr)
    n=list(eval(arr))
    sum=sum(n)
    cnt=n.__len__()
    cur.execute('SELECT income FROM pub.dim_income WHERE id <>0')
    for i in range(0,cnt):
        row=cur.fetchone()
        print '%s\t\t%d%%' % (row[0],round(100*n[i]/sum))
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
