from django.core.exceptions import PermissionDenied, BadRequest
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError
from django.shortcuts import render, redirect

menu = [1, 3, 4, 7]

# для хранения представления
# Create your views here.
def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            }
    return render(request, "women/index.html", context=data)

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

def years(request):
    return HttpResponse('<h1>Главные события с 2000 по 2014:</h1>'
                        '<ul>'
                        '<li><a href="http://127.0.0.1:8000/years/2000">2000: Официальное объявление Миллениумской декларации ООН.</a></li>'
                        '<li>2001: Террористические атаки 11 сентября в США</li>'
                        '<li>2002: Введение единой европейской валюты (евро)</li>'
                        '<li>2003: Вторжение США и их союзников в Ирак.</li>'
                        '<li>2004: Летние Олимпийские игры в Афинах.</li>'
                        '<li>2005: Разрушительный ураган Катрина.</li>'
                        '<li>2006: Ливанский кризис.</li>'
                        '<li>2007: Выход первого iPhone от Apple.</li>'
                        '<li>2008: Глобальный финансовый кризис.</li>'
                        '<li>2009: Пандемия свиного гриппа H1N1.</li>'
                        '<li>2010: Землетрясение в Гаити.</li>'
                        '<li>2011: Цунами в Японии и взрывы на АЭС Фукусима.</li>'
                        '<li>2012: Летние Олимпийские игры в Лондоне.</li>'
                        '<li>2013: Челябинский метеорит.</li>'
                        '<li>2014: Присоединение Крыма Россией.</li>'
                        '</ul>')

def year_archive(request, year):
    list_images = {
        2000: "https://proprikol.ru/wp-content/uploads/2020/10/kartinki-oon-1.jpg",
        2001: "https://prod.static9.net.au/fs/1f11d532-69fe-4ff0-ba7e-f90db3f24505",
        2002: "https://proprikol.ru/wp-content/uploads/2020/06/kartinki-evro-8.jpg",
        2003: "https://i.pinimg.com/originals/12/11/00/121100ecf78a05bbfff48c1b3b4b8f6d.jpg",
        2004: "https://cdn.fishki.net/upload/post/2016/08/01/2030075/tn/8052f636b81f5448a89c839ff6a835c7.jpg",
        2005: "https://vneklas-chas.ru/wp-content/uploads/2019/12/uragan-katrina-florida-2.jpg",
        2006: "https://katehon.com/sites/default/files/styles/natural/public/livan2022.jpg?itok=7yOKnzdD",
        2007: "https://eshop.macsales.com/blog/wp-content/uploads/2022/06/Apple-iPhone-1st-gen-scaled.jpeg",
        2008: "https://msk.kprf.ru/wp-content/uploads/2022/02/financialCrisis_V4.jpg",
        2009: "https://static.tbdcdn.com/uploads/2016/02/19/sub/76064-smallv2-298283.jpg",
        2010: "https://images.rapgenius.com/7e121bf03fe6093f9271ae2dce8960da.955x637x1.jpg",
        2011: "https://cdnstatic.rg.ru/uploads/images/photogallery/2021/04/13/b90cc13563c5d51/b90cc13563c5d511618298785.jpeg",
        2012: "https://4.bp.blogspot.com/-MyzOGxewjC0/UBQvqmPwkJI/AAAAAAAABj0/Zw9iGpc-Nss/s1600/61.jpg",
        2013: "https://s11.stc.yc.kpcdn.net/share/i/12/8409395/wr-960.webp",
        2014: "http://ic.pics.livejournal.com/russkiy_malchik/23683470/203132/203132_original.jpg"
    }

#PermissionDenied, BadRequest, Http404,

    if year < 2000:
        raise Http404()
    if year > 2014:
        return redirect('years', permanent=True)
    return HttpResponse(f'<img src={list_images[year]} width="700" height="700">')

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