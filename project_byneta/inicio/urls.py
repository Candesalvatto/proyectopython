from django.urls import path, include
from django.contrib import admin
# from . import views
from inicio.views import index


urlpatterns = [
    path('', index)
]
