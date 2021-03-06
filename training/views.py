from django.shortcuts import render, redirect
from .models import Dataset

# Create your views here.
def index(request):
    hasil = Dataset.objects.all()
    
    context = {
        'title':'Dataset',
        'data':hasil
    }
    if request.user.is_authenticated():
        return render(request, 'training/index.html', context)
    else :
        return redirect('home')

    #konten = "Test123!!!"
    #label = "Bukan Clickbait"
    #import pandas as pd
    #konten = []
    #label = []
    #df = pd.read_csv(r"C:\Users\awangt\Desktop\dataset.csv",sep="_",engine='python')
    #for item in df['Doc']:
    #    konten.append(item)
    #for item in df['Type']:
    #    label.append(item)
    #print(label)
    #if konten and label:
    #    for i in range(len(konten)):
    #        obj = Dataset.objects.create(konten=konten[i], label=label[i])
    #        obj.save()