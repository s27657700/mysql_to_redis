import pymysql
import time
import redis
host="localhost"
port=3306
user=''
passwd=''
db='toyota'
charset='utf8'
conn=pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db,charset=charset)
cursor=conn.cursor()
r=redis.Redis(host='172.28.128.12',port = 6379 , db=0)
while True:

    passed5min='''select model, count(*) from search  where  86400> (select t from search  order by t desc limit 1)-t  group by model  order by count(*) desc limit 1;'''
    cursor.execute(passed5min)
    data=cursor.fetchall()
    print(data[0])
    if data[0][0]!=None:
        r.set('hot',str(data[0]))
        

    time.sleep(15)

cursor.close()
conn.close()