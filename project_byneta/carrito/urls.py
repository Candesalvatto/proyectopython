from django.urls import path, include
from django.contrib import admin
from carrito.views import carrito,   ListaCarritoView,  CarritoDeleteView


urlpatterns = [
    path('', ListaCarritoView.as_view(), name='carrito'),
    path('carrito/<int:pk>/eliminar/', CarritoDeleteView.as_view(), name='eliminar-carrito'),
]
