from django import forms
from .models import News, Article, Category, PostCategory
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'post_author',
            'post_category',
            'post_title',
            'post_text',
        ]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'post_author',
            'post_category',
            'post_title',
            'post_text',
        ]
