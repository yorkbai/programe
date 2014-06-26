#!/usr/bin/env python
# --*-- coding: utf-8 --*--
'''  "zz" method for get the last three number of 13*13*....*13( 20times), 即13的20次方

    "zz1" method for print number from 1-100, if the number is 3 ,instead of 'fizz',if
    the number is 5, instead of 'buzz' , if it's  3&5 , instead of 'fizzbuzz'

    对于and，当计算a and b时，python会计算a，如果a为假，则取a值，如果a为真，则python会计算b且整个表达式会取b值。对于or，

    当计算a or b时，python会计算a，如果a为真，则整个表达式取a值，如果a为假，表达式将取b值。
    对于not，not将反转表表达式的“实际值”，如果表达式为真，not为返回假，如为表达式为假，not为返回真。

'''

def zz(a,n):
    i = a**n
    print i
    return str(i)[-3:]

def zz1():
   
    for x in range(1,101):
        print "fizz"[x%3*len('fizz')::]+"buzz"[x%5*len('buzz')::] or x   #注意复合表达式的运用（a and b  a or b  a not b)
        #print x and "fizz"[x%3*len('fizz')::]+"buzz"[x%5*len('buzz')::] 

def zz2():
    str1=[x+y for x in 'ABCDEFGHIJKLMEOPQRSTUVWXYZ' for y in '1234567890']
    print str1

def feb():
    a,b = 0,1
    while b < 20:
        print b
        a,b = b,a+b


if __name__ == '__main__':
    print zz(13,20)
    zz1()
    zz2()
    feb()
