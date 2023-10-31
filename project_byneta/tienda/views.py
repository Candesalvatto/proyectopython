from django.shortcuts import render, redirect
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



def agregar_accesorio(request):
    if request.method == 'POST':
        form = FormularioAccesorios(request.POST)
        if form.is_valid():
            print("IS VALID")
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            precio = form.cleaned_data['precio']
            producto = ProductoAccesorios(
                nombre=nombre, descripcion=descripcion, precio=precio)
            producto.save()
            return redirect('accesorios')
    else:
        form = FormularioAccesorios()

    return render(request, 'tienda/accesorios.html', {'form': form})



