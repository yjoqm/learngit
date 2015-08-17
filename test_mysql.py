#!/usr/bin/env python
# coding=utf-8
import MySQLdb
import MySQLdb.cursors

conn = MySQLdb.connect(host='127.0.0.1',port=3306, user = 'root',passwd='123456',db='zampda_v3_ad', cursorclass=MySQLdb.cursors.DictCursor)
#cursorclass查询结果返回dict类型，鍵是字段名方便查询
#l连接数据庫,假如前面澧有选择数据庫的话    

#cursorclass查询结果返回dict类型，鍵是字段名方便查询
#l连接数据庫,假如前面澧有选择数据庫的话         
#conn.select_db('zampda_v3_ad')
#获取cursor
cursor = conn.cursor()
#执行sql，查询返回结果的行数，增删改返回影响的行数
print cursor.execute('select * from material_base limit 10')
#返回取的结果
print cursor.fetchall()

cursor.close()
conn.close()



