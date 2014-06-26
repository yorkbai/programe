#!/usr/bin/env python
# --*-- coding:utf-8 --*--
''' The script get all urls in special website page '''

import urllib
import urllib2
import cookielib
import os
import re

def geturl(url,uid,pwd):
    try:
       # posturl = "http://myvps.com:4440/user/j_security_check"

        cookie=cookielib.CookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        urllib2.install_opener(opener)
        h = urllib2.urlopen(url)

        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:24.0) Gecko/20100101 Firefox/24.0', 'Referer':'http://localhost:4440/user/login'}
        postdata = {'j_username':uid,'j_password':pwd}
        postdata = urllib.urlencode(postdata)

        request = urllib2.Request(url,postdata,headers)
        print request
        out = open('/tmp/record.txt','w')
        response = urllib2.urlopen(request)
        text = response.read()

        link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,text)
        for url in link_list:
            print url
        out.write(text)
        out.close()

    except Exception,e:
        print str(e)

#    print text

if __name__ == '__main__':
    geturl("http://localhost:4440/user/j_security_check",'baiyq','baiyq_mzq_bl991218')
