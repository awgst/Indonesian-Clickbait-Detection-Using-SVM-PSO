from django.shortcuts import render, redirect
from .models import dataCek

# Create your views here.
def index(request):
    hasil = dataCek.objects.all()
    context = {
        'title' : 'Riwayat Cek Clickbait',
        'data' : hasil,
    }
    if request.user.is_authenticated():
        return render(request, 'riwayat/index.html', context)
    else :
        return redirect('home')

def hapusData(request):
    id_cek = request.GET.get('id_cek')
    dt = dataCek.objects.get(id_cek=id_cek)
    dt.delete()
    return redirect("/riwayat/")

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
        klasifikasi = "Judul Clickbait"# if probability[0][1] > probability[0][0] else "Bukan Clickbait"
        klasifikasi2 = "Bukan Clickbait"
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
    return render(request, "riwayat/adm-result.html", context)