from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'DjangoApplication/index.html', {"title": "Main page"})

def about(request):
    return render(request, 'DjangoApplication/about.html', {"title": "About page"})

def click(request):
   return render(request, 'DjangoApplication/click.html', {"title": "Сlick page"})

