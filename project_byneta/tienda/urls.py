from django.urls import path, include
from django.contrib import admin
from tienda.views import accesorios, brumas, autobronceantes



urlpatterns = [
    path('brumas', brumas, name='brumas'),
    path('accesorios', accesorios, name='accesorios'),
    path('autobronceantes', autobronceantes, name='autobronceantes'),
    # path('agregar-accesorio/', agregar_accesorio, name='agregar_accesorio'),
]
