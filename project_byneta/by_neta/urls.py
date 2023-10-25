from django.contrib import admin
from django.urls import path, include
from by_neta.views import view, other_view, saludo, template, accesorios
from inicio.views import index


urlpatterns = [
    path('', include('inicio.urls')),
    path('manual', include('manual.urls')),
    path('tienda/', include('tienda.urls')),
    path('cuenta/', include('cuenta.urls')),
    # path('fecha', other_view),
    # path('saludo/<nombre>/<apellido>', saludo),
    # path('template', template),
    # path('accesorios', accesorios),
    # path('crear_auto/<str:marca>', crear_auto),
    path('admin/', admin.site.urls),
]
