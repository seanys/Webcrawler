from bs4 import BeautifulSoup
from urllib import request
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context

# response = request.urlopen("http://en.wikipedia.org")

# response=request.urlopen("http://www.baidu.com")

# response=request.urlopen("https://www.liaoxuefeng.com/")

# soup = BeautifulSoup(response)

# print(soup.prettify)

# reg1 = re.compile("<[^>]*>")
# soup = reg1.sub('',soup.prettify())

# response=request.urlopen("https://en.wikipedia.org/w/load.php?debug=false&lang=en&modules=site.styles&only=styles&skin=vector")

response=request.urlopen("https://www.fdsm.fudan.edu.cn/AboutUs/teachers_dir.html")

soup = BeautifulSoup(response)

# print(soup.prettify)

print(soup.div)

# print(response.read())