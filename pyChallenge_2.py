#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
import string  
import re
import urllib.request


def getHtml(url):
	#�����ҳԴ��
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getStr(html):
	#��Դ���л�ȡ�����ַ���
    reg = r'!--([\s\S]*?)-->'
    
    
    str_re = re.compile(reg)
    html = html.decode('utf-8')  # python3
    str_list = str_re.findall(html)
    return str_list  #����һ��list

    # x = 0
    # for imgurl in imglist:
        # print(imgurl)

html = getHtml("http://www.pythonchallenge.com/pc/def/ocr.html")
	
# print(html)
# print(getStr(html)[1].strip())
#��Դ������ȡ���ַ�������ȥ����β�ո�
strs = getStr(html)[1].strip()
# web = ""
# for i in strs:
	# if i.isalpha():
		# web = web + i
		
# print(web)  #  equality		
# ��������http://blog.csdn.net/weixin_35955795/article/details/52448345
newstr =""

#��ȡ�ַ����а������ַ�����
for i in strs:				
	if not i in newstr:
		newstr = newstr + i

#��ȡÿ���ַ��ĸ���		
for j in newstr:			
	print(j + " : " + str(strs.count(j)))
	

