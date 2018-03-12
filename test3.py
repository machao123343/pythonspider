#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import urllib2
import userAgents
'''userAgents.py是个自定义的模块，位置处于当前目录下 '''

class Urllib2ModifyHeader(object):
	'''使用urllib2模块修改header '''
	def __init__(self):
		#这个是PC + IE 的User-Agent
		PIUA = userAgents.pcUserAgent.get('IE 9.0')
		#这个是Mobile + UC的User-Agent
		MUUA = userAgents.mobileUserAgent.get('Android QQ')
		#测试用的网站选择的是有道翻译
		self.url = 'http://www.baidu.com'

		self.useUserAgent(PIUA,1)
		self.useUserAgent(MUUA,2)

	def useUserAgent(self,userAgent,name):
		request = urllib2.Request(self.url)
		request.add_header(userAgent.split(':')[0],userAgent.split(':')[1])
		response = urllib2.urlopen(request)
		fileName = str(name) + '.html'
		with open(fileName,'a') as fp:
			fp.write("%s\n\n" %userAgent)
			fp.write(response.read())

if __name__ == '__main__':
	umh = Urllib2ModifyHeader()
