#-*- coding:utf-8 -*-


import urllib2
from bs4 import BeautifulSoup
from mylog import MyLog as mylog
import time
import codecs


class Item(object):
	top_num = None
	score = None
	mvName = None
	singer = None
	releaseTime = None

class GetMvList(object):
	def __init__ (self):
		self.urlBase = 'http://vchart.yinyuetai.com/vchart/trends?'
		self.areasDic = {'ML':'Mainland','HT':'Hongkong&Taiwan','US':'Americ','KR':'Korea','JP':'Japan'}
		self.log = mylog()
		self.geturls()

	def geturls(self):
		areas = ['MT', 'HT', 'US', 'KR', 'JP']

		pages = [str(i) for i in range(1,3)]
		for area in areas:
			urls = []
			for page in pages:
				urlEnd = 'area=' + area + '&page=' + page
				url = self.urlBase + urlEnd
				urls.append(url)
				self.log.info(u'添加URL:%s 到URLS' %url)
			self.spider(area, urls)

	def getResponseContent(self, url):
		request = urllib2.Request(url.encode('utf8'))
		try:
			response = urllib2.urlopen(request)
			time.sleep(1)#挂起进程的时间
		except:
			self.log.error(u'Python 返回URL: %s 数据失败' %url)
			return ''
		else:
			self.log.info(u'Python 返回URL: %s 数据成功' %url)
			return response.read()

	def spider(self, area, urls):
		items = []
		for url in urls:
			responseContent = self.getResponseContent(url)
			if not responseContent:
				continue     #如果响应值为空则跳过本次循环
			soup = BeautifulSoup(responseContent, 'lxml')
			tags = soup.find_all('li', attrs = {'name':'dmvLi'})
			for tag in tags:
				item = Item()
				try :
					item.top_num = tag.find('div', attrs = {'class':'top_num'}).get_text()
					if tag.find('h3', attrs = {'class': 'desc_score'}):
						item.score = tag.find('h3', attrs = {'class':'desc_score'}).get_test()
					else:
						item.score = tag.find('h3', attrs = {'class':'asc_score'}).get_text()

						item.mvName = tag.find('img').get('alt')
					item.singer = tag.find('a', attrs = {'class':'special'}).get_text()
					item.releaseTime = tag.find('p', attrs = {'class':'c9'}).get_text()
					items.append(item)
				except:
					self.log.error(u'添加mvName为<<%s>>的数据失败' %(item.mvName))
				else:
					self.log.info(u'添加mvName为<<%s>>的数据成功' %(item.mvName))
		self.pipelines(items, area)

	def pipelines(self, items, area):
		fileName = 'mvTopList.txt'
		nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
		with codecs.open(fileName, 'a', 'utf8') as fp:
			fp.write('%s -------%s\r\n' %(self.areasDic.get(area), nowTime))
			for item in items:
				fp.write('%s %s \t %s \t %s \t %s \r\n' 
						%(item.top_num, item.score, item.releaseTime, item.singer, item.mvName))
				self.log.info(u'添加mvName为<<%s>>的MV到%s...' %(item.mvName, fileName))
			fp.write('\r\n'*4)

if __name__ == '__main__':
	GML = GetMvList()

