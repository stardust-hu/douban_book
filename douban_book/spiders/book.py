# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from douban_book.items import DoubanBookItem
from douban_book import settings


class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["douban.com"]
    start_urls = [
        'https://book.douban.com/tag/' + settings.NAME
    ]

    def normal(self, s):
    	if s:
    		return s[0]
    	else:
    		return ''

    def parse(self, response):
    	nodes = response.xpath('//li[@class="subject-item"]')
    	for li in nodes:
    		item = DoubanBookItem()
    		item['title'] = self.normal(li.xpath('./div[2]/h2/a/@title').extract())
    		item['author'] = self.normal(li.xpath('.//div[@class="pub"]/text()').extract())
    		item['star'] = self.normal(li.xpath('.//span[@class="rating_nums"]/text()').extract())
    		item['comment'] = self.normal(li.xpath('.//span[@class="pl"]/text()').extract())
    		item['price'] = self.normal(li.xpath('.//span[@class="buy-info"]/a/text()').extract())
    		item['describe'] = self.normal(li.xpath('./div[2]/p/text()').extract())
    		yield item
    	next_page = response.xpath('//link[@rel="next"]/@href').extract()
    	if next_page:
    		next_page = next_page[0]
	    	yield Request('https://book.douban.com' + next_page, callback=self.parse)