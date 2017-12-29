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
    reg = r'nothing=([\s\S]*?)"'
    str_re = re.compile(reg)
    html = html.decode('utf-8')  # python3
    str_list = str_re.findall(html)
    # return str_list  #返回一个list
    # url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(str_list[0])
    return str_list[0]


url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

html = getHtml(url)
codes = getStr(html)

print(url + '?nothing=' + codes)
url = url + '?nothing=' + codes

i = 0
while i < 510:
    print(i)
    html = getHtml(url)
    html = html.decode('utf-8')
    print(html)
    strlist = html.split()
    numbers = strlist[5]
    # print(html.split()[5])
    print(numbers)
    i = i + 1
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + numbers
    print(url)

# peak.html
