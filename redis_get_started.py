import redis

redis = redis.StrictRedis(
    host='localhost',
    port='6379')

'''Если не почистить базу, останутся удаленные элементы'''
redis.flushdb()  # clear db

redis.set('mykey', 'Hello from Python!')
value = redis.get('mykey')
print(value)

redis.zadd('vehicles', {'car': 0})
redis.zadd('vehicles', {'bike': 0})
redis.zadd('vehicles', {'slon': 0})
vehicles = redis.zrange('vehicles', 0, -1)
print(vehicles)
