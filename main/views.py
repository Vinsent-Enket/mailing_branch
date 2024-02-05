import random

from django.shortcuts import render
from django.views.decorators.cache import cache_page

from blog.models import Blog
from mailing_services.models import Mailing, Client


def index(request):
    """Реализуйте главную страницу в произвольном формате, но обязательно отобразите следующую информацию:
количество рассылок всего,
количество активных рассылок,
количество уникальных клиентов для рассылок,
3 случайные статьи из блога.
def get_count_mailing():
    return Mailing.objects.count()


def get_active_mailing():
    return Mailing.objects.filter(status='START').count()"""
    mailing_cont = Mailing.objects.count()
    mailing_active_cont = Mailing.objects.filter(status='in_work').count()
    users_uniq = Client.objects.values('email').distinct().count()

    blogs_news_count = Blog.objects.count()
    blog_news = []
    """ Улучшить выбор 3ех рандомных новостей чтобы не было повторов
     first() and last()
    Метод first() возвращает первый элемент из QuerySet."""
    if blogs_news_count != 0:
        for i in range(3):
            a = random.randint(1, blogs_news_count)

        blog_news.append(Blog.objects.get(pk=a))
    context = {
        'mailing_count': mailing_cont,
        'mailing_active_cont': mailing_active_cont,
        'users_uniq': users_uniq,
        'blog_news': blog_news,
    }
    return render(request, 'main/index.html', context)
