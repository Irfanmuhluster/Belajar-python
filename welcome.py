print("Selamat datang di Python")
panjang = 10
lebar = 5
luas = panjang * lebar
print(luas)
nilai = 3
# Jika pernyataan pada if bernilai TRUE maka if akan dieksekusi, tetapi jika FALSE kode pada else yang akan dieksekusi.
if(nilai > 7):
    print("Selamat Anda Lulus")
else:
    print("Maaf Anda Tidak Lulus")


# Contoh penggunaan kondisi elif

hari_ini = "Minggu"

if(hari_ini == "Senin"):
    print("Saya akan kuliah")
elif(hari_ini == "Selasa"):
    print("Saya akan kuliah")
elif(hari_ini == "Rabu"):
    print("Saya akan kuliah")
elif(hari_ini == "Kamis"):
    print("Saya akan kuliah")
elif(hari_ini == "Jumat"):
    print("Saya akan kuliah")
elif(hari_ini == "Sabtu"):
    print("Saya akan kuliah")
elif(hari_ini == "Minggu"):
    print("Saya akan libur")

nilai2 = 90
if nilai2 > 80:
    print("Selamat, kamu dapat nilai A")
    if nilai2 > 95:
        print("Selamat kamu dapat bonus voucher pendidikan karena nilai kamu A")
    elif nilai2 == 100:
        print("Selamat kamu dapat buku pelajaran gratis selama satu semester karena nilai kamu A sempurna.")
elif nilai2 > 70 and nilai2 <= 80:
    print("Selamat, kamu dapat nilai B")
elif nilai2 > 60 and nilai2 <= 70:
    print("Selamat, kamu dapat nilai C")
elif nilai2 > 45 and nilai2 <= 60:
    print("Selamat, kamu dapat nilai D")
else:
    print("Maaf, kamu dapat nilai E. Kamu harus ikut ujian remedial ")


angka = [1, 2, 3, 4, 5]
for x in angka:
    print(x)

ulang = 10
i = 1
for i in range(ulang):
    print "Perulangan ke-"+str(i)

# perulangan menurun
for i in range(10, 0, -1):
    print(i)


name = 'John Doe'
message = "John Doe belajar bahasa python di Belajarpython"
print("name: ", name[0])
# perhuruf
print("message: ", message[5:8])

list = ['fisika', 'kimia', 1993, 2017]
print(list)
print("Nilai ada pada index 2 : ", list[2])
list[2] = 2001
print("Nilai baru ada pada index 2 : ", list)

print '{%s} pergi ke %s' % ('bapak', 'kantor')

print '{0} pergi ke {1}'.format('ibu', 'pasar')

print 'jumlah total: %10.3f' % 10.3333

print 'jumlah total: {0:10.3f}'.format(10.3333)

# tidak ada bedanya petik satu dan petik dua
# lat16.py


def halo(nama):
    print 'Halo %s!' % nama

# dollar hrs diikuti parameter dibagian paling belakang


def cetak_maksimal(a, b):

    if a > b:

        print '%s merupakan nilai maksimal' % a

    elif a == b:

        print '%s sama dengan %s' % (a, b)

    else:

        print '%s merupakan nilai maksimal' % b


halo('Dunia')  # memanggil fungsi halo dengan argumen 'Dunia'

halo('Indonesia')  # memanggil fungsi halo dengan argumen 'Indonesia'

cetak_maksimal(9, 100)
x = 9
y = 9

cetak_maksimal(x, y)

# value key kyk di array ini namanya set
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

i = [1, 2, 3, 4, 5]
j = ('a', 'b', 'c', 'd', 'e')

for elem in i:
    print(elem)

for elem in j:
    print(elem)


a = [1, 2, 3, 4, 5]

# built-in function di python untuk operasi list
jumlah = sum(a)
print 'jumlah', jumlah
