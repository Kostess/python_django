from django.core.exceptions import PermissionDenied, BadRequest
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404

from .models import Book

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Категории', 'url_name': 'category'},
        {'title': 'Список книг', 'url_name': 'categoryBook'},
        {'title': 'Список книг ID', 'url_name': 'categoryBookID'},
]

# для хранения представления
# Create your views here.

data_db = [{'id': 1, 'FI': 'Андрюхин Даниил', 'url': 'Andruhin', 'img': 'women/images/Andruhin.jpg', 'intersting': ('плетение биссером, '
                                                                                             'спорт, '
                                                                                       'бокс, '
                                                                                 'футбол'), 'is_sport': True},
           {'id': 2, 'FI': 'Андронов Назар', 'url': 'Andronov', 'img': 'women/images/Andronov.PNG', 'intersting': 'плавание, '
                                                                                          'ходьба скандинавская',
            'is_sport': False},
           {'id': 3, 'FI': 'Асадов Наил', 'url': 'Asadov', 'img': 'women/images/Asadov.PNG', 'intersting': 'конный спорт, литература, музыка, '
                                                                          'рисование', 'is_sport': True},
           {'id': 4, 'FI': 'Виноградский Иван', 'img': 'women/images/Vinogradskiy.PNG', 'url': 'Vinogradskiy', 'intersting': 'вязание, шахматы, шашки',
            'is_sport': True},
           {'id': 5, 'FI': 'Гришин Никита', 'img': 'women/images/Grishin.PNG', 'url': 'Grishin', 'intersting': 'вязание, шахматы, шашки', 'is_sport':
               True},
           {'id': 6, 'FI': 'Ковалев Егор', 'img': 'women/images/Kovalev.PNG', 'url': 'Kovalev', 'intersting': 'вязание, шахматы, шашки', 'is_sport':
               False},
           {'id': 7, 'FI': 'Короткая София', 'img': 'women/images/Korotkaya.jpg', 'url': 'Korotkaya', 'intersting': 'вязание, шахматы, шашки',
            'is_sport': False},
           {'id': 8, 'FI': 'Куленок Станислав', 'img': 'women/images/Kuzhelny.PNG', 'url': 'Kyzhelny', 'intersting':
               'вязание, шахматы, шашки',
            'is_sport': False},
           {'id': 9, 'FI': 'Палий Константин', 'img': 'women/images/Paliy.jpeg', 'url': 'Paliy', 'intersting': 'вязание, шахматы, шашки', 'is_sport':
               False},
           {'id': 10, 'FI': 'Покровский Даниил', 'img': 'women/images/Pokrovskiy.PNG', 'url': 'Pokrovsky', 'intersting': 'вязание, шахматы, шашки',
            'is_sport': False},
           {'id': 11, 'FI': 'Солодкий Никита', 'img': 'women/images/Solodkiy.jpg', 'url': 'Solodky', 'intersting': 'вязание, шахматы, шашки',
            'is_sport': True},
           {'id': 12, 'FI': 'Ушаков Никита', 'img': 'women/images/Ushakov.jpg', 'url': 'Ushakov', 'intersting': 'вязание, шахматы, шашки', 'is_sport':
               False},
           {'id': 13, 'FI': 'Маганков Кирилл', 'img': 'women/images/Magankov.jpeg', 'url': 'Mangankov', 'intersting': 'вязание, шахматы, '
                                                                                              'шашки', 'is_sport': True},
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

def student(request, name):
    data = {
        'name_student': name,
        'menu': menu,
        'posts_student': data_db,
    }
    return render(request, "women/studentCard.html", context= data)

def about(request):
    data = {'title': 'О сайте',
            'menu': menu,
            }
    return render(request, "women/about.html", context= data)

def categoryBook(request):
    books = Book.objects.all()
    data = {
        'title': 'Список книг',
        'books': books,
        'menu': menu,
    }
    return render(request, 'women/categoryBook.html', context=data)

def categoryBookID(request):
    books = Book.objects.all()
    data = {
        'title': 'Список книг ID',
        'books': books,
        'menu': menu,
    }
    return render(request, 'women/BookInfoID.html', context=data)

def bookInfo(request, name):
    book = get_object_or_404(Book, slug=name)
    data = {
        'title': 'Информация о книге',
        'book': book,
        'menu': menu,
    }
    return render(request, 'women/bookInfo.html', context=data)

def bookInfoID(request, id_book):
    book = get_object_or_404(Book, pk=id_book)
    data = {
        'title': 'Информация о книге',
        'book': book,
        'menu': menu,
    }
    return render(request, 'women/bookInfo.html', context=data)

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