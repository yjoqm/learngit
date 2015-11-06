#!/usr/bin/env python
# coding=utf-8
#生成随机码
#cursor.execute(   """CREATE TABLE JHM(id int(11) primary key AUTO_INCREMENT, jhm CHAR(20) NOT NULL , status CHAR(1) NOT NULL)"""
#数据库操作
import MySQLdb
import string
import random

conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306,db="test")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS JHM") #如果存JHM则删除
cur.execute("""CREATE TABLE JHM(id int(11) primary key AUTO_INCREMENT, jhm CHAR(20) NOT NULL , status CHAR(1) NOT NULL)""")

#config
config = {'y':10, 'x':20, 'title':"yjoqm"} #20代表生成的随机码的数量，10代表长度

#生成随机数
def jhm(num):
    b = ''.join(random.sample(string.ascii_letters + string.digits,num))
    return b


def sql(w):
    try:
        cur.execute(w)
    except:
        conn.rollback()

for z in range(config['x']):
    w = "INSERT INTO JHM(jhm,status)VALUES ('%s','%s')" % (config['title'] + jhm(config['y'] - len(config['title'])),'0')
    sql(w)

conn.commit()
conn.close()
