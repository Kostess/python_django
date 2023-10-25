from django.core.exceptions import PermissionDenied, BadRequest
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError
from django.shortcuts import render, redirect

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Категории', 'url_name': 'category'},
]

# для хранения представления
# Create your views here.

data_db = [{'id':1, 'FIO': 'Маганков Кирилл Александрович', 'intersting': 'плетение биссером, спорт, бокс, футбол', 'is_sport': True},
           {'id':2, 'FIO': 'Куленок Станислав Владимирович', 'intersting': 'плавание, ходьба скандинавская, шахматы', 'is_sport': False},
           {'id': 3, 'FIO': 'Короткая Софья Геннадьевна', 'intersting': 'конный спорт, литература, музыка, рисование', 'is_sport': True},
           {'id': 4, 'FIO': 'Ушаков Никита Юрьевич', 'intersting': 'вязание, шахматы, шашки', 'is_sport': False},
           ]

def index(request):
    data = {'title': 'Главная',
            'menu': menu,
            'posts': data_db,
            }
    return render(request, "women/index.html", context= data)

def category(request):
    data = {'title': 'Категории',
            'menu': menu,
            'posts': data_db,
            }
    return render(request, "women/category.html", context= data)

# def categorys(request):
#     data = {'title': 'Категории',
#             'menu': menu,
#             'posts': data_db,
#             }
#     return render(request, "women/category.html", context= data)

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