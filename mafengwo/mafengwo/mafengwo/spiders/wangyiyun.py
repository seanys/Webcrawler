import scrapy
import re
import bs4
import json
import random
import pymysql

class PathSpider(scrapy.Spider):
    name = "lyric"

    first_load=True

    current_id=39
    current_place="南京"
    
    start_urls = [
        "https://music.163.com/#/playlist?id=2332351054&userid=304626995"
    ]

    custom_settings = {
        "origin": "https://www.mafengwo.cn",
    }
    
    def parse(self, response):
        print("开始执行")
        # print(response.xpath("//div[@id='lyric-content']").extract())
        print(response.xpath("//html").extract())
        # while self.current_id<=50:
        #     while page_id<=300:
        #         yield scrapy.Request(
        #             "http://www.mafengwo.cn/gonglve/ajax.php?act=get_travellist&pageid=mdd_index&sort=1&cost=0&days=0&month=0&tagid=0&mddid={}&page={}".
        #             format(city_id,page_id),
        #             callback=self.parse_dests,
        #             meta={
        #                 "current_place": self.current_place
        #             }
        #         )
        #         page_id=page_id+1
            
        #     print("请求结束")

        #     self.current_id=self.current_id+1

