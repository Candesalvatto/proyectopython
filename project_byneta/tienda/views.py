from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from tienda.models import Producto



def accesorios(request):    
    return render(request, 'tienda/accesorios.html', {})

def brumas(request):
    
    return render(request, 'tienda/brumas.html', {})

def autobronceantes(request):
    
    return render(request, 'tienda/autobronceantes.html', {})



