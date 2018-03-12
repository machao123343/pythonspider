#-*- coding: utf-8 -*-

__author__ = 'hstking hstking@hotmail.com'

from scrapt.selector import Selector

with open('./superHero.xml','r') as fp:
	body = fp.read()
Selector(text = body).xpath('./*').extract()