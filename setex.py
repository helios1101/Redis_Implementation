from style import style 
from connection import redis

def Rsetex():
    style("REDIS setex")
    print("Format : setex key expire value")
    cmd, key,expire, value = input("> ").split()

    if (cmd=='setex'):
        if key:
            if expire:
                if  value:
                    redis.setex(key,expire,value)
                    print("OK")
                else:
                    print("provide value")
            else:
                print("provide expire time")
        else:
            print("provide key")
    else:
        print("wrong format")
