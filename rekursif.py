def rekursif(angka):
    if angka > 0 :
        print (angka)
        angka = angka - 1
        rekursif(angka)
    else :
        print(angka)
masukan = int(input("masukkan angka : "))
rekursif(masukan)