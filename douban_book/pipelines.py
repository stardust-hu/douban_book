# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES Settings
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import redis
from pymongo import MongoClient
from douban_book import settings

class DoubanBookPipeline(object):
	def open_spider(self, spider):
		self.file = open(settings.NAME + '.json', 'wb')

	def process_item(self, item, spider):
		# rd = redis.Redis(host='localhost', port=6379, db=1)
		# rd.lpush('book', json.dumps(dict(item)))
		line = json.dumps(dict(item)) + '\n'
		self.file.write(line)
		return item

	def close_spider(self, spider):
		self.file.close()

# from scrapy.conf import settings

class MongodbPipeline(object):
	def open_spider(self, spider):
		self.con = MongoClient(
			host = settings.MONGODB_SERVER,
			port = settings.MONGODB_PORT
			)
		db = self.con[settings.MONGODB_DB]
		self.collection = db[settings.NAME]

	def process_item(self, item, spider):
		self.collection.insert(dict(item))
		return item

	def close_spider(self, spider):
		self.con.close()