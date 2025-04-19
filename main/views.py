from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request): #это переменные
    context = {
        'title': 'Home',
        'content': 'Главная страница - HOME',

    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home',
        'content': 'Это страница о нас ',
        'text_on_page': 'Страница о нас магазина Home',
    }
    return render(request, 'main/about.html', context)

