print('PROGRAM HITUNG GAJIKARYAWAN')
print('-'*45)

#input data karyawan
nama_karyawan = input('Masukkan Nama Karyawan : ')
tunjangan_jabatan = (input('Masukkan Golongan Jabatan (1/2/3) : '))
tunjangan_pendidikan = input('Masukkan Pendidikan (SMA/D3/S1) : ')

#gaji pokok
gaji_pokok = 300000

#Hitung tunjangan jabatan
if tunjangan_jabatan == '1':
    tunjangan_jabatan = 0.05 * gaji_pokok
elif tunjangan_jabatan == '2':
    tunjangan_jabatan = 0.1 * gaji_pokok
elif tunjangan_jabatan == '3':
    tunjangan_jabatan = 0.15 * gaji_pokok
else:
    tunjangan_jabatan = 'Tidak Mendapatkan Tunjangan Jabatan'

#hitung tunjangan pendidikan
if tunjangan_pendidikan.upper() == 'SMA':
    tunjangan_pendidikan = 0.025 * gaji_pokok
elif tunjangan_pendidikan.upper() == 'D3':
    tunjangan_pendidikan = 0.2 * gaji_pokok
elif tunjangan_pendidikan.upper() == 'S1': 
    tunjangan_pendidikan = 0.3 * gaji_pokok
else:
    tunjangan_pendidikan = 'Tidak Mendapatkan Tunjangan Pendidikan'


#hitung honor lembur
jam_kerja = int(input('Masukkan Jumlah Jam Kerja : '))
if jam_kerja > 8:
    honor_lembur = (jam_kerja - 8) * 3500
else:
    honor_lembur = 0

#hitung total gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur

#tampilan hasil
print('\n')
print('Layar Keluaran')
print('-' * 45)
print(f'Karyawan yang bernama : {nama_karyawan}')
print('Honor yang diterima')
print(f'Tunjangan Jabatan\tRp : {tunjangan_jabatan:,.0f}')
print(f'Tunjangan Pendididkan\tRp : {tunjangan_pendidikan:,.0f}')
print(f'Honor Lembur\t\tRp : {honor_lembur:,.0f}')
print(f'\nTotal Gaji\t\tRp : {total_gaji:,.0f}')
print(f'(Gaji pokok + tunjangan + lembur)')