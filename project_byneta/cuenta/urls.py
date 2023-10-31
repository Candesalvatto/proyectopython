from django.urls import path, include
from django.contrib import admin
from cuenta.views import registro, loguin


urlpatterns = [
    path('registrar', registro, name='registro'),
    path('ingresar', loguin, name='loguin')
]
