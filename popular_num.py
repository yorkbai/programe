#!/usr/bin/env python

from collections import Counter

def stat1():
    list = [1,3,5,8,11,33,1,1,2,88,3,5,5,5]
    dict ={}
    for word in list:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    print dict
    new_list = sorted(dict,key=dict.get,reverse=True)
    print new_list
    print "The third popular item is %s" %  sorted(dict,key=dict.get,reverse=True)[:3]

def stat2():
    list = [1,3,5,8,11,33,2,88,3,5,5,5]
    c=Counter(list)
    print c.most_common(3)

def sort1():
    info = {'1':'first','2':'second','3':'third'}
    number = raw_input('input type you number:')
    print info.get(number,'error')

if __name__ == '__main__':
    stat1()
#    stat2()
#    sort1()
   

