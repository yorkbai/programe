#!/usr/bin/env python
# --*--  coding:utf-8 --*--
# Author : York bai
# Date : 2014/5/27
# Script Name:  readlog.py


''' 
    This script for stat the uniq ip from log file
    and stat the number of every ip. I using the dict's inernal method fromkeys() and keys() to get the uniq ip 
'''

from collections import Counter 

def f1(seq):
    return {}.fromkeys(seq).keys()

def f2():
    ip = []
    with open('/tmp/api_access.log') as f:
        lines = f.readlines()
        for l in lines:
            ip.append(l.split(' - - ')[0])
    print "The uniq ip is %s" %  len(f1(ip))

    li = Counter(ip).most_common(3)
    for i in range(len(li)):
        print "The %s found %s "  %  (list(li[i])[0], list(li[i])[1])

if __name__ == '__main__':
    f2()
