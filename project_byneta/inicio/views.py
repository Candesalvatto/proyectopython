from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse



def index(request):

    
    return render(request, 'inicio/index.html', {})

def about_me(request):

    
    return render(request, 'inicio/about_me.html', {})