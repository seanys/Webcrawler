import scrapy
import re
import bs4
import json
import random
import pymysql
import time
import hashlib
# from mafengwo.items import CityItem


class PathSpider(scrapy.Spider):
    name = "province2city"
    
    start_urls = [
        "http://www.mafengwo.cn/mdd/citylist/12700.html"
    ]

    custom_settings = {
        "origin": "https://www.mafengwo.cn",
    }

    # with open('/Users/sean/Documents/MyProjects/Python/爬虫/mafengwo/mafengwo/output/province.json', 'r') as f:
    #     provs = json.load(f)
    # for prov in provs:
    #     print(prov)

    def parse_cities(self,response):
        # print("获得页面")
        text_response=json.loads(response.body_as_unicode())
        print(text_response)
        # text_bs4=bs4.BeautifulSoup(text_response,'lxml')
        # sights=text_bs4.find_all("a")
        
        # items=[]
        # for sight in sights:
        #     item=SightItem()
        #     item['href']=sight['href']
        #     item['name']=sight['title']
        #     item['city_id']=10487
        #     items.append(item)
        # return items
    def make_headers(self):
        ''' 制作请求头 '''
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'zh,en-US;q=0.9,en;q=0.8,zh-HK;q=0.7,zh-CN;q=0.6',
            'content-length':51,
            'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie':'__jsluid_h=75a9b01e4ba3bf2cde2c1bab5386a927; mfw_uuid=5d3dc24a-a027-6350-baf3-a30eec237088; uva=s%3A91%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1564328544%3Bs%3A10%3A%22last_refer%22%3Bs%3A23%3A%22http%3A%2F%2Fwww.mafengwo.cn%2F%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1564328544%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=5d3dc24a-a027-6350-baf3-a30eec237088; ad_close_num=2; PHPSESSID=d1eg2j8v1ssk4qqh1osetrfpj5; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222019-08-28+18%3A15%3A56%22%3B%7D; __mfwc=direct; __omc_chl=; __omc_r=; mafengwo=4dbcbcd59539b19b954ede53ee7fedcb_37155464_5d665ab7778952.58614339_5d665ab7778984.56654395; mfw_uid=37155464; __mfwa=1564328544334.76626.29.1567077736830.1567079917855; uol_throttle=37155464; __mfwb=e44336b096cf.43.direct; __mfwlv=1567084946; __mfwvn=20; __mfwlt=1567084946',
            'host':'www.mafengwo.cn',
            'orgin':'http://www.mafengwo.cn',
            'DNT':1,
            'Proxy-Connection': 'keep-alive',
            'upgrade-insecure-requests': '1',
            'user-agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'   
        }
        return headers
    
    def back_reponse(self, url, headers, params=None, form_data=None, json_data=None, is_get=True):
        ''' 操作requests模块 '''
        try:
            proxies = { "http": "http://47.90.73.118:3128","https":"178.32.59.233:53281"}
            if is_get:
                # rp = self.ss.get(url, headers=headers, params=params)
                rp = self.ss.get(url, headers=headers, params=params,proxies=proxies)
            else:
                rp = self.ss.post(url, headers=headers, params=params, data=form_data, json=json_data)
                # rp = self.ss.post(url, headers=headers, params=params, data=form_data, json=json_data,proxies=proxies)
            if rp.status_code == 200:
                return rp 
            else:
                None
        except:
            return None
    
    def par(self,t):
        hl = hashlib.md5()
        hl.update(t)
        return hl.hexdigest()[2:12]
    
    def parse(self, response):
        page_id=1
        prov_id=13732

        for i in range(1,3):
            page_id=i
            t=int(time.time()*1000)
            qdata = '{"_ts":"'+str(t)+'","mddid":"'+str(prov_id)+'","page":"'+str(page_id)+'"}c9d6618dbc657b41a66eb0af952906f1'
            sn=self.par(qdata.encode('utf-8'))
            print(sn)

            yield scrapy.Request(
                "http://www.mafengwo.cn/mdd/base/list/pagedata_citylist?mddid=13732&page=2&_ts=1567084954469&_sn=6661c1d73a".
                format(prov_id,page_id,t,sn),
                callback=self.parse_cities,
            )

            yield scrapy.Request(
                "http://www.mafengwo.cn/mdd/base/list/pagedata_citylist?mddid={}&page={}&_ts={}&_sn={}".
                format(prov_id,page_id,t,sn),
                callback=self.parse_cities,
            )
        
        