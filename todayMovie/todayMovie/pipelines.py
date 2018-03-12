# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time

class TodaymoviePipeline(object):
    def process_item(self, item, spider):
    	now = time.strftime('%T-%m-%d', time.localtime())   #显示当前时间
    	fileName = 'movie' + now + '.txt'
    	with open(fileName, 'a') as fp:
    		fp.write(item['movieName'])
        return item
