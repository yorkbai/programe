#!/usr/bin/env python
# --*-- coding: utf-8  --*--

import sys
import os
import re

def get_file_list(repo, rev):
         """svnlook changed -r REV REPOS 获得发生变更的文件 
         """
         cmd = '%s changed -r %s %s' % ("/usr/bin/svnlook", rev, repo)
         output = os.popen(cmd).read()
         print output.replace('\n','\r\n ')

if __name__ == "__main__":
    get_file_list(sys.argv[1], sys.argv[2])
