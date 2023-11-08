from django.db import models
# хранение ORM-моделей для представления данных из БД

class Student(models.Model):
    fio = models.CharField(max_length=30)
    interesting = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_money = models.BooleanField(default=True)

# Create your models here.


