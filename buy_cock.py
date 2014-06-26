#!/usr/bin/env python
# --*-- coding: utf-8 --*--
''' one hundred yuan buy cock,hen,chick one huandred all'''

def Buy():
    cock_price,hen_price,chick_price = 5,3,1.0/3
    cock_Max,hen_Max,chick_Max = range(100/cock_price)[1:],range(100/hen_price)[1:],range(int(100/chick_price))[1:]
    items=[(cock,hen,chick) for cock in cock_Max for hen in hen_Max[1:] for chick in chick_Max[1:]  if int(cock*cock_price+hen*hen_price+chick*chick_price) == 100 and chick%3 == 0 and cock+hen+chick == 100]
    #for i in range(0,len(items)):
    #    print "cock:%s ,hen:%s,chick:%s"  % (items[int(i)][0], items[int(i)][1],items[int(i)][2])
    for j in items:
        print "%5s%10s%15s" % j

if __name__ == '__main__':
    Buy()
