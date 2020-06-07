# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MafengwoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class SightItem(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()
    city_id = scrapy.Field()
    city_name = scrapy.Field()

    location=scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()

    introduction=scrapy.Field()
    phone=scrapy.Field()
    site=scrapy.Field()
    time=scrapy.Field()

    transportation=scrapy.Field()
    tickets=scrapy.Field()
    open_time=scrapy.Field()

    images_urls=scrapy.Field()
    images_num=scrapy.Field()
    comments_num=scrapy.Field()
