from django.contrib import admin
from django.urls import path, include
from by_neta.views import view, other_view, saludo, template, accesorios
from inicio.views import index


urlpatterns = [
    path('', include('inicio.urls')),
    path('manual', include('manual.urls')),
    path('tienda/', include('tienda.urls')),
    path('cuenta/', include('cuenta.urls')),
    path('carrito', include('carrito.urls')),
    path('admin/', admin.site.urls),
]
