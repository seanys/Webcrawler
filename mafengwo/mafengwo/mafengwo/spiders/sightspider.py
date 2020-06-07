import scrapy
import re
import bs4
import json
import random
import pymysql
import time
import hashlib
# from mafengwo.items import SightItem

def __init__(self, *args, **kwargs):
    super(homeSpider, self).__init__(*args, **kwargs)
    pass

class PathSpider(scrapy.Spider):
    name = "sightspider"

    first_load=True

    current_id=39
    current_place="南京"
    
    start_urls = [
        "http://www.mafengwo.cn/jd/10487/gonglve.html"
    ]

    custom_settings = {
        "origin": "https://www.mafengwo.cn",
    }

    def parse_sights(self,response):
        text_response=json.loads(response.body_as_unicode())['data']['list']
        print(text_response)
        text_bs4=bs4.BeautifulSoup(text_response,'lxml')
        sights=text_bs4.find_all("a")
        
        city_id = response.meta['city_id']
        city_name = response.meta['city_name']

        items=[]
        for sight in sights:
            item=SightItem()
            item['href']=sight['href']
            item['name']=sight['title']
            item['city_id']=city_id
            item['city_name']=city_name
            items.append(item)
        return items

    
    def par(self,t):
        hl = hashlib.md5()
        hl.update(t)
        return hl.hexdigest()[2:12]
    
    def parse(self, response):
        with open('/Users/sean/Documents/MyProjects/Python/爬虫/mafengwo/mafenwo_sights/cities.json', 'r') as f:
            cities = json.load(f)
        for city in cities:
            city_id=city['city_id']
            city_name=city['name']
            for i in range(1,21):
                t=int(time.time()*1000)
                page_id=i
                qdata = '{"_ts":"'+str(t)+'","iMddid":"'+str(city_id)+'","iPage":"'+str(page_id)+'","iTagId":"0","sAct":"KMdd_StructWebAjax|GetPoisByTag"}c9d6618dbc657b41a66eb0af952906f1'
                sn=self.par(qdata.encode('utf-8'))

                yield scrapy.Request(
                    "http://www.mafengwo.cn/ajax/router.php?sAct=KMdd_StructWebAjax%7CGetPoisByTag&iMddid={}&iTagId=0&iPage={}&_ts={}&_sn={}".
                    format(city_id,page_id,t,sn),
                    meta={
                        "city_id":city_id,
                        "city_name":city_name
                    },
                    callback=self.parse_sights,
                )
        