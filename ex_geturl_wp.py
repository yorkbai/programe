#!/usr/bin/env python
# --*-- coding: UTF-8 --*--
''' The script get all urls in special website page '''

import urllib
import urllib2
import cookielib
import os
import re

def geturl(url,uid,pwd):
    try:
        status = u"登录"
        cookie=cookielib.CookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        urllib2.install_opener(opener)
        h = urllib2.urlopen(url)

        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:24.0) Gecko/20100101 Firefox/24.0', 'Referer':'http://117.79.156.73:40001/wordpress/wp-login.php'}
        postdata = {'log':uid,'pwd':pwd,'wp-submit':'status','redirect_to':'http://117.79.156.73:40001/wordpress','testcookie':'1'}
        postdata = urllib.urlencode(postdata)

        request = urllib2.Request(url,postdata,headers)
        print request
        out = open('d:\\record.txt','w')
        response = urllib2.urlopen(request)
        text = response.read()
        
        print response.geturl()
        print response.info()

        p=re.compile(r'href=\"signout\"')
        try:
            loginsucce=p.search(text)
            print u"登录成功"
        except:
            print u"好像没有成功登录"

        out.write(text)
        out.close()

    except Exception,e:
        print str(e)

if __name__ == '__main__':
    geturl("http://117.79.156.73:40001/wordpress/wp-login.php",'baiyq','bl1218')
