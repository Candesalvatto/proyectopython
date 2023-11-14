from django.urls import path, include
from django.contrib import admin
from tienda.views import accesorios, brumas, autobronceantes, agregar_al_carrito, detalle_producto, ProductoUpdateView,   agregar_producto, eliminar_producto



urlpatterns = [
    path('brumas', brumas, name='brumas'),
    path('accesorios', accesorios, name='accesorios'),
    path('autobronceantes', autobronceantes, name='autobronceantes'),
    path('agregar_carrito/<int:producto_id>', agregar_al_carrito, name='agregar_al_carrito'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('detalle/<int:producto_id>', detalle_producto, name= 'detalle_producto'),
    path('tienda/<int:pk>/editar/', ProductoUpdateView.as_view(), name='editar_producto'),
    # path('tienda/<int:pk>/eliminar_producto/', ProductoDeleteView.as_view(), name='eliminar_producto'),
    path('tienda/eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
]
