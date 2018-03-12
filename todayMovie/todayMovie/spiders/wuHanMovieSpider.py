# -*- coding: utf-8 -*-
import scrapy
from todayMovie.items import TodaymovieItem


class WuhanmovieSpider(scrapy.Spider):
    name = 'wuHanMovieSpider'
    allowed_domains = ['jycinema.com']
    start_urls = ('http://www.jycinema.com/html/default/bbs/film_detail.html?id=1643')

    def parse(self, response):
        subSelector = response.xpath('//meta[@name="description"]')

        item = TodaymovieItem()
        item['movieName'] = subSelector


    	return item

