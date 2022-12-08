print('~ Halo Selamat Datang di Kalkulator Sederhana ~')
x = input('Masukkan operator matematika yang ingin Anda hitung: ')
while True:
    if x == '+':
        a = int(input('Mau penjumlahan berapa: '))
        b = int(input('Print berapa banyak: '))
        for i in range(b):
            print(f'{i+1} + {b-i} = {(i+1)+(b-i)}')
    elif x == '-':
        a = int(input('Mau pengurangan berapa: '))
        b = int(input('Print berapa banyak: '))
        for i in range(b):
            print(f'{i+1} + {b-i} = {(i+1)-(b-i)}')
    elif x in ('x', 'X'):
        a = int(input('Mau perkalian berapa: '))
        b = int(input('Print berapa banyak: '))
        for i in range(b):
            print(f'{i+1} X {b-i} = {(i+1)*(b-i)}')
    elif x == ':':
        a = int(input('Mau pembagian berapa: '))
        b = int(input('Print berapa banyak: '))
        for i in range(b):
            print(f'{i+1} : {b-i} = {(i+1)/(b-i)}')
    else:
        print('Maaf, Operator Matematika yang Anda cari  tidak tersedia.')
        break
    pernyataan = input(' Ingin Menghitung Lagi? (Y/T): ')
    if pernyataan in ('T', 't'):
        print('Terima Kasih ')
        break
    elif pernyataan in ('Y', 'y'):
        continue
    else:
        print('ERROR\nPilih Y atau T\nUlangi Program')
        break