#!/usr/bin/evn python
#-*- coding: utf-8 -*-
#

import re
from bs4 import BeautifulSoup
import urllib2
from mylog import MyLog as mylog
from save2excel import SavaBallDate

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
		self.returnResult(self.items)
		self.pipelines(self.items)

	def getUrls(self):
		URL = r'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
		htmlContent = self.getResponseContent(URL)
		soup = BeautifulSoup(htmlContent, 'lxml')
		tag = soup.find_all(re.compile('p'))[-1]
		pages = tag.strong.get_text()
		for i in xrange(1,3):
			url = r'http://kaijiang.zhcw.com/zhcw/html/ssq/list_' + str(i) + '.html'
			self.urls.append(url)
			self.log.info(u'添加URL:%s 到URLS \s\n' %url)

	def returnResult(self, items):
		try:
			self.items = self.spider(self.urls)
			SavaBallDate(self.items)
		except:
			self.log.error(u'存入excel失败')
		else:
			self.log.info(u'存入excel成功')

	def getResponseContent(self, url):
		try:
			response = urllib2.urlopen(url.encode('utf-8'))
		except:
			self.log.error(u'Python 返回URL:%s 失败 \r\n' %url)
		else:
			self.log.info(u'Python 返回URL:%s 成功 \r\n' %url)
			return response.read()

	def spider(self, urls):

		items = []
		for url in urls:
			htmlContent = self.getResponseContent(url)
			soup = BeautifulSoup(htmlContent, 'lxml')
			tags = soup.find_all('tr', attrs = {})
			for tag in tags:
				if tag.find('em'):
					item = DoubleColorBallItem()
					tagTd = tag.find_all('td')
					item.date = tagTd[0].get_text()
					item.order = tagTd[1].get_text()
					tagEm = tagTd[2].find_all('em')
					item.red1 = tagEm[0].get_text()
					item.red2 = tagEm[1].get_text()
					item.red3 = tagEm[2].get_text()
					item.red4 = tagEm[3].get_text()
					item.red5 = tagEm[4].get_text()
					item.red6 = tagEm[5].get_text()
					item.blue = tagEm[6].get_text()
					item.money = tagTd[3].find('strong').get_text()
					item.firstPrize = tagTd[4].find('strong').get_text()
					item.secondPrize = tagTd[5].find('strong').get_text()
					items.append(item)
					#结构体数组追加
					self.log.info(u'获取日期为:%s 的数据成功' %(item.date))
		return items

	def pipelines(self, items):
		fileName = u'双色球.txt'.encode('GBK')
		with open(fileName, 'w') as fp:
			for item in items:
				fp.write('%s %s \t %s %s %s %s %s %s  %s \t %s \t %s %s \n'
					%(item.date,item.order,item.red1,item.red2,item.red3,item.red4,item.red5,item.red6,item.blue,item.money,item.firstPrize,item.secondPrize))

if __name__ == '__main__':
	GDCBN = GetDoubleColorBallNumber()



