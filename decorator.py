def mydecorator(f):
    def wrapper(name):
        print('sebelum dekorasi')
        return f(name)
        print('setelah dekorasi')
    return wrapper


def salam(tes):
    def wrapper(namas):
        return "Assalamu'alaikum " + tes(namas)
    return wrapper


def rahmat(tes):
    def wrapper(nama):
        return "Warohmatullah " + tes(nama)
    return wrapper


def berkah(tes):
    def wrapper(nama):
        return "Wabarokatuh " + tes(nama)
    return wrapper

# def decor1(name):
  #  return name


@mydecorator
def printdekor(name):
    return name


@salam
def decor2(name):
    return name


@salam
@rahmat
def decor3(namew):
    return namew


@salam
@rahmat
@berkah
def decor4(name):
    return name


# tetap saja wrapper dipanggil satu kali
print printdekor("Irfan")
# print decor1("Aziz")
print decor2("Aziz")
print decor3("Aziz")
print decor4("Aziz")
