from django.urls import path, include
from django.contrib import admin
from manual.views import manual


urlpatterns = [
    path('', manual, name='manual')
]
