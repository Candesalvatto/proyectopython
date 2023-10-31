from django.urls import path, include
from django.contrib import admin
from carrito.views import carrito, buscar_carrito


urlpatterns = [
    path('', carrito, name='carrito'),
    path('buscar/', buscar_carrito, name='buscar_carrito'),

]
