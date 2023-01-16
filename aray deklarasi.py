array = []
total = 0
n = int (input('Masukkan jumlah elemen array:'))
for x in range(n) :
    nilai =int(input('Masukkan nilai ke- {} :'.format(x+1)))
    array.append(nilai)
print('Semua nilainya adalah',array)
print('Hasil nilai total adalah : {}'.format(sum(array)))
print('Hasil rata rata nilai adalah : {}'.format(sum(array)/n))
