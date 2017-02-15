# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BbccrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = scrapy.Field()
    Type = scrapy.Field()
    Refer = scrapy.Field()
    Pubtime = scrapy.Field()
    Summary = scrapy.Field()
    Content = scrapy.Field()


class BbccrawlURLItem(scrapy.Item):
    Title = scrapy.Field()
    URL = scrapy.Field()
