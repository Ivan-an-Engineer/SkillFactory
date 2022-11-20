from django.shortcuts import render, reverse, redirect
from django.core.mail import send_mail
from news.models import Author, Category, Subscribers
from django.views import View
# Create your views here.


class SubscribeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'subscribe.html', {})

    def post(self, request, *args, **kwargs):
        subscriber = Subscribers(
            user=request.POST['user'],
            category=request.POST['category'],
        )
        subscriber.save()

        send_mail(
            subject=f'Вышла новость категории {subscriber.category}',
            messege='',
            from_email='IvanVavilov1997@yandex.com',  # здесь указываете почту, с которой будем отправлять
            recipient_list=[]  # здесь список получателей.
        )
        return redirect('subscribe:subscribe')
