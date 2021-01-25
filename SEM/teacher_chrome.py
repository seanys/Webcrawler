from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pandas as pd

university = "fudan"
page_link = "https://www.fdsm.fudan.edu.cn/AboutUs/teachers_dir.html"
route_link =  "https://www.fdsm.fudan.edu.cn/AboutUs/"

browser = webdriver.Chrome(executable_path="/Users/yangshan/chromedriver")
browser.get("https://www.fdsm.fudan.edu.cn/AboutUs/teachers_dir.html")
results = browser.find_elements_by_class_name("listW_p_ele")
all_names,all_links = [],[]
for item in results:
    soup = BeautifulSoup(item.get_attribute('innerHTML'), 'html.parser')
    for link in soup.findAll('a'):
        all_names.append(item.text)
        all_links.append(route_link + link.get("href"))

res_df = pd.DataFrame({"all_names":all_names,"all_links":all_links})
res_df.to_csv("data/school/%s.csv" % university,index="False")

browser.close()
