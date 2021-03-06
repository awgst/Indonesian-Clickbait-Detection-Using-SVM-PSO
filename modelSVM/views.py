from django.shortcuts import render, redirect
from pengujian.models import dataUji

import json
import numpy as np
import pickle

# Create your views here.
def index(request):
    hasil = dataUji.objects.values_list(flat=True)
    result =  np.zeros((len(hasil), 4))
    for i in range(5):
        result[i][0] = i+1
        result[i][1] = hasil.values_list('presisi', flat=True)[i]
        result[i][2] = hasil.values_list('recall', flat=True)[i]
        result[i][3] = hasil.values_list('akurasi', flat=True)[i]
    acc = pickle.load(open(r"C:\Dev\Django\mywebsite\pickles\acc.sav", "rb"))
    pres = pickle.load(open(r"C:\Dev\Django\mywebsite\pickles\pres.sav", "rb"))
    recall = pickle.load(open(r"C:\Dev\Django\mywebsite\pickles\recall.sav", "rb"))
    acc1 = pickle.load(open(r"C:\Dev\Django\mywebsite\pickles\acc-opt.sav", "rb"))
    pres1 = pickle.load(open(r"C:\Dev\Django\mywebsite\pickles\pres-opt.sav", "rb"))
    recall1 = pickle.load(open(r"C:\Dev\Django\mywebsite\pickles\recall-opt.sav", "rb"))
    data = np.zeros((len(acc),4))
    for i in range(len(acc)):
        data[i][0] = i+1
        data[i][1] = pres[i]*100
        data[i][2] = recall[i]*100
        data[i][3] = acc[i]*100
    #AVG SVM
    avg_acc1 = np.mean(acc)*100
    avg_pres1 = np.mean(pres)*100
    avg_recall1 = np.mean(recall)*100
    #AVG SVM-PSO
    avg_acc2 = np.mean(acc1)*100
    avg_pres2 = np.mean(pres1)*100
    avg_recall2 = np.mean(recall1)*100
    dump = []
    for i in range(5):
        dump.append(result[i].tolist())
    #print(dump)
    context ={
        'title':'Model Klasifikasi',
        'data':dump,
        'data2':data.tolist(),
        'acc1':avg_acc1,
        'pres1':avg_pres1,
        'recall1':avg_recall1,
        'acc2':avg_acc2,
        'pres2':avg_pres2,
        'recall2':avg_recall2,
    }
    if request.user.is_authenticated():
        return render(request, 'modelSVM/index.html', context)
    else :
        return redirect('home')