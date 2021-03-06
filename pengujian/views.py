from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import dataUji

# Create your views here.
def index(request):
    hasil = dataUji.objects.raw('SELECT * FROM `pengujian` WHERE model="SVM-PSO"')
    result = dataUji.objects.raw('SELECT * FROM `pengujian` WHERE model="SVM"')
    dump = {}
    data1 = []
    i = 1
    for item in result:
        dump = {'id_pengujian':i, 'tanggal':item.tanggal,'total_dataset':item.total_dataset, 'data_train': item.data_train, 'data_test':item.data_test, 'presisi':item.presisi, 'recall':item.recall, 'akurasi':item.akurasi}
        data1.append(dump)
        i = i+1
    context = {
        'title': 'Data Hasil Pengujian',
        'data': hasil,
        'data1':data1,
    }
    if request.user.is_authenticated():
        return render(request, 'pengujian/index.html', context)
    else :
        return redirect('home')

class table(TemplateView):
      template_name = 'index.html'

      def get_context_data(self, **kwargs):
            ctx = super(table, self).get_context_data(**kwargs)
            ctx['header'] = ['#', 'chemblID','Preferable Name']
            ctx['rows'] = [{'id':1, 'chemblid':534988,'prefName':'A'},
                           {'id':2, 'chemblid':31290,'prefName':'B'},
                           {'id':3, 'chemblid':98765,'prefName':'C'}]
            return ctx

"""
import pickle
    from datetime import date
    
    tanggal = date.today()
    accopt = pickle.load(open(r"C:\Dev\Django\mywebsite\pickles\acc-opt.sav", "rb"))
    presopt = pickle.load(open(r"C:\Dev\Django\mywebsite\pickles\pres-opt.sav", "rb"))
    recopt = pickle.load(open(r"C:\Dev\Django\mywebsite\pickles\recall-opt.sav", "rb"))
    acc = pickle.load(open(r"C:\Dev\Django\mywebsite\pickles\acc.sav", "rb"))
    pres = pickle.load(open(r"C:\Dev\Django\mywebsite\pickles\pres.sav", "rb"))
    rec = pickle.load(open(r"C:\Dev\Django\mywebsite\pickles\recall.sav", "rb"))
    for i in range(len(accopt)):
        obj = dataUji.objects.create(tanggal=tanggal, total_dataset=3797, data_train=3037, data_test=760, presisi=presopt[i]*100, recall=recopt[i]*100, akurasi=accopt[i]*100, model="SVM-PSO")
        obj.save()
    for i in range(len(accopt)):
        obj = dataUji.objects.create(tanggal=tanggal, total_dataset=3797, data_train=3037, data_test=760, presisi=pres[i]*100, recall=rec[i]*100, akurasi=acc[i]*100, model="SVM")
        obj.save()
"""