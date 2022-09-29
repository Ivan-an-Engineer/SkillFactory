"""NewsPaper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from news.views import NewsList, NewsDetail, NewsCreate, NewsEdit, ArticleList, \
    ArticleDetail, ArticleCreate, ArticleEdit, PostDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    # Делаем так, чтобы все адреса из нашего приложения (news/urls.py)
    # подключались к главному приложению с префиксом news/.
    #    path('news/', include('news.urls')),
    #    path('news/create/', NewsCreate.as_view(), name='news_create'),
    #    path('articles/', include('article.urls')),
    #    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('news/', NewsList.as_view(), name='news_list'),
    path('news/<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/create/sign/', include('sign.urls')),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='post_edit'),
    path('news/<int:pk>/edit/sign/', include('sign.urls')),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('news/<int:pk>/delete/sign/', include('sign.urls')),
    path('articles/', ArticleList.as_view(), name='articles_list'),
    path('articles/<int:pk>', ArticleDetail.as_view(), name='articles_detail'),
    path('articles/create/', ArticleCreate.as_view(), name='articles_create'),
    path('articles/create/sign/', include('sign.urls')),
    path('articles/<int:pk>/edit/', ArticleEdit.as_view(), name='post_edit'),
    path('articles/<int:pk>/edit/sign/', include('sign.urls')),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('articles/<int:pk>/delete/sign/', include('sign.urls')),
]
