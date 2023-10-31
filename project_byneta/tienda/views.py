from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from tienda.models import ProductoAccesorios, ProductoAutobronceante, ProductoBruma




def accesorios(request):    
    productos = ProductoAccesorios.objects.all()

    return render(request, 'tienda/accesorios.html',{'productos': productos})

def brumas(request):
    productos = ProductoBruma.objects.all()
    return render(request, 'tienda/brumas.html', {'productos': productos})

def autobronceantes(request):
    productos = ProductoAutobronceante.objects.all()
    return render(request, 'tienda/autobronceantes.html', {'productos': productos})




