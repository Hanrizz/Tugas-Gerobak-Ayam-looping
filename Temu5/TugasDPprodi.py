nis = int(input('Masukkan NIS anda: '))
nm = input('Masukkan Nama Lengkap Anda: ')
prodi = input('Pilih Jurusan Anda (SI/SIA): ')


if prodi.upper() == 'SI':
    hrg = 2400000
    jurusan = 'Sistem Informasi' 
elif prodi.upper() == 'SIA':
    hrg = 2000000
    jurusan = 'Sistem Informasi AKuntansi'
else:
    jurusan = 'Jurusan Tidak di Temukan!!!'
    hrg = 0

print('='*40)
print('NIS : ',nis)
print('Nama Mahasiswa : ', nm)
print('Jurusan : ', prodi.upper (), '-', jurusan)
print(f'Harga : {hrg:,.0f}')
print('=='*20)