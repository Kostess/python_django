from django.db import models
import datetime
# хранение ORM-моделей для представления данных из БД

dt_now = datetime.datetime.now()

class Student(models.Model):
    fio = models.CharField(max_length=30)
    interesting = models.TextField(blank=True)
    birdDay = models.DateTimeField(default=dt_now)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_money = models.BooleanField(default=True)

    def __str__(self):
        return self.fio

"""
    создание записей Student.objects.create(fio="Асадов Наил", interesting="конный спорт, литература, музыка")
    выбор всех записей Student.objects.all()
    выбор записей по критерию Student.objects.filter()
    выбор одной записи Student.objects.get() 
 

wq = Book.objects.filter(yearPublication__lt=2023)

for i in wq:
    print(i)
 
 
 
ws = Book.objects.order_by('price')  
 
for i in ws:
     print(i)


"""

class Book(models.Model):
    nameBook = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    yearPublication = models.IntegerField(default=0)
    publishingHouse = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)


