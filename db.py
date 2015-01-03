import MySQLdb
print "Connnecting..."
dbh=MySQLdb.connect(user="root",passwd="test",host="localhost",db="test")
print "Connection successful"
dbh.close()

