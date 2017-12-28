#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pyChallenge4.0.py
import string  
import re
import urllib.request


def getHtml(url):
	#获得网页源码
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getStr(html):
	#从源码中获取所需字符串 http://www.jb51.net/article/20654.htm
    reg = r'nothing=([\s\S]*?)"'		        
    str_re = re.compile(reg)
    html = html.decode('utf-8')  # python3
    str_list = str_re.findall(html)
    return str_list  #返回一个list

html = getHtml("http://www.pythonchallenge.com/pc/def/linkedlist.php")
print(getStr(html)[0])
