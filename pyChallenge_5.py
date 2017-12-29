#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import pickle
import urllib.request


# https://www.cnblogs.com/gengcx/p/7331120.html

def getHtml(url):
    # 获得网页源码
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


html = getHtml("http://www.pythonchallenge.com/pc/def/banner.p")  # 二进制文件
# html = html.decode('utf-8')  #转为utf-8格式

# -----------------------------------------------------------
# #print(html)
# with open('D:\Script\py_scripts\py5.pickle', 'w') as f:
# f.write(html)

# f.close()


# f = open('D:\Script\py_scripts\py5.pickle','rb')

# strs = pickle.load(f)

# print(strs)
# -----------------------------------------------------------

# p = pickle.dumps(html)
strs = pickle.loads(html)  # 将二进制文件直接反序列化,得到一个二维列表
# print(strs)


s = ''
for i in strs:
    for j in i:
        s += j[0] * j[1]
    # print(j)
    s += '\n'
print(s)
