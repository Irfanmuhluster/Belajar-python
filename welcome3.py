count = 0
while count < 5:
    print count, " is  less than 5"
    count = count + 1
else:
    print count, " is not less than 5"

# buat urutan data_tahun bertipe 'list'
data_tahun = []

# meminta masukan untuk memasukkan data tahun
pilihan = raw_input("Ingin input tahun (Y/N)? ")

# lakukan pengulangan while, sampai user
# memasukkan selain karakter Y.
while 1:
    # lakukan pengujian if, jika user meng-input Y/y
    if pilihan in ('y', 'Y'):
        # input tahun
        tahun = raw_input('Input data tahun: ')
        # masukkan input tahun ke list data_tahun
        data_tahun.append(int(tahun))
        # tawarkan input tahun yang lainnya
        pilihan = raw_input("Ingin input tahun lainnya (Y/N)? ")
    else:
        # jika user menginput selain Y/y, maka langsung
        # keluar dari pengulangan while
        break

# lakukan filter untuk memilih mana yang
# termasuk tahun kabisat, gunakan fungsi filter() tadikan yg dimasukkan banyak tahun tp yg dibutuhkan tahun kabisat saja pokoke gitulah
# memanggil lambda
tahun_kabisat = list(filter(lambda n: n % 4 == 0, data_tahun))

# tampilkan hasil filter tahun kabisat
print('Anda telah memasukkan %d tahun kabisat, yaitu \
%s' % (len(tahun_kabisat), tahun_kabisat))

# %s is for a string (char array).
# %d is for an integer (int).
# %f is for a float/double.
