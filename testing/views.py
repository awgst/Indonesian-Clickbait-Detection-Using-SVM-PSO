from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context ={
        'title':'Data Testing',
    }
    if request.user.is_authenticated():
        return render(request, 'testing/index.html', context)
    else :
        return redirect('home')
        