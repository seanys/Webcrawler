# -*- coding: utf-8 -*-

# Scrapy settings for mafengwo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'mafengwo'

SPIDER_MODULES = ['mafengwo.spiders']
NEWSPIDER_MODULE = 'mafengwo.spiders'

USER_AGENT = 'Googlebot/2.1'

RETRY_TIMES = 5
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mafengwo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
FEED_EXPORT_ENCODING='UTF-8' 

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'mafengwo.middlewares.MafengwoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'mafengwo.middlewares.MafengwoDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'mafengwo.pipelines.MafengwoPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 500
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DOWNLOADER_MIDDLEWARES = {  
    # 'mafengwo.middlewares.ProxyMiddleware': 543
    'mafengwo.middlewares.ChromeDownloaderMiddleware': 543
}

PROXIES=[
    'http://138.68.240.218:808',
    'http://162.243.108.161:312',
    'http://158.177.89.87:900',
    'http://207.154.231.213:312',
    'http://178.62.193.19:312',
    'http://138.197.204.55:312',
    'http://165.227.215.71:312',
    'http://138.197.157.60:808',
    'http://217.61.125.194:808',
    'http://91.211.245.176:808',
    'http://31.220.51.173:808',
    'http://113.53.230.167:8',
    'http://35.204.123.188:808',
    'http://51.68.80.21:8',
    'http://91.200.114.58:5149',
    'http://139.162.78.109:808',
    'http://51.79.65.157:312',
    'http://89.246.66.124:312',
    'http://139.59.64.9:808',
    'http://94.177.246.142:808',
    'http://174.138.54.49:312',
    'http://138.68.161.60:808',
    'http://162.243.108.129:808',
    'http://167.99.40.249:8',
    'http://217.182.120.160:808',
    'http://140.227.33.252:6008',
    'http://167.179.103.33:8',
    'http://148.66.23.132:808',
    'http://51.15.17.155:1204',
    'http://138.197.157.32:808',
    'http://139.59.61.229:808',
    'http://59.62.42.232:3237',
    'http://101.255.116.113:5328',
    'http://139.59.101.223:312',
    'http://140.227.72.115:6008',
    'http://182.53.198.54:808',
    'http://82.196.11.105:312',
    'http://217.182.120.167:808',
    'http://45.55.9.218:808',
    'http://88.198.24.108:312',
    'http://188.166.83.13:808',
    'http://94.177.232.21:312',
    'http://109.70.202.137:4125',
    'http://110.74.196.235:4614',
    'http://138.68.41.90:808',
    'http://94.177.255.8:8',
    'http://68.183.147.115:808',
    'http://195.209.176.2:808',
    'http://159.203.2.130:8',
    'http://51.15.17.155:1148',
    'http://93.177.66.160:808',
    'http://185.99.35.81:8',
    'http://51.15.17.155:1558',
    'http://54.183.230.101:8',
    'http://167.71.242.25:8',
    'http://93.157.163.66:3508',
    'http://185.122.44.218:3680',
    'http://45.55.23.78:312',
    'http://157.245.8.142:312',
    'http://138.197.145.103:808',
    'http://185.34.22.225:4405',
    'http://51.15.17.155:1101',
    'http://210.5.10.87:5328',
    'http://138.68.165.154:808',
    'http://140.227.72.33:6008',
    'http://68.183.147.115:8',
    'http://188.18.54.242:6089',
    'http://167.71.167.227:808',
    'http://139.59.169.246:808',
    'http://217.61.22.186:312',
    'http://147.0.153.106:312',
    'http://67.205.146.29:808',
    'http://93.190.137.63:108',
    'http://139.59.53.106:808',
    'http://202.88.243.198:312',
    'http://211.244.224.130:808',
    'http://213.160.189.203:3150',
    'http://51.15.17.155:1150',
    'http://198.199.119.119:312',
    'http://217.23.6.40:312',
    'http://139.59.99.63:808',
    'http://140.227.24.69:6008',
    'http://93.190.137.134:108',
    'http://103.242.13.69:808',
    'http://140.227.53.106:6008',
    'http://223.19.212.30:819',
    'http://93.64.183.162:5650',
    'http://139.59.53.107:808',
    'http://45.55.23.78:808',
    'http://95.85.36.236:808',
    'http://176.235.143.71:808',
    'http://140.227.59.229:6008',
    'http://80.211.209.187:8',
    'http://188.226.141.211:808',
    'http://206.214.211.166:8',
    'http://138.197.157.45:808',
    'http://78.36.202.254:3233',
    'http://45.55.27.15:808',
    'http://94.127.217.66:4011',
    'http://150.109.55.190:8',
    'http://203.189.142.23:5328',
    'http://80.211.135.240:808',
    'http://207.180.226.111:8',
    'http://139.59.99.119:808',
    'http://51.15.17.155:1457',
    'http://180.178.98.150:3587',
    'http://182.52.51.47:4114',
    'http://192.241.245.207:312',
    'http://144.217.169.71:808',
    'http://140.227.9.125:6008',
    'http://91.122.37.92:2121',
    'http://139.59.109.156:808',
    'http://51.15.17.155:2588',
    'http://194.124.35.114:8',
    'http://140.227.200.111:6008',
    'http://176.102.48.105:3201',
    'http://140.227.168.6:6008',
    'http://119.192.195.83:44',
    'http://118.122.114.238:900',
    'http://139.59.62.255:808',
    'http://66.82.22.79:8',
    'http://51.15.17.155:1513',
    'http://80.211.31.121:8',
    'http://191.240.156.154:3612',
    'http://114.143.181.199:8',
    'http://188.166.119.186:8',
    'http://139.59.99.234:312',
    'http://217.61.125.194:8',
    'http://167.71.206.166:808',
    'http://181.196.176.22:4247',
    'http://85.43.127.116:8',
    'http://198.199.120.102:808',
    'http://178.62.193.19:808',
    'http://212.2.204.181:5194',
    'http://35.198.192.157:8',
    'http://200.141.192.70:808',
    'http://140.227.172.6:6008',
    'http://165.227.215.71:808',
    'http://138.68.173.29:808',
    'http://140.227.8.169:6008',
    'http://178.172.201.137:888',
    'http://138.197.204.55:808',
    'http://149.56.193.7:808',
    'http://207.180.226.111:312',
    'http://45.248.138.210:5971',
    'http://92.249.122.108:6177',
    'http://159.138.5.222:8',
    'http://159.65.151.96:808',
    'http://1.10.189.53:3780',
    'http://119.82.252.115:4908',
    'http://105.19.49.178:8',
    'http://139.59.61.229:312',
    'http://54.37.208.209:5031',
    'http://144.217.163.138:808',
    'http://148.66.23.133:808',
    'http://88.198.50.103:808',
    'http://67.205.149.230:808',
    'http://89.46.196.59:8',
    'http://91.211.245.193:8',
    'http://47.240.46.238:888',
    'http://162.243.108.141:808',
    'http://31.202.35.218:4520',
    'http://188.166.83.20:312',
    'http://51.15.17.155:2455',
    'http://119.28.203.242:800',
    'http://51.15.17.155:1415',
    'http://51.15.17.155:1119',
    'http://193.107.106.95:3295',
    'http://134.209.14.170:808',
    'http://188.226.141.61:808',
    'http://119.161.78.100:312',
    'http://113.53.29.227:5077',
    'http://195.20.102.248:3302',
    'http://103.105.197.66:8',
    'http://165.22.162.120:312',
    'http://51.15.17.155:1136',
    'http://51.15.17.155:1557',
    'http://182.19.41.145:8',
    'http://182.163.103.99:5655',
    'http://140.227.64.157:6008',
    'http://94.177.232.21:808',
    'http://51.15.17.155:2208',
    'http://185.132.179.109:808',
    'http://91.103.196.170:4125',
    'http://95.85.36.236:312',
    'http://103.89.253.246:312',
    'http://198.199.119.119:808',
    'http://119.192.195.83:808',
    'http://139.59.53.105:808',
    'http://139.180.193.43:811',
    'http://207.154.231.212:312',
    'http://91.200.124.197:3084',
    'http://94.177.232.21:8',
    'http://159.203.166.41:808',
    'http://217.61.22.186:808',
    'http://122.201.112.114:8',
    'http://35.247.236.179:808',
    'http://163.172.95.183:312',
    'http://138.197.222.35:312',
    'http://51.15.17.155:1555',
    'http://1.10.188.214:4259',
    'http://113.53.83.212:4466',
    'http://167.88.117.209:808',
    'http://163.158.19.154:8',
    'http://110.39.52.10:4548',
    'http://217.61.99.199:312',
    'http://186.64.121.186:8',
    'http://188.166.83.13:312',
    'http://140.227.79.205:6008',
    'http://13.78.116.29:8',
    'http://181.129.50.138:4833',
    'http://140.227.59.172:6008',
    'http://99.79.116.201:8',
    'http://193.188.254.67:5328',
    'http://51.15.17.155:1488',
    'http://148.66.23.130:808',
    'http://109.75.47.248:3015',
    'http://118.97.94.234:8',
    'http://45.55.27.161:312',
    'http://175.139.179.65:3513',
    'http://176.102.48.94:3097',
    'http://138.68.240.218:312',
    'http://139.59.101.223:808',
    'http://51.15.17.155:1417',
    'http://176.10.127.194:8',
    'http://200.110.172.2:8',
    'http://51.15.17.155:1259',
    'http://139.59.109.156:312',
    'http://165.22.33.143:808',
    'http://159.138.20.247:8',
    'http://35.240.23.37:8',
    'http://192.117.146.110:8',
    'http://167.99.57.138:808',
    'http://197.254.48.242:5536',
    'http://149.129.57.78:8',
    'http://144.217.163.138:312',
    'http://138.197.157.44:808',
    'http://138.68.24.145:808',
    'http://139.59.99.63:312',
    'http://51.15.17.155:2109',
    'http://192.162.193.243:3691',
    'http://138.197.222.35:808',
    'http://193.107.247.98:5328',
    'http://92.222.180.156:808',
    'http://165.227.42.16:8',
    'http://186.64.121.186:312',
    'http://51.15.17.155:1928',
    'http://212.17.117.221:8',
    'http://138.68.161.14:312',
    'http://176.9.119.170:808',
    'http://67.205.174.209:808',
    'http://89.46.196.59:808',
    'http://162.243.108.161:808',
    'http://147.135.226.209:808',
    'http://158.46.127.222:5257',
    'http://5.140.233.65:5809',
    'http://80.211.31.121:808',
    'http://188.166.83.17:808',
    'http://61.238.82.202:808',
    'http://51.15.17.155:2450',
    'http://177.128.42.25:4500',
    'http://207.154.231.213:808',
    'http://174.138.54.49:808',
    'http://185.199.82.163:5328',
    'http://78.158.54.213:5178',
    'http://165.227.42.16:808',
    'http://182.52.90.43:3332',
    'http://213.141.93.60:3212',
    'http://41.170.12.92:3744',
    'http://109.248.43.28:8',
    'http://110.74.209.202:5276',
    'http://167.99.114.19:312',
    'http://34.74.43.175:808',
    'http://207.154.231.211:808',
    'http://159.138.1.185:8',
    'http://81.163.36.210:3419',
    'http://147.135.226.209:8',
    'http://109.75.44.36:3167',
    'http://51.15.17.155:2408',
    'http://167.99.114.19:808',
    'http://140.227.9.115:6008',
    'http://138.128.117.162:8',
    'http://91.134.24.240:808',
    'http://140.227.234.90:6008',
    'http://140.227.231.88:6008',
    'http://163.172.95.183:808',
    'http://165.227.215.62:808',
    'http://89.250.221.106:5328',
    'http://37.59.136.91:8',
    'http://158.69.185.135:808',
    'http://207.188.73.155:8',
    'http://144.217.161.146:808',
    'http://176.117.255.182:5310',
    'http://68.183.195.222:808',
    'http://125.110.80.143:900',
    'http://51.15.17.155:1104',
    'http://209.97.169.49:811',
    'http://51.15.17.155:2560',
    'http://139.59.99.119:312',
    'http://51.15.17.155:2598',
    'http://124.156.108.71:8',
    'http://176.119.18.92:4165',
    'http://159.203.91.6:312',
    'http://202.85.52.151:8',
    'http://171.100.83.50:3171',
    'http://138.201.72.117:8',
    'http://202.138.248.171:5328',
    'http://110.74.196.232:3985',
    'http://207.154.231.212:808',
    'http://104.128.206.123:5776',
    'http://61.19.40.50:4263',
    'http://168.194.15.194:5328',
    'http://134.209.126.148:808',
    'http://70.37.111.187:8',
    'http://146.88.51.235:8',
    'http://140.227.175.6:6008',
    'http://157.245.8.142:808',
    'http://188.226.141.127:808',
    'http://154.73.137.157:4333',
    'http://140.227.56.192:6008',
    'http://182.53.206.47:4759',
    'http://47.90.95.31:811',
    'http://35.240.139.161:808',
    'http://51.15.17.155:1111',
    'http://157.230.135.138:808',
    'http://150.109.47.193:811',
    'http://162.243.107.120:312',
    'http://207.154.231.216:808',
    'http://188.168.96.34:3429',
    'http://51.15.17.155:1101',
    'http://192.241.245.207:808',
    'http://91.188.223.137:8',
    'http://188.166.83.20:808',
    'http://212.237.38.168:808',
    'http://140.227.8.155:6008',
    'http://134.209.126.148:312',
    'http://103.99.177.247:8',
    'http://140.227.27.254:6008',
    'http://188.166.83.34:808',
    'http://62.152.75.110:5028',
    'http://207.180.226.111:808',
    'http://167.71.161.102:808',
    'http://176.9.75.42:808',
    'http://67.205.146.29:312',
    'http://202.182.121.205:808',
    'http://140.227.10.102:6008',
    'http://154.72.63.84:3865',
    'http://80.211.209.187:808',
    'http://81.93.78.162:4059',
    'http://59.91.127.29:5384',
    'http://203.246.112.133:312',
    'http://139.59.53.106:312',
    'http://139.180.163.43:808',
    'http://194.42.119.235:4273',
    'http://103.105.197.67:8',
    'http://191.103.254.145:4732',
    'http://217.23.6.40:808',
    'http://139.255.92.26:5328',
    'http://14.162.146.128:4008',
    'http://190.205.122.58:5328',
    'http://181.196.151.82:4605',
    'http://47.75.213.201:8',
    'http://213.159.248.165:5600',
    'http://159.203.166.41:312',
    'http://31.41.92.154:2350',
    'http://51.15.17.155:1101',
    'http://197.234.35.82:5328',
    'http://42.2.66.140:808',
    'http://67.205.132.241:808',
    'http://211.252.169.8:8',
    'http://159.65.237.253:808',
    'http://197.221.113.65:4267',
    'http://91.225.109.186:5661',
    'http://45.55.27.161:808',
    'http://41.210.161.114:8',
    'http://176.9.119.170:312',
    'http://82.208.111.100:5248',
    'http://185.132.178.210:808',
    'http://140.227.29.110:6008',
    'http://174.138.38.206:808',
    'http://80.53.233.124:8',
    'http://159.203.91.6:808',
    'http://217.61.22.186:8',
    'http://93.39.228.188:312',
    'http://81.23.32.47:44',
    'http://217.61.122.19:808',
    'http://94.177.255.8:808',
    'http://167.71.206.166:800',
    'http://200.116.226.210:3696',
    'http://104.32.43.13:5328',
    'http://168.70.27.80:900',
    'http://51.15.17.155:1158',
    'http://176.196.89.216:4684',
    'http://47.75.186.127:8',
    'http://95.213.195.134:8',
    'http://47.240.38.111:8',
    'http://207.154.231.217:312',
    'http://60.246.89.102:5328',
    'http://180.235.39.9:8',
    'http://52.233.189.29:8',
    'http://140.227.65.187:6008',
    'http://88.198.24.108:808',
    'http://145.239.81.69:808',
    'http://46.4.96.137:312',
    'http://80.211.135.240:312',
    'http://212.67.65.82:5553',
    'http://140.227.58.206:6008',
    'http://167.71.101.134:808',
    'http://51.15.17.155:1341',
    'http://45.55.27.15:312',
    'http://118.175.226.30:5217',
    'http://140.227.28.170:6008',
    'http://91.134.24.240:8',
    'http://91.77.162.117:808',
    'http://95.154.104.147:3776',
    'http://140.227.199.231:6008',
    'http://51.15.17.155:1116',
    'http://89.250.149.114:6098',
    'http://91.211.245.193:808',
    'http://185.7.85.21:8',
    'http://220.130.51.190:808',
    'http://88.99.149.188:3128',
    'http://5.167.51.235:808',
    'http://185.132.178.203:808',
    'http://140.227.30.81:6008',
    'http://193.233.9.167:4142',
    'http://46.4.96.137:808',
    'http://159.224.220.63:4429',
    'http://159.203.127.55:8',
    'http://68.183.155.113:808',
    'http://181.196.254.202:5328',
    'http://181.48.28.66:3083',
    'http://171.25.164.123:3058',
    'http://103.124.104.4:8',
    'http://185.132.178.207:808',
    'http://160.119.129.42:3782',
    'http://45.7.231.15:808',
    'http://181.57.198.102:4696',
    'http://146.88.51.234:8',
    'http://159.138.3.119:8',
    'http://46.52.213.194:6197',
    'http://162.243.108.129:312',
    'http://125.26.109.114:6100',
    'http://119.15.82.222:3779',
    'http://125.26.7.124:6164',
    'http://191.96.42.106:312',
    'http://36.67.223.67:4367',
    'http://139.59.99.234:808',
    'http://140.227.201.232:6008',
    'http://51.15.17.155:1142',
    'http://188.166.83.17:312',
    'http://167.71.242.25:312',
    'http://103.9.188.160:4673',
    'http://80.188.212.2:4672',
    'http://162.243.107.120:808',
    'http://139.59.59.63:808',
    'http://202.51.188.139:5620',
    'http://61.238.82.201:808',
    'http://212.75.217.42:4047',
    'http://138.186.23.5:4609',
    'http://165.227.160.139:8',
    'http://138.68.161.14:808',
    'http://51.15.17.155:1961',
    'http://197.159.12.167:6193',
    'http://124.158.177.171:2350',
    'http://51.15.17.155:1120',
    'http://109.86.184.131:4923',
    'http://46.4.46.98:888'
]