#!/usr/bin/env python
#--*-- coding: utf-8 --*--


def splitnum():
    num = int(raw_input('plz enter the number that needed split:'))
    while(num != 1):
        for i in range(2,num+1):
            if num%i == 0:
                num = num/i
                if (num == 1):
                    print '%d' % i
                else:
                    print '%d * ' % i,
                    break
            
        
        

if __name__ == '__main__':
    splitnum()
