from style import style 
from connection import redis


def Rzrank():
    style("REDIS zrank")
    print("Format : zrank key member")
    cmd, key, member = input("> ").split()

    if (cmd=='zrank'):
        if key:
            if member:
                print(redis.zrank(key, member))
            else:
                print("provide member")
        else:
            print("provide key")
    else:
        print("wrong format")
