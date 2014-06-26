#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# Script name:  geturl_nologin.py
# Auth: York Bai
# Date: 2014/1/13

''' 
   The script get all urls in special website page (http://jm.gamepaopao.com)
   this script using requests module of python , we need install it first.
   # cd /usr/local/src/python/module
   # curl -OL https://github.com/kennethreitz/requests/zipball/master
   # unzip master
   # cd  kennethreitz-requests-ac4e058 
   # python setup.py install
   then we can using it after import .

'''

import re
import requests

def geturl():
    try:
        # GET source code of webpage
        r = requests.get('http://jm.gamepaopao.com')
        s_code = r.text
        out = open('/tmp/url_record.txt','w')
        out1 = open('/tmp/img_record.txt','w')

        # Get all urls through regex
        link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,s_code)
        for url in link_list:
            if "javaScript" in url or "javascript" in url or '#' in url:
                pass
            else:
                #print url
                out.write(url + '\n')

        
        img_list=re.findall(r'src="(http.+?\.png)"',s_code,re.I)
        for imgurl in img_list:
            out1.write(imgurl + '\n')

    except Exception,e:
        print str(e)

    out.close()
    out1.close()

if __name__ == '__main__':
    geturl()
