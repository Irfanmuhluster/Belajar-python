import json
import codecs


# baca file
data = codecs.open('jsonformatter2.txt', 'r', 'utf-8-sig')

sipp = data.read()

getdata = json.loads(sipp)

for showdata in getdata['data']['acct']:
    user = showdata['user']
    print(user)
