#!/usr/bin/env python
# --*-- coding:utf-8 --*--
''' test script for file operater'''

import os

def Stat_alllines():
    path=os.getcwd()
    filelist = os.listdir(os.getcwd())
    allline = 0 
    for file in filelist:
        if os.path.isdir(file):
            continue
        else:
            fileHandle = open(file,'r')
            lineno = len(fileHandle.readlines())
            allline += lineno
    print allline
        
    fileHandle.close()
        
    #fileHandle=open(filelist[len(filelist)-1])
    #num = 0
    
    #for content in fileHandle.readlines():
    #    if 'glob' in content:
    #        print content
    #        num += 1
    #print num

    #for (num,content) in enumerate(fileHandle):
    #    if 'glob' in content:
    #        print num,content
    #        allnum += 1
    #print allnum
    

    #print fileHandle.readlines()[5:]
    #for line in fileHandle.readlines()[4:12]:
    #    print line 

def file1():
    print 'plz input filename:'
    raw = raw_input()
    if os.path.isdir(raw):
        print 'your input is directory,plz input filename that being stat'
        return 
    if os.path.isfile(raw):
        fileHandle = open(raw,'rb')
        charno = len(fileHandle.read())
        lineno = len(fileHandle.readlines())
        print 'the file include %s character' % charno 
        print 'the file include %s line' % lineno

    

    fileHandle.close()


if __name__ == '__main__':
    Stat_alllines()
    #file1()

