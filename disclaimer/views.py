from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        'title':'Disclaimer',
        'heading' : 'Disclaimer',
        'subheading' : 'Semua hasil prediksi belum tentu menjamin kebenarannya...',
    }
    if request.user.is_authenticated():
        return redirect('dashboard')
    else :
        return render(request, 'disclaimer/index.html', context)
    