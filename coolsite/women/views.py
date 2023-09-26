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

def students(request):
    return HttpResponse('<h1>Список студентов:</h1>'
                        '<ul>'
                        '<li>paliy</li>'
                        '<li>ushakov</li>'
                        '<li>solodkiy</li>'
                        '<li>grishin</li>'
                         '<li>korotkaya</li>'
                        '</ul>')

def student(request, student):
    list_student = {
        'paliy': ['Палий', 'Константин', 'Сергеевич', 'ИВТ-201', '03.08.23'],
        'ushakov': ['Ушаков', 'Никита', 'Юрьевич', 'ИВТ-201', '03.08.23'],
        'solodkiy': ['Солодкий', 'Никита', 'Олегович', 'ИВТ-201', '03.08.23'],
        'grishin': ['Гришин', 'Никита', 'Сергеевич', 'ИВТ-201', '03.08.23'],
        'korotkaya': ['Короткая', 'София', 'Сергеевич', 'ИВТ-201', '03.08.23'],
    }
    return HttpResponse(f'<h1>Данные студента:</h1>'
                        f'Фамилия: {list_student[student][0]} <br>'
                        f'Имя: {list_student[student][1]} <br>'
                        f'Отчество: {list_student[student][2]} <br>'
                        f'Группа: {list_student[student][3]} <br>'
                        f'Дата Рождения: {list_student[student][4]} <br>')