#!/usr/bin/env python
#encoding:utf-8

import os
import MySQLdb

# db config
DBHost = '192.168.0.1'
DBUser = 'ro'
DBPwd = '12356'
DBName = 'ss'

NDBHost = '192.168.0.69'
NDBUser = 'rsjot'
NDBPwd = '123456'
NDBName = 'sss_spring'



sql_associate = "SELECT account_id , associate FROM t_accountinfo_approve WHERE associate != '' AND associate IS NOT NULL;"
sql_relation = "SELECT agent_id, advertiser_id, relation_id FROM t_companymappinginfo;"
sql_insert = "INSERT INTO t_companymappinginfo(agent_id, advertiser_id, relation_id, ext_info) VALUES(%s, %s, %s, '')"
sql_update_agent_id = "UPDATE t_accountinfo SET agent_id = %s WHERE id= %s;"

def fetch_associate():
    db_conn = MySQLdb.connect(DBHost, DBUser, DBPwd, DBName, charset="utf8")
    cursor = db_conn.cursor()
    try:
        cursor.execute(sql_associate)
        data_associate = cursor.fetchall()
    except MySQLdb.Error, e:
        print "Error: unable to fectch data.%s: %s" % (e.args[0], e.args[1])
    #print data_associate
    cursor.close()
    db_conn.close()
    return data_associate

def fectch_relation():
    db_conn = MySQLdb.connect(DBHost, DBUser, DBPwd, DBName, charset="utf8")
    cursor = db_conn.cursor()
    try:
        cursor.execute(sql_relation)
        data_relation = cursor.fetchall()
    except MySQLdb.Error, e:
        print "Error: unable to fectch data.%s: %s" % (e.args[0], e.args[1])
    #print data_relation
    cursor.close()
    db_conn.close()
    return data_relation


def data_sync(data_associate, data_relation):
    db_conn = MySQLdb.connect(NDBHost, NDBUser, NDBPwd, NDBName, charset="utf8")
    cursor = db_conn.cursor()
    d = {}
    for item in data_associate:
        l_aid= item[1].split(',')
        for aid in l_aid:
            if d.has_key(aid) == False:
                d.setdefault(aid, [])
            d[aid].append(item[0])
    print d
    try:
        for k, v in d.iteritems():
            if len(v) > 1:
                print k,v
            for _v in v:
                for r_item in data_relation:
                    if r_item[0] == _v and r_item[1] == int(k):
                        if int(k) != r_item[2]:
                            print r_item, k
                        else:
                            _tmp = sql_update_agent_id % (_v, int(k))
                            cursor.execute(_tmp)
                            print _tmp
        db_conn.commit()
    except Exception, e:
        print "insert error. Error:%s" % e
        print _tmp
        print "*" * 10
    cursor.close()
    db_conn.close()






def companymapping_sync(data_associate):
    db_conn = MySQLdb.connect(DBHost, DBUser, DBPwd, DBName, charset="utf8")
    cursor = db_conn.cursor()
    i = 1000
    try:
        for item in data_associate:
            associate = item[1].split(',')
            for aid in associate:
                p = (item[0], aid, i)
                _tmp = sql_insert % p
                print _tmp
                i = i+1
                cursor.execute(_tmp)
        db_conn.commit()
    except Exception, e:
        print "insert error. Error:%s" % e
        print _tmp
        print "*" * 10

if __name__== '__main__':
    data_associate = fetch_associate()
    data_relation = fectch_relation()
    data_sync(data_associate, data_relation)
    #companymapping_sync(data_associate)
