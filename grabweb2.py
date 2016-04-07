#! /usr/bin/env python
# -*- coding=utf-8 -*-
# @Author pythontab
import sys
import urllib

url = "http://www.baidu.com"
url = sys.argv[1]
html = urllib.urlopen(url).read()
print(html)
file_object = open('thefile.html', 'wb')
file_object.write(html)
file_object.close()
