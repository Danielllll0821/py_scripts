#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pyChallenge_3.py
#  

import string
import re
import urllib.request


def getHtml(url):
    # 获得网页源码
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getStr(html):
    # 从源码中获取所需字符串 http://www.jb51.net/article/20654.htm
    reg = r'!--([\s\S]*?)-->'

    str_re = re.compile(reg)
    html = html.decode('utf-8')  # python3
    str_list = str_re.findall(html)
    return str_list  # 返回一个list


html = getHtml("http://www.pythonchallenge.com/pc/def/equality.html")

# print(html)
# print(getStr(html)[0].strip())
# 从源码中提取的字符串，并去掉首尾空格
strs = getStr(html)[0].strip()

# 获取新字符
# AAAbCCC 
# aBBBcDDDe 字符格式
newreg = r'[a-z]{1}[A-Z]{3}[a-z][A-Z]{3}[a-z]{1}'
newstr_re = re.compile(newreg)
newstr_list = newstr_re.findall(strs)
print(newstr_list)

web = ""
for i in newstr_list:
    web = web + i[4]
print(web)  # linkedlist  http://www.pythonchallenge.com/pc/def/linkedlist.html
