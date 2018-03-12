#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstkong hstking@hotmail.com'

import re
import urllib2

class TodayMovie(object):
	def __init__(self):
		self.url = 'http://www.jycinema.com/html/default/schedule'
		self.timeout = 5
		self.fileName = './todayMovie.txt'
		self.getMovieInfo()

	def getMovieInfo(self):
		response = urllib2.urlopen(self.url,timeout = self.timeout)
		movieList = re.findall('film_title.*', response.read())
		with open(self.fileName, 'w') as fp:
			for movie in movieList:
				movie = self.subStr(movie)
				print(movie.decode('utf-8'))
				fp.write(movie + '\n')

	def subStr(self, st):
		st = st.replace('film-tltle">','')
		st = st.replace('</h3>','')
		return st

if __name__ == '__main__':
	tm = TodayMovie()
