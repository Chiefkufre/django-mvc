from django.contrib import admin

# Register your models 

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['content']
    list_display = ['id', 'title']

admin.site.register(Article, ArticleAdmin)
