from django.urls import path, include
from django.contrib import admin
from carrito.views import carrito,   ListaCarritoView,  CarritoDeleteView, buscar_carrito


urlpatterns = [
    path('', ListaCarritoView.as_view(), name='carrito'),
    path('buscar/', buscar_carrito, name='buscar_carrito'),
    path('carrito/<int:pk>/eliminar/', CarritoDeleteView.as_view(), name='eliminar-carrito'),
]
