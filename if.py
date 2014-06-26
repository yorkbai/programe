#!/usr/bin/env python
# --*-- coding: utf-8 --*--
''' This is comment for if statment.

    if statment not need'''


def fib(n):
    print 'n = %s' %  n 
    if(n > 1 ):
        return n*fib(n-1)
    else:
        print 'end of the lines'
        return 1
    if 1 >  0:
        print 'ok'
    else:
        print 'fail'

def if2():
    num = int(raw_input("Enter num:"))
    print num

def str_convert():
    a = ['1','2','3']
    s = ' '.join(a)
    print s
    print type(s)
    s1 = 'Hello world!'
    l = s1.split()
    print l

    list1=[1,2,3]
    s2 = ' '.join(str(e) for e in list1)
    s3 = " ".join(str(e) for e in list1)
    print s2 
    print s3 
    print type(s2)

if __name__ == '__main__':
    #str_convert()
    print fib(5) 
    #print if2()
    #print __doc__
    #print fib.__doc__
