print('GEROBAK FRIED CHICKEN')
print('-'*50)


print('Kode  JenisPotong  Harga')
print('-'*50)
print('D     Dada         Rp.2500')
print('P     Paha         Rp.2000')
print('S     Sayap        Rp.1500')
print('-'*50)


data_pesanan= []
total_harga = 0

banyakjenis = int(input('Masukkan Banyak Jenis Potong yang Dibeli : '))
for i in range(banyakjenis) :
    print(f'\nJenis ke - {i+1}')
    kode = input('Masukkan Jenis Potong (D/P/S) : ').upper()

    while kode not in ['D', 'P', 'S']:
        print("Kode tidak valid! Silakan masukkan D, P, atau S")
        kode = input("Kode Potong [D/P/S] : ").upper()
    
    banyak_potong = int(input('Masukkan Banyak Potongan yang Dibeli : '))

    if kode == 'D':
        harga = 2500
        jenis = 'Dada'
    elif kode == 'P':
        harga = 2000
        jenis = 'Paha'
    else:
        harga = 1500
        jenis = 'Sayap'
    
    jumlah_harga = harga * banyak_potong
    total_harga += jumlah_harga

    data_pesanan.append({
    'jenis': jenis,
    'harga': harga,
    'banyak': banyak_potong,
    'jumlah': jumlah_harga
    })

pajak = total_harga * 0.1
total_bayar = total_harga

print('\n'+'='*50)
print('GEROBAK FRIED CHICKEN')
print('='*50)
print('No.\tJenis\t\tHarga\tBanyak\tJumlah')
print('\tPotong\t\tSatuan\tBeli\tHarga')
print('-'*50)

for i, pesanan in enumerate(data_pesanan, 1):
    print(f"{i}\t{pesanan['jenis']}\t\tRp. {pesanan['harga']}\t\t{pesanan['banyak']}\t\tRp. {pesanan['jumlah']}")
    
print('-'*50)
print(f'\t\t\t\tJumlah Bayar : Rp.{total_harga}')
print(f'\t\t\t\tPajak 10%    : Rp.{int(pajak)}')
print(f'\t\t\t\tTotal Bayar  : Rp.{int(total_bayar)}')