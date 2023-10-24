from django.core.exceptions import PermissionDenied, BadRequest
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError
from django.shortcuts import render, redirect

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Категории', 'url_name': 'category'},
        # {'title': 'Логин', 'url_name': 'home'},
]

# для хранения представления
# Create your views here.

data_db = [{'id':1, 'title': 'Гришин Никита Сергеевич', 'intersting': 'Литература, музыка, фотография, вязание, программирование', 'is_sport': False},
           {'id':2, 'title': 'Ушаков Никита Юрьевич', 'intersting': 'Плавание, Туризм, Бокс', 'is_sport': True},
           {'id': 3, 'title': 'Солодкий Никита Олегович', 'intersting': 'Игры, велосипед, тренажерный зал', 'is_sport': True},

           ]

def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            }
    return render(request, "women/index.html", context= data)

def category(request):
    data = {'title': 'Категории',
            'menu': menu,
            }
    return render(request, "women/category.html", context= data)

def about(request):
    data = {'title': 'О сайте',
            'menu': menu,
            }
    return render(request, "women/about.html", context= data)

#404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Старница не найдена :(</h1>')

#500
def errorServer(request):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')

#400
def accessDenied(request, exception):
    return HttpResponseBadRequest('<h1>Доступ запрещен</h1>')

#403
def unableToProcessRequest(request, exception):
    return HttpResponseForbidden('<h1>Невозможно обработать запрос</h1>')