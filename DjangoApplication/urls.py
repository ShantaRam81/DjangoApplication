
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('click', views.click, name='click'),
    path('add_news', views.add_news, name='add_news'),
    path('news/<int:news_id>', views.news_detail, name='news_detail'),
    path('news/<int:news_id>/edit', views.edit_news, name='edit_news'),
]
