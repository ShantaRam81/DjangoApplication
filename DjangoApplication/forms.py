from .models import News
from django.forms import ModelForm, TextInput, Textarea, Select, ImageField


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'autor', 'category', 'photo']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Контент статьи'
            }),
            "autor": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор статьи'
            }),
            "category": Select(attrs={
                'class': 'form-control',
            }),
        }