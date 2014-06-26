#!/usr/bin/env python
# --*-- coding:utf-8 --*--

def grade():
    score = int(raw_input('plz enter the score of student:'))
    if score >= 90:
        print 'A'
    elif  60<= score <=89:
        print 'B'
    elif  0< score <=59:
        print 'C'
    else:
        print 'the score should  between 0 and 100'
    print score

def pr():
    a = [1,2,3,4]
    if 1 in a:
        print "The list include %s" % 1


if __name__ == '__main__':
    #grade()
    pr()
