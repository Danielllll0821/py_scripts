# -*- coding: utf-8 -*-
import subprocess
import re

def getPING(domain):
    # 调用系统自带的ping.exe实现PING domain，返回值为：ip,丢包率,最短，最长，平均
    p = subprocess.Popen(["ping.exe", domain], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out = p.stdout.read().decode('gbk')
    # Pinging www.a.shifen.com [115.239.211.112] with 32 bytes of data
    regIP = r'\d+\.\d+\.\d+\.\d+'
    # Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)   数据包: 已发送 = 4，已接收 = 4，丢失 = 0 (0% 丢失)，
    regLost = r'\(\d+%'
    # Minimum = 37ms, Maximum = 38ms, Average = 37ms   最短 = 37ms，最长 = 77ms，平均 = 48ms
    regMinimum = u'Minimum = \d+ms|最短 = \d+ms'
    regMaximum = u'Maximum = \d+ms|最长 = \d+ms'
    regAverage = u'Average = \d+ms|平均 = \d+ms'
    ip = re.search(regIP, out)
    lost = re.search(regLost, out)
    minimum = re.search(regMinimum, out)
    maximum = re.search(regMaximum, out)
    average = re.search(regAverage, out)
    if ip:
        ip = ip.group()[1:-1]
    if lost:
        lost = lost.group()[1:]
    if minimum:
        minimum = filter(lambda x: x.isdigit(), minimum.group())
    if maximum:
        maximum = filter(lambda x: x.isdigit(), maximum.group())
    if average:
        average = filter(lambda x: x.isdigit(), average.group())
    return ip.encode('raw_unicode_escape'), lost.encode('raw_unicode_escape'), minimum.encode('raw_unicode_escape'), maximum.encode('raw_unicode_escape') , average.encode('raw_unicode_escape')

if __name__ == '__main__':
    ping_result = getPING('www.baidu.com')
    print ping_result
