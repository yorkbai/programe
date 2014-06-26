#!/usr/bin/env python
# --*-- coding: utf-8 --*--

'''
Created on 2013-11-20
Function: 
@author: YorkBai
'''

import os,sys


reload(sys)
sys.setdefaultencoding("utf-8")

year = int(raw_input(u'请输入年份：'))
month = raw_input(u'请输入月份：')
day = int(raw_input(u'请输入日期：'))
dic = {'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
days = 0
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):    #如果是闰年，则二月29天
    dic['2'] = 29
    
if int(month)>1:
    for obj in dic:
        if month == obj:
            for i in range(1,int(obj)):
                days += dic[str(i)]
    days += day
else:
    days = day
print u'%s年%s月%s日是该年的第%s天' %(year,month,day,days)
