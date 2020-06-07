import scrapy
import re
import bs4
import json
import time
import pymysql
from mafengwo.items import SightItem

class PathSpider(scrapy.Spider):

    name = "sightpage"

    # start_urls = ["http://www.mafengwo.cn/poi/6427.html"]
    start_urls = ["https://baidu.com"]

    def sight_parse(self,response):
        item=SightItem()
        item['name']=response.meta['name']
        item['href']=response.meta['href']
        item['city_id']=response.meta['city_id']
        item['city_name']=response.meta['city_name']
        
        introduction=response.xpath("//div[@class='summary']/text()").extract()
        if(len(introduction)>0):
            item['introduction']=re.sub(" ", "", introduction[0])
            item['introduction']=re.sub("\"", "\'", item['introduction'])
            print(introduction[0])
        else:
            item['introduction']=""

        phone=response.xpath("//li[@class='tel']/div[@class='content']/text()").extract()
        if(len(phone)>0):
            item['phone']=phone[0]
            print(phone[0])
        else:
            item['phone']=""

        time=response.xpath("//li[@class='item-time']/div[@class='content']/text()").extract()
        if(len(time)>0):
            item['time']=time[0]
            print(time[0])
        else:
            item['time']=""

        site=response.xpath("//li[@class='item-site']/div[@class='content']/a/@href").extract()
        if(len(site)>0):
            item['site']=site[0]
            print(site[0])
        else:
            item['site']=""

        location=response.xpath("//div[@class='mod mod-location']/div[@class='mhd']/p[@class='sub']/text()").extract()
        if(len(location)>0):
            item['location']=location[0]
            print(location[0])
        else:
            item['location']=""

        open_time=response.xpath("//div[@class='mod mod-detail']/dl[last()]/dd/text()").extract()
        item['open_time']= open_time
        print(open_time)

        transportation=response.xpath("//div[@class='mod mod-detail']/dl[last()-2]/dd/text()").extract()
        item['transportation']=transportation
        # for index,trans_simple in enumerate(item['transportation']):
            # item['transportation'][index]=re.sub("\"", "\'", trans_simple)
        
        print(item['transportation'])

        tickets=response.xpath("//div[@class='mod mod-detail']/dl[last()-1]/dd/div/text()").extract()
        item['tickets']=tickets
        print(tickets) 

        images_urls=response.xpath("//a[@class='photo']/div[@class='bd']/div/img/@src").extract()
        item['images_urls']=images_urls
        print(images_urls)

        images_num=response.xpath("//a[@class='photo']/div[@class='bd']/span/text()").extract()
        
        if(len(images_num)>0):
            # item['images_num']=images_num[0]
            item['images_num']=re.sub("\D", "", images_num[0])
            print(re.sub("\D", "", images_num[0]))
        else:
            item['images_num']=-1

        comments_num=response.xpath("//li[@data-scroll='commentlist']/a/span/text()").extract()
        item['comments_num']=re.sub("\D", "", comments_num[0])
        print(re.sub("\D", "", comments_num[0]))

        # db = pymysql.connect("rm-bp14fgqt2783fvljh0o.mysql.rds.aliyuncs.com","mc","Westbrook0","cAuth" )
        # cursor = db.cursor()
        # sql='update sights set location="{}",introduction="{}",time="{}",phone="{}",tickets="{}",open_time="{}",transportation="{}",images_urls="{}",images_num={},comments_num={},site="{}",exist=1 where name="{}"'.format(item['location'],item['introduction'],item['time'],item['phone'],item['tickets'],item['open_time'],item['transportation'],item['images_urls'],item['images_num'],item['comments_num'],item['site'],item['name'])
        # cursor.execute(sql)
        # db.commit()
        # db.close()
       
        return item

        
    def parse(self, response):

        # with open('/Users/sean/Documents/MyProjects/Python/爬虫/mafengwo/mafengwo/output/sights_hot.json', 'r') as f:
        #     sights = json.load(f)

        db = pymysql.connect("rm-bp14fgqt2783fvljh0o.mysql.rds.aliyuncs.com","mc","Westbrook0","cAuth" )
        cursor = db.cursor()
        sql="SELECT * FROM sights where exist=0"
        cursor.execute(sql)
        sights = cursor.fetchall()

        for sight in sights:
            # name=sight['name']
            # href=sight['href']
            # city_id=sight['city_id']
            # city_name=sight['city_name']
            name=sight[4]
            href=sight[3]
            city_id=sight[1]
            city_name=sight[2]
            # print(name,href,city_id,city_name)
            yield scrapy.Request(
                    href,
                    meta={
                        "name":name,
                        "href":href,
                        "city_id":city_id,
                        "city_name":city_name
                    },
                    callback=self.sight_parse,
                )
                
        print(len(sights))
        db.close()
