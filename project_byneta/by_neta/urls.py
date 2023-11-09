from django.contrib import admin
from django.urls import path, include
from by_neta.views import view, other_view, saludo, template, accesorios
from inicio.views import index
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('inicio.urls')),
    path('manual', include('manual.urls')),
    path('tienda/', include('tienda.urls')),
    path('cuenta/', include('cuenta.urls')),
    path('carrito', include('carrito.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
