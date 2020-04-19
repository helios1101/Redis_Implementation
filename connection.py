import redis
redis = redis.Redis()

try (redis.ping()):
    print("ok")
else:
    print("not ok")