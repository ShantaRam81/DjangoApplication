from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from DjangoApplication.models import News
from DjangoApplication.forms import NewsForm



# Create your views here.

def index(request):
    l_news = News.objects.all()
    return render(request, 'DjangoApplication/index.html', {'l_news': l_news, 'title': 'Список новостей'})

def about(request):
    return render(request, 'DjangoApplication/about.html', {"title": "About page"})

def click(request):
   return render(request, 'DjangoApplication/click.html', {"title": "Сlick page"})

def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'DjangoApplication/news_detail.html', {'news': news})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.create_at = timezone.now()
            news.save()
            return redirect('news_detail', news.id)
    else:
        form = NewsForm()
    data = {'form': form}
    return render(request, 'DjangoApplication/add_news.html', data)

def edit_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_detail', news.id)
    else:
        form = NewsForm(instance=news)
    return render(request, 'DjangoApplication/add_news.html', {'form': form, 'news': news})

