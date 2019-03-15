import redis
# from optparse import OptionParser
oke = dir(redis)
print(oke)
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('mobil', 'Suziki')
S = r.get('mobil')
print(S)


# r = redis.StrictRedis(host='localhost', port=6379, db=0)
# for key in r.scan_iter("user:*"):
#     # delete the key
#     r.delete(key)
