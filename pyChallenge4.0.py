#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pyChallenge4.0.py
import string  
import re
import urllib.request


def getHtml(url):
	#�����ҳԴ��
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getStr(html):
	#��Դ���л�ȡ�����ַ��� http://www.jb51.net/article/20654.htm
    reg = r'nothing=([\s\S]*?)"'		        
    str_re = re.compile(reg)
    html = html.decode('utf-8')  # python3
    str_list = str_re.findall(html)
    return str_list  #����һ��list

html = getHtml("http://www.pythonchallenge.com/pc/def/linkedlist.php")
print(getStr(html)[0])
