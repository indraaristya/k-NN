from numpy import genfromtxt
import numpy as np

dataTrain = genfromtxt('DATA_TRAIN.csv',delimiter=',')
dataTest = genfromtxt('DATA_TEST.csv',delimiter=',')
dataTesting = genfromtxt('DATA_TESTING.csv',delimiter=',')

#Like 0
#Provokasi 1
#Komentar 2
#Emosi 3
#Hoax 4
#k=59

hasilManhattan = 0
manhattanTemp = [] * 10000
hasilnya = [0] * 4000 #untuk testing
#hasilnya = [0] * 3500 #untuk validasi
trainRow = 0
validRow = 0
i = 0
kNN = 0
kesimpulan = 0
arraykNN = [0] * 59
countHoax = 0
countTdk = 0

def manhattan(x,y):
    hasil = x - y
    if (hasil < 0):
        hasil = -1*hasil
    return hasil

#---------CODE UNTUK VALIDASI---------#
# for validRow in range(0,500):
#     for trainRow in range(0,3499):
#         like = manhattan((dataTrain[trainRow, 0]), (dataTest[validRow, 0]))
#         provo = manhattan((dataTrain[trainRow,1]),(dataTest[validRow,1]))
#         komen = manhattan((dataTrain[trainRow,2]),(dataTest[validRow,2]))
#         emosi = manhattan((dataTrain[trainRow,3]),(dataTest[validRow,3]))
#         #print(i)
#         hasilnya[i] = like + provo + komen + emosi
#         i=i+1
#         if (i == 3499):
#             arrayManhattan = np.array(hasilnya)
#             indexSorted = np.argsort(arrayManhattan)
#             list.sort(hasilnya)
#             # print(arrayManhattan)
#             # print(indexSorted)
#
#             while (kNN < 58):
#                 arraykNN[kNN] = dataTrain[indexSorted[kNN],4]
#                 #print(arraykNN[kNN])
#                 if (arraykNN[kNN] == 0.0):
#                     countTdk = countTdk + 1
#                 elif (arraykNN[kNN] == 1.0):
#                     countHoax = countHoax + 1
#                 kNN = kNN + 1
#             if (countTdk > countHoax):
#                 ht = 0
#             elif (countTdk < countHoax):
#                 ht = 1
#             #print("KNN: ",kNN)
#             #print(countTdk, " ",countHoax," ",ht)
#             print(ht)
#
#             kNN = 0
#             i = 0
#             countHoax = 0
#             countTdk = 0

#print(indexSorted)
#print(validRow)


#---------CODE UNTUK TESTING---------#
for testRow in range(0,1000):
    for trainRow in range(0,3999):
        like = manhattan((dataTrain[trainRow, 0]), (dataTesting[testRow, 0]))
        provo = manhattan((dataTrain[trainRow,1]),(dataTesting[testRow,1]))
        komen = manhattan((dataTrain[trainRow,2]),(dataTesting[testRow,2]))
        emosi = manhattan((dataTrain[trainRow,3]),(dataTesting[testRow,3]))
        hasilnya[i] = like + provo + komen + emosi #perhitungan distance ditampung pada array hasilnya.
        i=i+1
        if (i == 3999):
            arrayManhattan = np.array(hasilnya)
            indexSorted = np.argsort(arrayManhattan) #melakukan sorting ascending pada indeks dari data distance
            list.sort(hasilnya) #melakukan sorting ascending pada data distance

            while (kNN < 58):
                arraykNN[kNN] = dataTrain[indexSorted[kNN],4] #menyimpan label kelas dari 59 data terkecil
                if (arraykNN[kNN] == 0.0):
                    countTdk = countTdk + 1
                elif (arraykNN[kNN] == 1.0):
                    countHoax = countHoax + 1
                kNN = kNN + 1
            if (countTdk > countHoax):
                kesimpulan = 0
            elif (countTdk < countHoax):
                kesimpulan = 1

            print(kesimpulan)

            kNN = 0 #reset variabel yang digunakan dalam program untuk perulangan
            i = 0
            countHoax = 0
            countTdk = 0