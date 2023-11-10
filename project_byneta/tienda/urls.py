from django.urls import path, include
from django.contrib import admin
from tienda.views import accesorios, brumas, autobronceantes, agregar_al_carrito



urlpatterns = [
    path('brumas', brumas, name='brumas'),
    path('accesorios', accesorios, name='accesorios'),
    path('autobronceantes', autobronceantes, name='autobronceantes'),
     path('agregar_carrito/<int:producto_id>', agregar_al_carrito, name='agregar_al_carrito'),
]
