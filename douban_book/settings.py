# -*- coding: utf-8 -*-

# Scrapy settings for douban_book project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'douban_book'

SPIDER_MODULES = ['douban_book.spiders']
NEWSPIDER_MODULE = 'douban_book.spiders'

USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)'

DOWNLOAD_HANDLERS = {'s3': None}

ITEM_PIPELINES = {
	'douban_book.pipelines.DoubanBookPipeline' : 200,
	# 'douban_book.pipelines.MongodbPipeline' : 100,
}
DOWNLOAD_DELAY = 2
COOKIES_ENABLED = True

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'douban'

NAME = u'机器学习'
