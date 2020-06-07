import json
import pymysql

db = pymysql.connect("rm-bp14fgqt2783fvljh0o.mysql.rds.aliyuncs.com","mc","Westbrook0","cAuth" )
cursor = db.cursor()

with open('/Users/sean/Documents/MyProjects/Python/爬虫/mafengwo/mafengwo/sight_detail_output/8-31-13:50.json', 'r') as f:
    sights = json.load(f)

for sight in sights:
    # print(sight)
    sql='update sights set location="{}",introduction="{}",time="{}",phone="{}",tickets="{}",open_time="{}",transportation="{}",images_urls="{}",images_num={},comments_num={},site="{}",exist=1  where name="{}"'.format(sight['location'],sight['introduction'],sight['time'],sight['phone'],sight['tickets'],sight['open_time'],sight['transportation'],sight['images_urls'],sight['images_num'],sight['comments_num'],sight['site'],sight['name'])
    cursor.execute(sql)
    db.commit()
    # print(sight['location'],sight['introduction'],sight['time'],sight['phone'],sight['tickets'],sight['open_time'],sight['transportation'],sight['images_urls'],sight['images_num'],sight['comments_num'],sight['site'],sight['name'])



db.close()