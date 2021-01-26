'''
Irvin Andryan P. / 13519162
IF 2211 K-03
Tugas Kecil 1 Cryptarithmetic Problem
'''

import time
import os

#--------membuka file input dan memasukkan isinya ke dalam listOfContain
os.chdir("..")
inputFile = open("test/textinput1.txt", "r")
isiFile = inputFile.read()
listOfContain = isiFile.split("\n")
inputFile.close()

#--------membentuk list yang berisi operand
listOperand = [''] * (len(listOfContain) - 2)
for i in range(len(listOfContain) - 2):
    listOperand[i] = listOfContain[i]
listOperand = [s.replace('+', '') for s in listOperand] #menghapus tanda +
listOperand = [s.strip(' ') for s in listOperand] #menghapus space kosong

#--------menyimpan hasil dalam variabel "hasil"
hasil = listOfContain[len(listOfContain) - 1]


def solver (operand, hasil):

    startTime = time.perf_counter()
    #--------membentuk listOfKata berisi hanya operand dan hasil tanpa tanda '+' dan '-----'
    listOfKata = [0 for i in range(len(listOperand) + 1)]
    for i in range(len(listOperand)):
        listOfKata[i] = listOperand[i]
    listOfKata[len(listOfKata) - 1] = hasil

    #--------membentuk list hurufUnik berisi huruf-huruf unik yang ada
    hurufUnik = []
    for i in range(len(listOfKata)):
        for j in range(len(listOfKata[i])):
            if (listOfKata[i][j] not in hurufUnik):
                hurufUnik.append(listOfKata[i][j])

    #--------membentuk list berisi huruf-huruf awal kata
    hurufAwal = []
    for i in range(len(listOfKata)):
        if(listOfKata[i][0] not in hurufAwal):
            hurufAwal.append(listOfKata[i][0])

    counter = 0 #menghitung banyak percobaan

    stringOfDigit = '1234567890'
    initialNumber = ''
    for dig in range(len(hurufUnik)):
        initialNumber += stringOfDigit[dig]
    i_unik = int(initialNumber)


    while(i_unik < 10**(len(hurufUnik))):
        angkaUnik = [] #list untuk menyimpan angka yang digunakan
        num = str(i_unik)
        j_unik = 0
        masihbenar = True
        while(j_unik < len(num) and masihbenar == True):
            if (hurufUnik[j_unik] in hurufAwal and num[j_unik] == '0'):
                    #print(num[j_unik])
                    masihbenar = False #ketika angka di index n pada list angkaUnik = 0 dan huruf di index n pada list hurufUnik merupakan huruf pertama suatu kata
            else:
                if(num[j_unik] not in angkaUnik):
                    angkaUnik.append(num[j_unik])
                    j_unik += 1
                else:
                    masihbenar = False

        if (masihbenar == True):
            #menggabungkan angka-angka dari list angkaUnik ke dalam listOfString angka sesuai urutan kemunculan huruf pada suatu kata
            listOfStringAngka = ['' for i in range(len(listOfKata))]
            for i in range(len(listOfKata)):
                for j in range(len(listOfKata[i])):
                    idx = hurufUnik.index(listOfKata[i][j])
                    listOfStringAngka[i] += str(angkaUnik[idx])

            result = int(listOfStringAngka[len(listOfStringAngka)-1])
            total = 0
            #menjumlahkan
            for i in range(len(listOfStringAngka) -1):
                total += int(listOfStringAngka[i])
            if(total == result):
                #output
                for i in range(len(listOfStringAngka) -1):
                    if (i == len(listOfStringAngka) - 2):
                        print(listOperand[i].rjust(5),'+',end = ' '.rjust(8))
                        print(listOfStringAngka[i].rjust(10),'+')
                    else:
                        print(listOperand[i].rjust(5), end = ' '.rjust(10))
                        print(listOfStringAngka[i].rjust(10))
                print("-------".rjust(5), end = ' '.rjust(10))
                print("-------".rjust(10))
                print(hasil.rjust(5), end = ' '.rjust(10))
                print((listOfStringAngka[len(listOfStringAngka)-1]).rjust(10))

                
                durasi = time.perf_counter() - startTime
                print("waktu proses : %.5f detik" % durasi)
                print("jumlah percobaan : %d kali" % counter)
                break
            else:
                counter += 1
                i_unik += 1
        else:
            i_unik += 1


solver(listOperand, hasil)





            
