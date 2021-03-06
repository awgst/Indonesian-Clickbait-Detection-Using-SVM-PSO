#import string untuk melakukan fungsi translate(digunakan untuk menghapus tanda baca)
import string
#import pandas untuk membaca file dataset dalam bentuk csv
import pandas as pd
#Menggunakan Regular expression
import re

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


#Fungsi CaseFolding
def caseFolding(kalimat):
    kalimat = kalimat.lower()
    return kalimat
#Fungsi Cleansing
def cleansing(kalimat):
    tokens = kalimat.split()
    for kata in tokens:
        if "-" in kata:
            index = kata.index("-")
            kata_b = kata[:index]
            kalimat = kalimat.replace(kata,kata_b)
    kalimat = kalimat.translate(str.maketrans('','',string.punctuation))
    kalimat = re.sub(r"\d+", "", kalimat)
    kalimat = kalimat.strip()
    return kalimat
#Fungsi 
#Fungsi Tokenizing
def tokenizing(kalimat):
    tokens = kalimat.split()
    return tokens
#Fungsi filtering untuk menghapus stopword
def filtering(kata):
    f = open(r"C:\Dev\Module\stopword.txt", mode='r')
    file = f.readlines()
    listStopword = []
    for i in file:
        temp = i.replace("\n","")
        listStopword.append(temp)
    result = []
    for t in kata:
        if t not in listStopword:
            result.append(t)
    f.close()
    return result
#Fungsi untuk mengganti kata
def wordConversion(kalimat):
    kal = pd.read_csv(r"C:\Users\awangt\Desktop\word.csv",error_bad_lines=False, warn_bad_lines=False)
    kata_awal = []
    kata_ganti = []
    for i in range(len(kal)):
        kata_awal.append(kal['Awal'][i])
        kata_ganti.append(kal['Ganti'][i])
    for i in range(len(kalimat)):
        for j in range(len(kata_awal)) :
            if kalimat[i] == kata_awal[j]:
                kalimat[i] = kata_ganti[j]
    return kalimat                        
#Fungsi Stemming menggunakan sastrawi
def wordStemming(kalimat) :
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    hasil = []
    for kata in kalimat:
        hasil.append(stemmer.stem(kata))
    return hasil
    

