def hello():
    print "Hello world"


def getDBConfig():
    config = {
        "driver": "sqlite3",
        "name": "testing.db",
        "path": "/home/user/Documents"
    }

    return config


def getName(id):
    if id == 1:
        name = "Alexander Grotesqiue"
    elif id == 2:
        name = "Saleh Mahmoud Al Qassam"
    elif id == 3:
        name = "Natasha Vorvanova"

    return name


def getHargaDealer(harga):
    harga_baru = harga + ((harga / 100.0) * 15.0)
    print harga_baru


# lambda adalah function tanpa nama utk function pendek
def xe(length): return range(0, length)


ntap = xe(10)
print(ntap)

'''range dlm function '''
# def getNumberList(length):
#    x = range(0, length)
#    return x

'''range dalam for '''
#ulang = 10
#i = 1
# for i in range(ulang):
#    print "Perulangan ke-"+str(i)


def getLuasPersegiPanjang(p, l):
    x = p * l
    return x


hello()

db_config = getDBConfig()
print db_config

name = getName(3)
print name

# ginijuga bisa
getHargaDealer(1000000)


# number_list = getNumberList(10)
# print number_list

luas = getLuasPersegiPanjang(20, 10)
print luas

x = "lorem ipsum sit amet dolor amet.\nlorem ipsum sit amet dolor amet."

print(x.split(" "))
print(x.splitlines())


def hello(x, y):
    print("Hello world (%d, %d)" % (x, y))


for i in range(0, 10):
    hello(i, i**i)


def hello(x, y, z, *args):
    print(x)
    print(y)
    print(z)
    print(args)


hello(1, 2, 3, 4)
hello(1, 2, 3, 4, 5)
hello(1, 2, 3, 4, 5, 6)

# ARGS KELEBHIANNYA ?
