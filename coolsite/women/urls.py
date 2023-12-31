"""
URL configuration for coolsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, register_converter
from women.classMarsh import Alphabet
from women.views import *



register_converter(Alphabet, "alphabet")

urlpatterns = [
    path('', index, name='home'),
    path('category/', category,name='category'),
    # path('category/<str:name>', categorys,name='categorys'),
    path('about/', about, name='about'),
    path('category/<str:name>', student, name='student'),
    path('categoryBook', categoryBook, name='categoryBook'),
    path('categoryBookID', categoryBookID, name='categoryBookID'),
    path('categoryBook/<int:id_book>', bookInfoID, name='bookInfoID'),
    path('categoryBook/<slug:name>', bookInfo, name='bookInfo'),
]
