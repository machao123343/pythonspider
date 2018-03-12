#-*- coding: utf-8 -*-

__author__ = 'hstking hstking@hotmail.com'

import urllib2
import sys
import re

def teseArgument():
  	if len(sys,argv) != 2:
 	 	print(u"只需要一个参数就够了")
  		tipUse()
 		exit()
	else:
  		TP = TestProxy(sys,argv[1])

def tipUse():
	print(u'该程序只能由一个参数， 这个参数2必须是一个可用的proxy')
	print(u"usage: python testUrllib2WithProxy.py http://1.2.3.4.5")
	print(u"usage: python testUrllib2WithProxy.py https://1.2.3.4.5")

class TestProxy(object):
	def __init__(self,proxy):
		self.proxy = proxy
		self.checkProxyFormat(self.proxy)
		self.url = 'http://www.baidu.com'
		self.timeout = 5
		self.flagWord = '百度'
		self.useProxy(self.proxy)

	def checkProxyFormat(self,proxy):
		try:
			proxyMatch = re.compile('http[s]?://[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}:[\d]{1,5}$')
			re.search(proxyMatch,proxy).group()  #找寻匹配的代理url
		except AttributeError:
			tipUse()
			exit()
		flag = 1
		proxy = proxy.replace('//','')
		try:
			protocol = proxy.split(':')[0]
			ip = proxy.split(':')[1]
			port = proxy.split(':')[2]
		except IndexError:
			print(u'下标出界')
			tipUse()
			exit()
		flag = flag and len(proxy.split(':')) == 3 and len(ip.split('.')) == 4
		flag = ip.split('.')[0] in map(str,xrange(1,256)) and flag
		flag = ip.split('.')[1] in map(str,xrange(256)) and flag
		flag = ip.split('.')[2] in map(str,xrange(256)) and flag
		flag = ip.split('.')[3] in map(str,xrange(1,255)) and flag
		flag = protocol in [u'http',u'https'] and flag
		flag = port in map(str,range(1,65535)) and flag
        if flag:
        	print(u'输入的http代理服务器符合标准')
        else:
        	tipUse()
        	exit()

	def useProxy(self,proxy):
		protocol = proxy.split('//')[0].replace(':','')
		ip = proxy.split('//')[1]
		opener = urllib2.build_opener(urllib2.ProxyHandler({protocol:ip}))
		urllib2.install_opener(opener)
		try:
			response = urllib2.urlopen(self.url,timeout = self.timeout)
		except:
			print(u'连接错误，退出程序')
			exit()
		str = response.read()
		if re.search(self.flagWord,str):
			print(u'已取得特征词，该代理可用')
		else:
			print(u'该代理不可用')

if __name__ == '__main__':
	testArgument()	


