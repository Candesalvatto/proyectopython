from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse



def registro(request):
    
    return render(request, 'cuenta/registro.html', {})


def loguin(request):
    
    return render(request, 'cuenta/loguin.html', {})