from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        'title':'About',
        'heading' : 'About',
        'subheading' : 'Sebuah website yang dibuat untuk melakukan pengecekan judul berita berbahasa Indonesia apakan merupakan sebuah judul berita clickbait atau bukan.',
    }
    if request.user.is_authenticated():
        return redirect('dashboard')
    else :
        return render(request, 'about/index.html', context)
    