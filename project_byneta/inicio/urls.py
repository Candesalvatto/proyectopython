from django.urls import path, include
from django.contrib import admin
from inicio.views import index, about_me


urlpatterns = [
    path('', index, name='inicio'),
    path('acerca_de_mi',about_me , name='about_me')
]
