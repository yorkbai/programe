#!/usr/bin/env python
# --*-- coding: utf-8 --*--


def shoot():
    people = range(1,101)
    print 'people being shoot.....'
    print people
    while len(people)  != 1:
        people = people[1::2]
        print people
    print "The last people living is number: %s" % people[0]

if __name__ == '__main__':
    shoot()
