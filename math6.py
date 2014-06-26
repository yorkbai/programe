#!/usr/bin/env python
# --*-- coding:utf-8 --*--
''' this python script get the number from list that include four number '''

import os


def max_num():
    numblist = [1,2,3,4]
    numb = 0
    max = 0
#    out = open('/tmp/number.txt','w')
    for i in numblist:
        for j in numblist:
            for k in numblist:
                if k != i and k != j and j != i:
                    numb += 1
                    n= i*100 + j*10 + k
                    if n > max:
                        max = n
#                    out.write( str(n) + '\n')
#    out.close()
#    print numb
    print max

def print_char():
    print '****'
    print '*'
    print '*'
    print '****'

def table():
    for i in range(1,10):
        for j in range(1,i+1):
            print "%s*%s = %s" % (i,j,i*j) ,  #打印多个表达式，用逗号隔开，会在每个参数之间插入一个空格符
        print '\n'

if __name__ ==  "__main__":
    max_num()
    print_char()
    table()
