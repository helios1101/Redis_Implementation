import json         # to parse json objects
import redis        # to use redis with python
import argparse     # for help manual

parser = argparse.ArgumentParser()

# adding help manual ---------------------------------------------------------------------------------------------------------------------
parser.add_argument("--get", "--GET", action="store", default = False, help="to get the value for the provided key")
parser.add_argument("--set", "--SET",action="store", default = False, help="to set the value for the provided key")
parser.add_argument("--expire", "--expire",action="store", default = False, help="to get the expiration value for the provided key")
parser.add_argument("--value","--VALUE", action= "store", help="value")
parser.add_argument("--zadd","--ZADD", action="store", default=False, help="ZADD [CH] key score member")
parser.add_argument("--zrank", action="store", default=False)
parser.add_argument("--key",  action="store")
parser.add_argument("--score", action="store")
parser.add_argument("--member", action="store")
parser.add_argument("--zrange", action="store")

arguments = parser.parse_args()

redis = redis.Redis()

# for getting values from redis----------------------------------
if arguments.get: 
    if redis.get(arguments.get):
        print(redis.get(arguments.get).decode("utf-8"))
    else:
        print("No value in DB")

# for setting valye in redis--------------------------------------
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
        
# for adding to a orered set ---------------------------------------------
if arguments.zadd:
    if arguments.key:
        if arguments.score:
            if arguments.member:
                # redis.zadd("key",{"value":score}) syntax of zadd for newer update of redis-----------------
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
