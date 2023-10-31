from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from tienda.models import Producto




def accesorios(request):    
    productos = Producto.objects.all()

    return render(request, 'tienda/accesorios.html',{'productos': productos})

def brumas(request):
    
    return render(request, 'tienda/brumas.html', {})

def autobronceantes(request):
    
    return render(request, 'tienda/autobronceantes.html', {})




