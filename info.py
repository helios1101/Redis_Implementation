from connection import redis 
from style import style

def infoDB():
    style("Getting DB Info")
    data = redis.info()
    for key, value in data.items():
        print(key, ":", value)