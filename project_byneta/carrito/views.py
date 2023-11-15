from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from carrito.models import Carrito
from carrito.forms import FormularioCarrito
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required   
def carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user)
    
    return render(request, 'carrito/carrito.html', {'carrito': carrito, 'fecha': date.today()})




class ListaCarritoView(LoginRequiredMixin, ListView):
    model = Carrito
    context_object_name = 'productos_carrito'
    template_name = "carrito/carrito.html"
    
    def get_queryset(self):
        producto_a_buscar = self.request.GET.get('producto')
        if producto_a_buscar:
            listado_de_productos = self.model.objects.filter(producto__nombre__icontains=producto_a_buscar, usuario=self.request.user)
            print('PRIMER PRINT--------------')
        else:
            listado_de_productos = self.model.objects.filter(usuario=self.request.user)
            print('-----------------SEGUNDA PRINT')
        return listado_de_productos

   
    #elimina producto del carrito

class CarritoDeleteView(LoginRequiredMixin, DeleteView):
    model = Carrito
    template_name = "carrito/carrito.html"
    success_url = reverse_lazy('carrito')

    




