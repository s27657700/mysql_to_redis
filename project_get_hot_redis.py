import redis
r=redis.Redis(host='',port = 6379 , db=0)
def get_hot():
    car=r.get('hot').decode('utf-8').replace("\'",'').replace(' ','')
    car=car[1:-1].split(',')
    print(car)
    return car
