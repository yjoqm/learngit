#!/usr/bin/env python
#encoding:utf-8

import os
import datetime
import MySQLdb

DBHost = '221.228.208.58'
DBUser = 'exposer'
DBPwd = 'exposer123'
DBName = 'z_kup'

sql_fetch = '''
replace  into hub_data_source_view_day (`client_id`,  `code_id`, `file_path`, `status`, `process_date`, `data_time`, `process_result`, `process_count`, `process_success`, `process_fail`, `access_flag`, `click`, `meta_type_id`, `import_type_id`, `update_time`, `track_id`) 
select client_id, code_id, '', 2, '%s', '%s', NULL, sum(process_count), sum(process_success), sum(process_fail), access_flag, sum(click), meta_type_id, import_type_id, now(), track_id  from hub_data_source_view where process_date >= '%s' and process_date < date_add('%s', interval 1 day) group by track_id, client_id, code_id, access_flag, meta_type_id, import_type_id ;
'''

def fetch_data(exe_sql, begin, end):
  db_conn = MySQLdb.connect(DBHost, DBUser, DBPwd, DBName, charset="utf8")
  cursor = db_conn.cursor()

  begin = datetime.datetime.strptime(begin, '%Y-%m-%d')
  end = datetime.datetime.strptime(end, '%Y-%m-%d')

  try:
    for i in range((end - begin).days + 1):
      day = begin + datetime.timedelta(days=i)
      t = exe_sql % (day, day, day, day)
      cursor.execute(t)
    db_conn.commit()
  except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
  cursor.close()
  db_conn.close()
  return True


if __name__ == '__main__':
    begin = '2015-06-07'
    end = '2015-06-07'
    datas = fetch_data(sql_fetch, begin, end)
    print datas
