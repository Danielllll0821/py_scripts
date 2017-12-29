#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string

word = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# Newword = ""
# for i in word:
# if i.isalpha():
# if  ord(i) == 121:
# I = chr(97)
# elif ord(i) == 122:
# I = chr(98)
# else:
# I = chr(ord(i) + 2)

# else:
# I = i

# Newword = Newword + I

# print (string.ascii_letters)
# print (string.ascii_lowercase)
# print (string.ascii_uppercase)
# print (string.ascii_lowercase[2:])
# print (string.ascii_lowercase[:2])
# print (string.ascii_lowercase[2:] + string.ascii_lowercase[:2]) #生成新的小写字母表 

s = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
Newword = word.translate(s)

print(Newword)
