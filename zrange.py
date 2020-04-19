from style import style 
from connection import redis


def Rzrange():
    style("REDIS zrange")
    print("Format : zrange key from to")
    cmd, key, start, end = input("> ").split()

    if (cmd=='zrange'):
        if key:
            if start:
                if end:
                    data = redis.zrange(key, start, end)
                    if data:
                        for i in data:
                            print(i.decode('utf-8'))
                    else:
                        print("empty list or set")
                else:
                    print("provide end")
            else:
                print("provide expire start")
        else:
            print("provide key")
    else:
        print("wrong format")
