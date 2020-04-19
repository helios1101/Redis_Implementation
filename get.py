
from style import style
from connection import redis

def Rget():
    style("REDIS get")
    print("format : get key")
    cmd, key = input("> ").split()

    if (cmd=='get'):
        if key:
            if (redis.get(key)):
                print(redis.get(key).decode("utf-8"))
            else:
                print("(nil)")
        else:
            print("provide key")
    else:
        print("wrong format")
