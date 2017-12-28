#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import pickle
import urllib.request
# https://www.cnblogs.com/gengcx/p/7331120.html

def getHtml(url):
	#»ñµÃÍøÒ³Ô´Âë
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://www.pythonchallenge.com/pc/def/banner.p")
html = html.decode('utf-8')
#print(html)
with open('D:\Script\py_scripts\py5.pickle', 'w') as f:
	f.write(html)

	f.close()


f = open('D:\Script\py_scripts\py5.pickle','rb')

strs = pickle.load(f)

print(strs)
