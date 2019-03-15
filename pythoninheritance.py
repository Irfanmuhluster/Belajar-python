class Kendaraan(object):

    bahan_bakar = "bensin"

    def __init__(self, Nama_Kendaraan):
        self.nama = Nama_Kendaraan


mobil = Kendaraan("mobil")
motor = Kendaraan("motor")

print(mobil.nama)
print(motor.nama)


class Car(object):
    """
            blueprint for car
    """

    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarating...")
        "accelarator functionality here"

    def change_gear(self, gear_type):
        print("gear changed")
        " gear related functionality here"


maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)
print(maruthi_suzuki.color)


class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):

        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()
