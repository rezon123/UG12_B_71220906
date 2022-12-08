angka = int(input("silahkan input nomor anda >>"))
print(' '*(angka-1),"*")
for angka2 in range ((angka-1),0,-1):
    print(' '*(angka2-1),"**")
print ("**"*angka)