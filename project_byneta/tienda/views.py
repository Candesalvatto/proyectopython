from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from tienda.models import Producto
from tienda.forms import FormularioAccesorios
from carrito.models import Carrito



def brumas(request):
    productos = Producto.objects.filter(tipo='bruma')
    return render(request, 'tienda/brumas.html', {'productos': productos})

def autobronceantes(request):
    productos = Producto.objects.filter(tipo='autobronceante')
    return render(request, 'tienda/autobronceantes.html', {'productos': productos})

def accesorios(request):   
    productos = Producto.objects.filter(tipo='accesorio')
    form = FormularioAccesorios() 

    return render(request, 'tienda/accesorios.html', {'productos': productos, 'form': form})





def agregar_al_carrito(request, producto_id):
        producto = Producto.objects.get(request, id=producto_id)
        Carrito, creado = Carrito.objects.get_or_create( producto=producto)

        if not creado:
            Carrito.cantidad += 1


        Carrito.save()
        return redirect('carrito')


















