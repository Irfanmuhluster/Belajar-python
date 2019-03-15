a = [3, 2, 1, 5, 4, 3, 3]

print(a)

# tukar
a.reverse()
print(a)

a.sort()
print(a)

# hitung banyaknya suatu elemen yang mirip
ew = a.count(3)
print('elemen yg sama',ew)

# melihat indeks
print(a.index(4))
print(a.index(5))

# menambah isi ilst
a.append(10)
print(a)

# menghapus elemen dari list dimulai dari urutan terakhir
a.pop()
print(a)

# menyisipkan elemen pada indeks tertentu ke list
# (index, angka yg disisipkan)
a.insert(2, 20)
print(a)