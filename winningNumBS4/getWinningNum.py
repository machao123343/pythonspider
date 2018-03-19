#!/usr/bin/evn python
#-*- coding: utf-8 -*-
#

import re
from bs4 import BeautifulSoup
import urllib2
from mylog import MyLog as myLog

class DoubleColorBallItem(object):

	#定义一个需要爬取的结构体集群
	date = None
	order = None
	red1 = None
	red2 = None
	red3 = None
	red4 = None
	red5 = None
	blue = None
	money = None
	firstPrize = None
	secondPrize = None

class GetDoubleColorBallNumber(object):
	'''这个类用于获取双色球中奖号码， 返回一个txt文件'''
	
	def __init__(self):
		self.urls = []
		self.log = mylog()
		self.getUrls()
		self.items = self.spider(self.urls)
		self.pipelines(self.items)

	def getUrls(self):
		URL = r'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
		htmlContent = self.getResponseContent(URL)
		soup = BeautifulSoup(htmlContent, 'lxml')
		tag = soup.find_all(re.compile('p'))[-1]
		pages = tag.strong.get_text()
		for i in xrange(1,int(pages)+1):
			url = r'http://kaijiang.zhcw.com/zhcw/html/ssq/list_' + str(i) + '.html'
			

