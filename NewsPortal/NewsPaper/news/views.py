from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, News, Article
from .forms import NewsForm, ArticleForm
from .filters import PostFilter
from django.urls import reverse_lazy


class PostList(ListView):
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-post_date'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsList(PostList):
    # Указываем модель, объекты которой мы будем выводить
    model = News
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'post_list.html'
    news_or_article = 'новостей'


class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости
    model = News
    # Используем другой шаблон — post.html
    template_name = 'post.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'


class NewsCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = NewsForm
    # модель товаров
    model = News
    # и новый шаблон, в котором используется форма.
    template_name = 'news_create.html'


class NewsEdit(UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'news_create.html'


class ArticleList(PostList):
    # Указываем модель, объекты которой мы будем выводить
    model = Article
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'post_list.html'
    news_or_article = 'статей'


class ArticleDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости
    model = Article
    # Используем другой шаблон — post.html
    template_name = 'post.html'
    # Название объекта, в котором будет выбранная пользователем статья
    context_object_name = 'post'


class ArticleCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = ArticleForm
    # модель товаров
    model = Article
    # и новый шаблон, в котором используется форма.
    template_name = 'article_create.html'


class ArticleEdit(UpdateView):
    form_class = ArticleForm
    model = Article
    template_name = 'article_create.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news_list')
