import json
import pymysql

db = pymysql.connect("rm-bp14fgqt2783fvljh0o.mysql.rds.aliyuncs.com","mc","Westbrook0","cAuth" )
cursor = db.cursor()

with open('/Users/sean/Documents/MyProjects/Python/爬虫/mafengwo/mafengwo/output/sights_hot.json', 'r') as f:
    sights = json.load(f)

for sight in sights:
    sql='Insert into sights(href,name,city_id,city_name) values("{}","{}",{},"{}")'.format(sight['href'],sight['name'],sight['city_id'],sight['city_name'])
    cursor.execute(sql)
    db.commit()



db.close()