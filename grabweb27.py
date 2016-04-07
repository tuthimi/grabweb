#! /usr/bin/env python
import sys
import urllib2

url = sys.argv[1]
webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100311 Firefox/23.0'} 
req = urllib2.Request(url=url, headers=webheader)  
html = urllib2.urlopen(req).read()
#print(html)
file_object = open('web.html', 'wb')
file_object.write(html)
file_object.close()
print("done")
