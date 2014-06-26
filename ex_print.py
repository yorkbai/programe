#!/usr/bin/env python
''' This script for print image through *'''

def print_image(n,c):
    print ' '*(n-1) + c
    for x in xrange(2,20):
        print ' '*(n-x) + c + ' '*(2*x-3) + c
    print (c+' ')*n

def print_1():
    name = 'Zed A. Shaw'
    age = 35 # not a lie
    height = 74 # inches
    weight = 180 # lbs
    eyes = 'Blue'
    teeth = 'White'
    hair = 'Brown'

    print "Let's talk about %s." % name
    print "He's %d inches tall." % height
    print "He's %d pounds heavy." % weight
    print "Actually that's not too heavy."
    print "He's got %s eyes and %s hair." % (eyes, hair)
    print "His teeth are usually %s depending on the coffee." % teeth

    # this line is tricky, try to get it exactly right
    print "If I add %d, %d, and %d I get %d." % ( age, height, weight, age + height + weight)

def print_2():
    test = """hello,\nworld"""
    print "this is test1: %s" %test
    print "this is test2: %r" %test

if __name__ == '__main__':
    print_image(20,'+')
    print_1()
    print_2()
