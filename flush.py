from style import style
from connection import redis

def Rflush():
    style("REDIS flush")
    print("Are you sure?")
    i = input()
    if i =='yes':
        redis.flushall()
        print("DB flushed")
    else:
        pass
    