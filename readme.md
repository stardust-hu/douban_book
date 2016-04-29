#豆瓣图书信息爬取

练习使用scrapy框架

> 主要信息包括：书名、作者、价格、简介、评论数、星级

> 默认输出json文件

###使用

该程序暂使用标签搜索，在**setting.py**文件中设置**NAME**属性来获取某一类图书

e.g:

    NAME = u'机器学习'

开始抓取：

    scrapy crawl book

    scrapy crawl book -o 机器学习.csv #输出为csv文件

**由于采集的是原始数据，未能将价格、评论数提取为数字**