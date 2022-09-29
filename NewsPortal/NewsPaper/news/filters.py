from django_filters import FilterSet, ModelMultipleChoiceFilter, DateFilter
from django.forms.widgets import DateInput
from .models import Post, News, Article, Category

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.


class PostFilter(FilterSet):

    category = ModelMultipleChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Categories',
        conjoined=True,
    )
    post_date = DateFilter(
        lookup_expr=('gt'),
        widget=DateInput(
            attrs={'type': 'date'}))

    class Meta:
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'post_title': ['icontains'],
        }