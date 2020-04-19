from style import style 
from connection import redis


def Rzadd():
    style("REDIS zadd")
    print("Format : zadd key score member")
    cmd, key, score, member = input("> ").split()

    if (cmd=='zadd'):
        if key:
            if score:
                if member:
                    redis.zadd(key, {member:score})
                    print("OK")
                else:
                    print("provide member")
            else:
                print("provide score")
        else:
            print("provide key")
    else:
        print("wrong format")
