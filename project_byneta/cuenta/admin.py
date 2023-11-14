from django.contrib import admin
from cuenta.models import Usuario, Cliente, DatosExtra

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(DatosExtra)

