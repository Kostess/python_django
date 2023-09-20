from django.http import HttpResponse
from django.shortcuts import render
# для хранения представления
# Create your views here.
def index(request):
    return HttpResponse('Главная страница основого приложения')

def categorys(request):
    return HttpResponse('<h1>Ссылки по категориям </h1>')

def category(request, cat_id):
    return HttpResponse(f'<h1>Номер категории-- </h1> <br> {cat_id}')