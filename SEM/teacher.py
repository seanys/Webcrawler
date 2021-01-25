import requests
import csv
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

url = 'https://www.fdsm.fudan.edu.cn/AboutUs/teachers_dir.html'

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
fo = open("data/pages/fudan.html", "a+")
fo.write(soup.text)
fo.close()


# print(soup.prettify())
# print(soup)

# links = soup.find_all('div', {'class': 'listW_p_ele'})

# print(links)

