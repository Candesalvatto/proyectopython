from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from carrito.models import Carrito
from carrito.forms import FormularioCarrito, BuscarProductoCarrito



def carrito(request): #agregar productos al carrito por un formulario
   productos_carrito = Carrito.objects.all()
   if request.method == 'POST':
       formulario = FormularioCarrito(request.POST)
       if formulario.is_valid():
           datos = formulario.cleaned_data
           
           producto = datos.get('producto')
           cantidad = datos.get('cantidad')
           precio = datos.get('precio')
           
           producto_carrito = Carrito(producto= producto.lower(), cantidad= cantidad, precio= precio)
           producto_carrito.save()
           return redirect('carrito')
       else:
           return render(request, 'carrito/carrito.html',{'form': formulario})                             
   formulario = FormularioCarrito()
   return render(request, 'carrito/carrito.html',{'form': formulario, 'productos_carrito': productos_carrito})




def buscar_carrito(request):
    listado_de_productos = Carrito.objects.all()
    formulario_busqueda = BuscarProductoCarrito(request.GET)
    
    if formulario_busqueda.is_valid():
        producto_a_buscar = formulario_busqueda.cleaned_data.get('producto')
        listado_de_productos = Carrito.objects.filter(producto__icontains=producto_a_buscar)
    
    return render(request, 'carrito/carrito.html', {'formulario_busqueda': formulario_busqueda, 'productos_carrito': listado_de_productos})




