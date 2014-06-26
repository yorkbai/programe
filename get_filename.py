#!/usr/bin/python

import os

filenames=os.listdir(os.getcwd())
print filenames
for name in filenames:
	filenames[filenames.index(name)]=name.split('.', 1)[0] # get file name
#	filenames[filenames.index(name)]=name.split('.', 1)[1]  
#	filenames[filenames.index(name)]=name.split('.')[-1]  # get file type
out=open('names.txt','w')
for name in filenames:
  	out.write(name+'\n')
out.close()
