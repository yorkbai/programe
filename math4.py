#!/usr/bin/python
#-*- coding:utf-8 -*-

from sys import stdout
from math import sqrt 

def sushu():
    for i in range(101,201):
        flag = 1
        k = int(sqrt(i))
        for j in range(2,k+1):
            if i%j == 0:
                flag = 0
                break
        if flag == 1:
            print '%5d' % (i),

def yinzishu():
    n = int(raw_input("input number:\n"))
    print "n = %d" % n

    for i in range(2,n + 1):
        while n != i:
            if n % i == 0:
                 stdout.write(str(i))
                 stdout.write("*")
                 n = n / i
            else:
                break
    print "%d" % n

if __name__ == "__main__":
    sushu()
    yinzishu()
