# buka file
file_puisi = open("puisi.txt", "r")

# baca isi file
puisi = file_puisi.readlines()

for teks in puisi:
    print(teks)

# tutup file
file_puisi.close()
