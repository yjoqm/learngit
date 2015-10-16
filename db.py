import MySQLdb
print "Connnecting..."
dbh=MySQLdb.connect(user="root",passwd="test",host="localhost",db="test")
print "Connection successful"
dbh.close()

rows=(('2','two'),
('3','three'))
print "connecting...."
dbh=MySQLdb.connect(host="localhost",user="root",passwd="test",db="test")
print "connection successed"
cur=dbh.cursor()
query="insert into test values(%s,%s)"
for i in rows:
    cur.execute(query,i)
dbh.commit()
dbh.close()

