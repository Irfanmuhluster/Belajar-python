import redis
import json

# import ui
# from optparse import OptionParser

r = redis.StrictRedis(host='localhost', port=6379, db=0)
newum = r.info()
print(json.dumps(newum, indent=4, sort_keys=True))
print(r.lrange('batang', 0, 2))
print(r.get('daun'))

try:
    keys = r.scan_iter()
except:
    print("Error using scan_iter, maybe you need the latest version of python-redis?")
    exit(1)

itemised_keys = r.scan_iter()

# len(itemised_keys)
# print(itemised_keys)
count = 0
for key in itemised_keys:
    count = count + 1
    print(key)
print("counted: {} keys".format(count))


# print("iwejrio")


# headers = ['CPU System', 'CPU User', 'Used Memory']
# data = []
# dapetin list account via whmapi1
# for item in whm_list_accounts(ctx, node):
#     data.append(
#         [
#             (ui.teal, item['domain'], ),    # domain
#             (ui.yellow, item['user'], ),    # username
#             (ui.white, item['diskused'], )  # disk usage
#         ]
#     )
# # tampilkan
# ui.info_table(data, headers=headers)
