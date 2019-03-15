class Karyawan(object):

    'Class ini untuk data Karyawan'
    jml_karyawan = 0  # Class variable
    alamat = 'pokoke'

    # constructor
    def __init__(self, kid, nama, jabatan):

        self.kid = kid
        self.nama = nama
        self.jabatan = jabatan
        Karyawan.jml_karyawan += 1
        Karyawan.alamat

    # method
    def infoKaryawan(self):

        print("Karyawan baru masuk")
        print("===================")
        print("ID : " + self.kid)
        print("Nama : " + self.nama)
        print("Jabatan : " + self.jabatan)


# cara mengakses/memakai class/membuat Object
obj = Karyawan("K001", "Ganjar", "Teknisi")
print("ID :" + obj.kid)
# bisa juga gini
print(f"ID : {obj.kid}")
print("nama :" + obj.nama)
print("jabatan :" + obj.jabatan)

# tambah karyawan baru
obj2 = Karyawan("K002", "Nadya", "Akunting")
obj2.infoKaryawan()

# tampilkan total Karyawan
print("-----------------------------")
print("Total Karyawan : " + str(Karyawan.jml_karyawan))
print("alamat : " + Karyawan.alamat)
