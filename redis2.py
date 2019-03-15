import redis
import json
# import ui
# from optparse import OptionParser

r = redis.StrictRedis(host='localhost', port=6379, db=0)
newum = r.info()
print(json.dumps(newum, indent=4, sort_keys=True))
