#!/usr/bin/env python

import math

def flower():
    for i in xrange(100,1000):
        a = i%10
        b = i/100
        c = int(i/10)%10
        if i == a**3 + b**3 + c**3:
            print i

def sqrt1():
    for i in range(1000):
        x = int(math.sqrt(i+100))
        y = int(math.sqrt(i+268))
        if (x*x == i+100) and (y*y == i+268):
            print i

if __name__ == '__main__':
    flower()
    sqrt1()
