from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from training.models import Dataset
from riwayat.models import dataCek
from pengujian.models import dataUji
# Create your views here.
def index(request):
    hasil = Dataset.objects.all()
    riwayat = dataCek.objects.all()
    data_uji = dataUji.objects.all()
    total_dataset = len(hasil)
    total_datacek = len(riwayat)
    total_datauji = len(data_uji)
    train = (total_dataset * 80) /100
    test = (total_dataset * 20) /100
    context = {
        'title':'Dashboard',
        'dataset':total_dataset,
        'train':round(train),
        'test':round(test),
        'riwayat':total_datacek,
        'datauji':total_datauji,
    }
    if request.user.is_authenticated():
        return render(request, 'dashboard/index.html', context)
    else :
        return redirect('home')
        