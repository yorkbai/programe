#!/usr/bin/env python


def sum():
    a = xrange(101)
    b = range(1,101)

    list = [ num for num in xrange(1,100) if num%3 == 0 or num%5 == 0]
    print list

    sum = 0
    for i in list:
        sum = sum + i

    print  sum


if __name__ == '__main__':
   sum()
