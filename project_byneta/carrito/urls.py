from django.urls import path, include
from django.contrib import admin
from carrito.views import carrito, buscar_carrito, eliminar_carrito, editar_carrito, ListaCarritoView, CarritoCreateView, CarritoUpdateView, CarritoDeleteView, ver_carrito


urlpatterns = [
    path('', ListaCarritoView.as_view(), name='carrito'),
    path('crear-carrito/', CarritoCreateView.as_view(), name='crear-carrito'),
    path('buscar/', buscar_carrito, name='buscar_carrito'),
    # path('<int:producto_id>/eliminar/', eliminar_carrito, name='eliminar_carrito'),
    # path('<int:producto_id>/editar/', editar_carrito, name='editar_carrito')
    path('carrito/<int:pk>/editar/', CarritoUpdateView.as_view(), name='editar-carrito'),
    path('carrito/<int:pk>/eliminar/', CarritoDeleteView.as_view(), name='eliminar-carrito'),
]
