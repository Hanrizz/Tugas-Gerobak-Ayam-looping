count = 0 
while (count < 5):
    print('The Count is: ', count)
    count = count + 1
print('Good Bye!')

count = 0
while (count < 8):
    print(count, 'Angka tidak lebih dari 8')
    count = count + 1
else:
    print(count, 'Angka lebih dari 8')


ulang = int(input('dikit aja pls!!'))
for i in range(ulang) :
    print ('data Ke - ' +str(i+1))
    nama = input('Masukka Nim Anda : ')
    uts = int(input('Masukkan Nilai UTS Anda : '))
    uas = int(input('Masukkan Nilai UAS Anda : '))
    
    print('-'*40)
print('NIM anda adalah %s nilai UTS anda %i nilai UAS anda %i' % (nama,uts,uas))