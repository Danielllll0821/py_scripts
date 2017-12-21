from telnetlib import Telnet


tn = Telnet('134.224.1.10', 23)
tn.read_until(b'Username:')
tn.write(b'cisco')
print(tn.read_all())
tn.write(b'\n')
tn.read_until(b'word')
tn.write(b'cisco@123')
tn.write(b'\n')
tn.read_until(b'>')
tn.write(b'show ver')
tn.write(b'\n')

