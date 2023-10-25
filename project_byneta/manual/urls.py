from django.urls import path, include
from django.contrib import admin
# from . import views
from manual.views import manual


urlpatterns = [
    path('', manual)
]
