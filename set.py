#!/usr/bin/python3
from style import style 
from connection import redis

def Rset():
    style("REDIS set")
    print("format : set key value")
    cmd, key, value = input("> ").split()

    if (cmd=='set'):
        if key:
            if value:
                redis.set(key,value)
                print("OK")
            else:
                print("provide value")
        else:
            print("provide key")
    else:
        print("wrong format")
