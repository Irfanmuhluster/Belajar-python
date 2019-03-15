temps = [("Berlin",29),("Cairo",36),("Tokyo",23),("Beijing",21),("Hongkong",29)]
c_to_f = lambda data : (data[0],(9/5)*data[1] + 32)
oke = list(map(c_to_f,temps))
print(oke)


conto = list(map(round, [12.3, 10.7, 5.2]))
print(conto)


# Lambda function dapat digunakan bersama method map() dan filter()
# lamda adalah sebuah ekpresi function tanpa nama
# syarat map tu ada operasi dan ada angkanya, DI TEMPERATURE ADA 2 DATA DIARRAY
#map untuk merubah filter untuk menyaring