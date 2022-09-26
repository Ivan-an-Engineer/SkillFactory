from django.contrib import admin
from .models import Author, News, Article, Category, PostCategory, Comment

# Register your models here.
admin.site.register(Author)
admin.site.register(News)
admin.site.register(Article)
admin.site.register(Category),
admin.site.register(PostCategory)
admin.site.register(Comment)