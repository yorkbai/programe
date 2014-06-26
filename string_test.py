#!/usr/bin/env python
# --*-- coding:utf-8 --*--

def stat2():
    str = raw_input('plz enter a string:')
    letter = 0
    space = 0
    digit = 0 
    other = 0
    for c in str:
        if c.isalpha():
            letter += 1
        elif c.isspace():
            space +=1
        elif c.isdigit():
            digit +=1
        else:
            other += 1
    print "The letter is %s个 ; the space is %s个; the digit is %s个 and other is %s个" %(letter,space,digit,other)


def num1():
    num = int(raw_input('number:'))
    times = int(raw_input('times:'))
    b = num
    sum = 0
    for i in range(0,times):
        if i==times-1:
            print "%d " % (num),   # 用一个逗号结尾就可以禁止输出换行
        else:
            print "%d +" % (num),
        sum += num
        num = num*10+b
    print '= %d' % (sum)    

def split1():
    str = '192.168.0.1'
    print str.split('.')
    print str.split('.',1)
    print str.split('1')
    print str.split('1',2)
    str1,str2 = str.split('.',1)
    print str1,str2



if __name__ == '__main__':
#    stat2()
    num1()
    split1()
