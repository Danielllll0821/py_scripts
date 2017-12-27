#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
import string  
import re
import urllib.request


def getHtml(url):
	#获得网页源码
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getStr(html):
	#从源码中获取所需字符串
    reg = r'!--([\s\S]*?)-->'
    
    
    str_re = re.compile(reg)
    html = html.decode('utf-8')  # python3
    str_list = str_re.findall(html)
    return str_list  #返回一个list

    # x = 0
    # for imgurl in imglist:
        # print(imgurl)

html = getHtml("http://www.pythonchallenge.com/pc/def/ocr.html")
	
# print(html)
# print(getStr(html)[1].strip())
strs = getStr(html)[1].strip()
web = ""
for i in strs:
	if i.isalpha():
		web = web + i
	

print(web)
