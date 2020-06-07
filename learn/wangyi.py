# -*- coding: utf-8 -*-
import os
import sys
import urllib
import requests
import re
from lxml import etree


def Page_Info(myPage):
    '''Regex'''
    mypage_Info = re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', myPage, re.S)
    return mypage_Info

def Spider(url):
    i = 0
    print ("downloading ", url)
    myPage = requests.get(url).content.decode("utf-8")
    print(myPage)
    # myPage = urllib2.urlopen(url).read().decode("gbk")
    # myPageResults = Page_Info(myPage)
    save_path = u"网易新闻抓取"
    filename = str(i)+"_"+u"新闻排行榜"
    # StringListSave(save_path, filename, myPageResults)
    i += 1
    # for item, url in myPageResults:
    #     print ("downloading ", url)
    #     new_page = requests.get(url).content.decode("gbk")
    #     # new_page = urllib2.urlopen(url).read().decode("gbk")
    #     newPageResults = New_Page_Info(new_page)
    #     filename = str(i)+"_"+item
    #     # StringListSave(save_path, filename, newPageResults)
    #     i += 1


if __name__ == '__main__':
    print ("start")
    # start_url = "http://news.163.com/rank/"
    start_url = "https://flights.ctrip.com/itinerary/oneway/sha-can?date=2019-07-18"
    Spider(start_url)
    print ("end")