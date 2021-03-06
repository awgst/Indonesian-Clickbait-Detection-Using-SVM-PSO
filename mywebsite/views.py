from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from json import dumps
from riwayat.models import dataCek
def index(request):
    context ={
        'title':'Home',
        'heading':'Cek Clickbait!',
    }
    if request.user.is_authenticated():
        return redirect('dashboard')
    else :
        return render(request, 'index.html', context)

def loginView(request):
    context ={
        'title':'Login',
        'heading':'Login',
    }
    if request.method == 'POST':
        usernameku = request.POST['username']
        passwordku = request.POST['password']
        
        user = authenticate(request, username=usernameku, password=passwordku)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else :
            messages.add_message(request, messages.ERROR, "Login Gagal")
            return redirect('login')
    if request.method == 'GET':
        if request.user.is_authenticated():
            return redirect('dashboard')
        else :
            return render(request, 'login.html', context)
    

def logoutView(request):
    context ={
        'title':'Login',
        'heading':'Login',
    }
    lo = logout(request)
    return redirect('home')

    return render(request, 'logout.html', context)

def getPredict(request):
    if request.method == 'POST':
        from scipy.sparse import csr_matrix as matrixTransform
        from datetime import date
        import pickle
        import preProcessing as prepro
        import TermWeight as tw
        import time
        
        tanggal = date.today()

        judul = request.POST['judul']
        teksInput = judul
        #PreProcessing
        judul = prepro.caseFolding(judul)
        judul = prepro.cleansing(judul)
        judul = prepro.tokenizing(judul)
        judul = prepro.wordConversion(judul)
        judul = prepro.filtering(judul)
        judul = prepro.wordStemming(judul)
        #Load Model
        model = pickle.load(open(r"C:\Dev\Django\mywebsite\pickles\model.sav", "rb"))
        _words = pickle.load(open(r"C:\Dev\Django\mywebsite\pickles\words.sav", "rb"))
        tfidf = pickle.load(open(r"C:\Dev\Django\mywebsite\pickles\tfidf.sav", "rb"))
        #print(model)
        #Predict
        wjudul = tw.wordtfidf(_words, tfidf, judul)
        matriks = matrixTransform(wjudul)
        prediction_SVM = model.predict(matriks)
        probability = model.predict_proba(matriks)
        klasifikasi = "Judul Clickbait"
        klasifikasi2 = "Bukan Clickbait"
        # if probability[0][1] > probability[0][0] else "Bukan Clickbait"
        context = {
            'title':'Home',
            'heading':'Hasil Prediksi',
            'teksinput':teksInput,
            'prepro':judul,
            'predict':klasifikasi,
            'predict2':klasifikasi2,
            'probability':'{:.1f}'.format(probability[0][1]*100),
            'probability2':'{:.1f}'.format(probability[0][0]*100),
            'tfidf':wjudul,
        }
        time.sleep(5)
        if teksInput:
            obj = dataCek.objects.create(tanggal=tanggal, konten=teksInput, preprocessing=judul, tfidf=wjudul, klasifikasi=klasifikasi)
            obj.save()
    return render(request, "result.html", context)