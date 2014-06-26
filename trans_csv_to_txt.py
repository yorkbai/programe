#!/usr/bin/python
# Scripts Name:  trans_csv_to_txt.py
# Date: 2014/4/17
# Author: YorkBai
# --*-- coding: uft-8 --*--
''' This scritps to translate csv to txt . '''

import sys,os,csv,string
from os import linesep


def hex2dec(string_num):
    return str(int(string_num.lower(), 16))

def main():    
    if len(sys.argv) < 3:
        print "Usage: python trans_csv_to_txt.py inputfile outputfile"
        sys.exit()

    source = sys.argv[1]
    des = sys.argv[2]
    try:
        ifile  = open(source, "rb")
        reader = csv.reader(ifile)
        ofile  = open(des, "wb")

        for row in reader:
            if  reader.line_num == 1:
                continue
            #tmp1= string.atoi(hex2dec(row[5])) + string.atoi(hex2dec(row[6])) + string.atoi(hex2dec(row[7]))
            #tmp2 = str(tmp1)
            tmp1= hex2dec(row[5]) + hex2dec(row[6]) + hex2dec(row[7])
            del row[6:8]
            row[5]=tmp1.zfill(6)
            str_convert = '^a'.join(row)
            ofile.write(str_convert + '\n')
    except Exception,e:
        sys.exit() 
    finally:    
        ifile.close()
        ofile.close()

if __name__ == "__main__":    
    main()
