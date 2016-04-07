#! /usr/bin/env python
import sys
import urllib.request

url = sys.argv[1]
webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'} 
req = urllib.request.Request(url=url, headers=webheader)  
html = urllib.request.urlopen(req).read()
print(html)
file_object = open('thefile.html', 'wb')
file_object.write(html)
file_object.close()
