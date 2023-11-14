from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from carrito.models import Carrito
from carrito.forms import FormularioCarrito, BuscarProductoCarrito
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from datetime import date


@login_required   
def carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user)
    formulario_busqueda = BuscarProductoCarrito()

    
    return render(request, 'carrito.html', {'carrito': carrito, 'fecha': date.today(), 'formulario_busqueda': formulario_busqueda})


def buscar_carrito(request):
    formulario_busqueda = BuscarProductoCarrito(request.GET)
    listado_de_productos = []

   
    if formulario_busqueda.is_valid():
        producto_a_buscar = formulario_busqueda.cleaned_data.get('producto')
        print('PRIMER PRINT--------------')
        if producto_a_buscar:
            listado_de_productos = Carrito.objects.filter(producto__nombre__icontains=producto_a_buscar)
            print('-----------------SEGUNDA PRINT')
   
    return render(request, 'carrito/carrito.html', {'formulario_busqueda': formulario_busqueda, 'productos_carrito': listado_de_productos})



     #muestra formulario para crear producto carrito
class ListaCarritoView(ListView):
    model = Carrito
    context_object_name = 'productos_carrito'
    template_name = "carrito/carrito.html"

   
    #elimina producto del carrito

class CarritoDeleteView(DeleteView):
    model = Carrito
    template_name = "carrito/carrito.html"
    success_url = reverse_lazy('carrito')

    




