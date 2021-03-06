import math
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
    
#words = []
#_score = {}
_score = []

def countTFIDF(word, doc):
    words = word
    score = [[] for k in range(len(words))]
    score = countTF(words, doc, score)
    score = countDF(words, doc,score)
    score = countIDF(words, doc, score)
    score = countW(words, doc, score)
    _score = score
    kolom = []
    #Menampilkan dalam bentuk tabel
    for i in range(len(doc)):
        kolom.append("d{}".format(i))
    kolom.append("DF")
    kolom.append("IDF")
    for i in range(len(doc)):
        kolom.append("W[d{}]".format(i))
    dframe = pd.DataFrame(_score, columns=kolom)
    return dframe

def makeWords(dokumen):
    termOfDoc = []
    for word in dokumen:
        if word not in termOfDoc:
            termOfDoc.append(word)
    return termOfDoc

def countTF(words, doc, score):
    #Fungsi untuk menghitung TF(frekuensi kemunculan kata pada tiap dokumen)
    #Fungsi ini bekerja dengan menyocokkan semua kata kunci dengan setiap kata pada tiap dokumen
    #Jika kata pada dokumen sama dengan kata kunci maka akan menambah skor tf
    #Skor akan disimpan sementara pada variabel freq_term kemudian hasilnya akan disimpan pada _score
    j = 0
    freq_term = 0
    for word in words:
        for i in range(len(doc)):
            for wordfreq in doc[i]:
                if word == wordfreq:
                    freq_term += 1
            score[j].append(freq_term)
            freq_term = 0
        j += 1
    return score
    #EndofFunc
    

def countDF(words, doc, score):
    #Fungsi untuk menghitung DF
    #Untuk semua kata yang terdapat pada kata kunci akan dilakukan pengecekan jika dokumen tersebut memiliki kata tersebut
    #Hasil DF akan disimpan kedalam variabel _score
    i = 0
    j = 0
    df = 0
    for word in words:
        for i in range(len(doc)):
            for term in doc[i]:
                if word == term:
                    df += 1
        score[j].append(df)
        df = 0
        j += 1
    return score
    #EndofFunc
    

def countIDF(words, doc, score):
    #Fungsi untuk menghitung IDF dari tiap kata
    idf = 0
    for word in range(len(words)):
        idf = math.log10(len(doc)/score[word][len(doc)])+1
        num = '{:.3f}'.format(idf)    
        score[word].append(float(num))
        idf = 0
    return score
    #EndofFunc


def countW(words, doc, score):
    #Fungsi untuk menghitung bobot kata dengan w = tf * idf
    w = 0
    for word in range(len(words)):       
        for i in range(len(doc)):
            w = score[word][i] * float(score[word][len(doc)+1])
            num =float('{:.3f}'.format(w)) 
            score[word].append(num if num != 0 else 0)
            w = 0
    return score
    #EndofFunc

def wordtfidf(words, tfidf, doc):
    #Fungsi untuk mendapatkan bobot dari kata baru terhadap hasil pembobotan sebelumnya
    weight = []
    for j in range(len(words)):
        if words[j] in doc:
            weight.append(tfidf['IDF'][j])
        else :
            weight.append(0)
    return weight
"""countTF(words, doc)
countDF(words, doc)
countIDF(words)
countW(words, doc)
"""
     
    

