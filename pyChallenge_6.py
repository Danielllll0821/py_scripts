#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import zipfile

z = zipfile.ZipFile('D:\Script\py_scripts\channel.zip', 'r')
# for i in z.infolist():
# print(i.file_size, i.filename) #返回每个文件的大小和文件名

nothing = '90052'
l = []  # nothing列表
c = []  # comment
s = ''  # 最终字符
try:
    while True:
        print(nothing)
        c.append(z.getinfo(nothing + '.txt').comment)  # 获得每个文件的comment
        l.append(nothing)
        o = z.open(nothing + '.txt', 'r')
        nothing = str(o.read().split()[-1], encoding="utf-8")  # 读取每个文件的内容，并提取按空格划分的最后一个元素

except:
    print(str(z.open(l[-1] + '.txt', 'r').read(), encoding="utf-8"))  # 打开最后一个文件，并读取相应的内容

for i in c:
    s += str(i, encoding="utf-8")
print(s)  # hockey
