from connection import redis
from style import style

def testDB():
    style("Testing connection")
    ping = redis.ping()
    if ping == True:
        print("Redis DB connected!")
    else:
        print("DB not conencted!")