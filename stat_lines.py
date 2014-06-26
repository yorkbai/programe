#!/usr/bin/env python
# --*-- coding: utf-8 --*--
''' 一行语句统计文件行数  
    第一种方法简捷但在文件较大时可能会不工作，建议使用第二种
'''

def count1(path):
    
    thefilepath = path
    count = len(open(thefilepath,'rU').readlines())
    print count

def count2(path):
    thefilepath = path
    Count = 0
    for count,line in enumerate(open(thefilepath,'rU')):
        pass
        Count += 1
    print Count

if __name__ == '__main__':
    count1("/usr/local/src/mydoc/secure.txt")
    count2("/usr/local/src/mydoc/secure.txt")
