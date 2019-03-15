ini_baris = 'NAME="CentOS Linux"'
print(f'ini baris : {ini_baris}')
output2 = ini_baris.strip().split('=')[1].title()
# strip menghilangkan split utk mengetahui posisi, sebenarnya kan
# split utk menjdkan array'''
print(f'NAME: {output2}')  # default pemisah (, adalah spasi)
