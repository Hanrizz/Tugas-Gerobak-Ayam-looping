'''print("He said,", "What's there?")'''
"""print('''He said, "What's there?"''')"""   #menggunakan '''
"""print('He said, "What\'s there?"') """     #menggunakan escape (\) untuk tanda kutip tunggal
'''print("He said, \"What's there?\"")'''     #menggunakan escape (\) untuk tanda kutip ganda

"""print("ini adalah \x48\x45\x78")"""

"""#menggunakan posisi default
default_order = "{}, {} dan {}".format("Anis", "Bowo", "Ganjar")
print('\n--- Urutan default ---')
print(default_order)

#menggunakan argjument posisi
positional_order = "{2}, {0} dan {1}".format("Anis", "Bowo", "Ganjar")
print('\n--- Urutan berdasarkan posisi ---')
print(positional_order)"""


#format integer
print("{0} bila di ubah jadi biner menjadi |{0:b}|".format(12))

#forat float
print("Format eksponensial: |{0:e}|".format(1566.345))

#meratakan string\
print("Sepertiga sama dengan:| {0:.3f}|".format (1/3))

#Pemulatan
print("|{:<10}|{:^10}|{:>10}|".format('beras', 'gula', 'garam'))



print('Universitas Bina Sarana Informatika'.lower())
print('Universitas Bina Sarana Informatika'.upper())
print("I Love Programming in Python".split())
print("I Love Python".startswith("I"))
print("Saya belajar Python".endswith("on"))
print(' - '.join(["I", 'love', 'you']))
print("Belajar Java di BSi".replace('Java', 'Python'))

string = 'I Love Python'
print(len(string))