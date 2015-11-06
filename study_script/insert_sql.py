#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
 
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306)
    cur=conn.cursor()
    conn.select_db('zampda_v3_ad')
    values = [('test_1',130,0),('test_2',100,0),('test_3',163,0)]
    sql = "insert into material_group(group_name,advertiser_id,status) values(%s,%s,%s)"
    cur.executemany(sql,values)
    
    conn.commit()
    cur.close()
    conn.close()
 
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])