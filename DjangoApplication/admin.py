from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ["title"]


admin.site.register(News)
admin.site.register(Category)