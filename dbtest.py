#!/usr/bin/env python
# --*-- coding:utf-8 --*--
''' This is a db connect execise '''

import MySQLdb


try:
    db= MySQLdb.connect(user='root',db='db_name',passwd='*******',host='127.0.0.1',charset='utf8')
except Exception,e:
    print e
    sys.exit()
cursor = db.cursor()
sql= 'select * from cms_sections limit 5'
cursor.execute(sql)
data=cursor.fetchall()
print "the select result set is %s " %  type(data)
if data:
    for x in data:
        print x
        l = list(x)
        print l
        print l[4],l[6]
        #print x[:]
        #print x[6].encode('utf8')
cursor.close()
db.close()
