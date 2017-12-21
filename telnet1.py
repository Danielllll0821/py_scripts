# -*- coding: utf-8 -*-   

from telnetlib import Telnet
import telnetlib
  
'''''Telnet远程登录：Windows客户端连接Linux服务器'''  
  
# 配置选项  
Host = '134.224.1.10' # Telnet服务器IP  
username = "cisco"   # 登录用户名
password = "cisco@123"  # 登录密码
finish = '>'      # 命令提示符（标识着上一条命令已执行完毕）  
  
# 连接Telnet服务器  
tn = telnetlib.Telnet(Host)  

print(str(username))
print(str(password))
# 输入登录用户名
tn.read_until(b'Username:')
tn.write(b'cisco\n')


# 输入登录密码
tn.read_until(b'Password:')
tn.write(b'cisco@123\n')
print(tn.read_all())
# 登录完毕后，执行ls命令
tn.read_until(b'finish')
tn.write('show privilege' + '\r\n')
print(tn.read_all())
# ls命令执行完毕后，终止Telnet连接（或输入exit退出）
tn.read_until(finish)
tn.close() # tn.write('exit\n')
