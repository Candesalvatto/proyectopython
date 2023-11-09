from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from tienda.models import ProductoAccesorios, ProductoAutobronceante, ProductoBruma
from tienda.forms import FormularioAccesorios





def brumas(request):
    productos = ProductoBruma.objects.all()
    return render(request, 'tienda/brumas.html', {'productos': productos})

def autobronceantes(request):
    productos = ProductoAutobronceante.objects.all()
    return render(request, 'tienda/autobronceantes.html', {'productos': productos})

def accesorios(request):   
   productos = ProductoAccesorios.objects.all()
   form = FormularioAccesorios() 

   return render(request, 'tienda/accesorios.html', {'productos': productos, 'form': form})





def agregar_al_carrito(request):
    producto_id = request.GET.get('producto_id')

    return redirect('carrito')








