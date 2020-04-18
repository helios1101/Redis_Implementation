import json         
import redis      
import argparse 

parser = argparse.ArgumentParser()
arguments = parser.parse_args()
redis = redis.Redis()

if arguments.get: 
    if redis.get(arguments.get):
        print(redis.get(arguments.get).decode("utf-8"))
    else:
        print("No value in DB")

if arguments.set:
    if arguments.value:
        if (arguments.expire):
            redis.setex(arguments.set, arguments.expire, arguments.value)
            print(arguments.set, "set to", arguments.value, "for", arguments.expire, "seconds")
        else:
            redis.set(arguments.set, arguments.value)
            print(str(arguments.set), ":" , str(arguments.value))

    else:
        print("value not given for the key :", arguments.set) 

if arguments.zadd:
    if arguments.key:
        if arguments.score:
            if arguments.member:
                redis.zadd(arguments.key, { arguments.member : arguments.score})
                print("zadd", arguments.key, arguments.score, arguments.member )
            else:
                print("provide member for zadd")
        else:
            print("provide score for zadd")
    else:
        print("provide the key for zadd")
        
        
if arguments.zrange:
    if arguments.key:
        data = redis.zrange(arguments.key, 0, -1)
        print(data[:])
    else:
        print("provide the key for zrange")


if arguments.zrank:
    if arguments.key:
        if arguments.member:
            data = redis.zrank(arguments.key, arguments.member)
            print(data)
        else:
            print("provide member for zrank")
    else:
        print("provide the key for zrank")
