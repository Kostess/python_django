from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# для хранения представления
# Create your views here.
def index(request):
    res = request.GET
    print(request.GET)
    return HttpResponse(f'Главная страница основого приложения <br> {dict(res)}')

def categorys(request):
    return HttpResponse('<h1>Ссылки по категориям </h1>')

def category(request, cat_id):
    if cat_id > 1000:
        raise Http404()
    if cat_id < 50:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Номер категории-- </h1> <br> {cat_id}')

def students(request):
    return HttpResponse('<h1>Список студентов:</h1>'
                        '<ul>'
                        '<li>1 - Палий</li>'
                        '<li>2 - Ушаков</li>'
                        '<li>3 - Солодкий</li>'
                        '<li>4 - Гришин</li>'
                         '<li>5 - Короткая</li>'
                        '</ul>')

def student(request, student):
    list_student = {
        1: ['Палий', 'Константин', 'Сергеевич', 'ИВТ-201', '03.08.23'],
        2: ['Ушаков', 'Никита', 'Юрьевич', 'ИВТ-201', '03.08.23'],
        3: ['Солодкий', 'Никита', 'Олегович', 'ИВТ-201', '03.08.23'],
        4: ['Гришин', 'Никита', 'Сергеевич', 'ИВТ-201', '03.08.23'],
        5: ['Короткая', 'София', 'Сергеевна', 'ИВТ-201', '03.08.23'],
    }
    return HttpResponse(f'<h1>Данные студента:</h1>'
                        f'Фамилия: {list_student[student][0]} <br>'
                        f'Имя: {list_student[student][1]} <br>'
                        f'Отчество: {list_student[student][2]} <br>'
                        f'Группа: {list_student[student][3]} <br>'
                        f'Дата Рождения: {list_student[student][4]} <br>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Старница не найдена :(</h1>')