from django.urls import path, include
from django.contrib import admin
from tienda.views import accesorios, brumas, autobronceantes


urlpatterns = [
    path('brumas', brumas),
    path('accesorios', accesorios),
    path('autobronceantes', autobronceantes)
]
