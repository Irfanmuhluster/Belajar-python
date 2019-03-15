import http.client
import json

conn = http.client.HTTPSConnection("api.rajaongkir.com")

headers = {'key': "87bd7b24a64252042151af555f23e94b"}

conn.request("GET", "/starter/province", headers=headers)

res = conn.getresponse()
data = res.read()

sipp = data.decode("utf-8")

getdata = json.loads(sipp)

data1 = []
data2 = []

# print(getdata)

for ext in getdata['rajaongkir']['results']:
    province_id = ext['province_id']
    province = ext['province']
    data1.append(str(province_id))
    data2.append(str(province))


tes1 = data1
tes2 = data2
cek = list(zip(tes1, tes2))
print(cek)

# print(json['rajaongkir']['results'][$i]['province'])


# conncity.request("GET", "/starter/city?province=3", headers=headers)
