word = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

Newword = ""
for i in word:
	if i.isalpha():
		if  ord(i) == 121:
			I = chr(97)
		elif ord(i) == 122:
			I = chr(98)
		else:	
			I = chr(ord(i) + 2)
		
	else:
		I = i
		
	Newword = Newword + I
	
	
	
print(Newword)
