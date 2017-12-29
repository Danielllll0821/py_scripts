#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import urllib.request
import re


def getHtml(url):
    # 获得网页源码
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getStr(html):
    # 从源码中获取所需字符串 http://www.jb51.net/article/20654.htm
    reg = r'img src="(.*?)"'
    str_re = re.compile(reg)
    html = html.decode('utf-8')  # python3
    str_list = str_re.findall(html)
    return str_list  # 返回一个list

    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jpeg' % x)
        x = x + 1


html = getHtml("http://www.pythonchallenge.com/pc/def/oxygen.html")  # 二进制文件

print(getStr(html))
