#!/usr/bin/env python
# -*- coding:utf-8 -*-


import fileinput
from glob import glob

def stat_character():
    for line in fileinput.input(glob('/tmp/1.log')):
        print fileinput.lineno(), u'文件:', fileinput.filename(), u'行号:', fileinput.filelineno(), u'长度:', len(line.strip('/n'))
        fileinput.close()

if __name__ == '__main__':
    stat_character()
