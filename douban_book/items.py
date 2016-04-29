# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DoubanBookItem(Item):
	title = Field()
	author = Field()
	star = Field()
	comment = Field()
	price = Field()
	describe = Field()
