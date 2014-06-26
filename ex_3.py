#!/usr/bin/env python
# --*-- coding:utf-8 --*--
'''This ex is very useful for us.

    include dict ,string ,method ,comments etc'''


def connect(params):
    return ";".join(["%s=%s"  %  (k,v) for k,v in params.items()])


print "the type of range() is %s " %  type(range(1,101))
for i in range(1,101) :
    print "the range method result is a list elem is  %s" %  i

print "the type of xrange() is %s " %  type(xrange(1,101))
for j in xrange(1,101) :
    print  " the xrange method result is a xrange object ! is %s" % j

if __name__ == ' __main__':
    myparams = {'a':1,'b':2,'c':3}
    #print connect(myparams)
    diff()
