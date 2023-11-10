from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from carrito.models import Carrito
from carrito.forms import FormularioCarrito, BuscarProductoCarrito, EditarProductoCarrito
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required







# def carrito(request, producto_id): 
    
#         carrito_items = Carrito.objects.filter(usuario=request.user, id=producto_id)
#         return render(request, 'carrito/carrito.html', {'carrito_items': carrito_items})
    
def carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user)
    return render(request, 'carrito.html', {'carrito': carrito})

    
@login_required   
def ver_carrito(request):
   carrito = request.session.get('carrito', {})
   return render(request, 'carrito/carrito.html', {'carrito': carrito})

    # productos_carrito = Carrito.objects.all()
    # formulario_busqueda = BuscarProductoCarrito()
    # if request.method == 'POST':
    #     formulario = FormularioCarrito(request.POST)
    #     if formulario.is_valid():
    #         datos = formulario.cleaned_data
            
    #         producto = datos.get('producto')
    #         cantidad = datos.get('cantidad')
    #         precio = datos.get('precio')
            
    #         producto_carrito = Carrito(producto= producto.lower(), cantidad= cantidad, precio= precio)
    #         producto_carrito.save()
    #         return redirect('carrito')
    #     else:
    #         return render(request, 'carrito/carrito.html',{'form': formulario})                             
    # formulario = FormularioCarrito()
    # return render(request, 'carrito/carrito.html',{'form': formulario, 'productos_carrito': productos_carrito, 'formulario_busqueda': formulario_busqueda})




def buscar_carrito(request):
   listado_de_productos = Carrito.objects.all()
   formulario_busqueda = BuscarProductoCarrito(request.GET)
   formulario = FormularioCarrito()
   
   if formulario_busqueda.is_valid():
       producto_a_buscar = formulario_busqueda.cleaned_data.get('producto')
       if producto_a_buscar:
           listado_de_productos = Carrito.objects.filter(producto__icontains=producto_a_buscar)
   
   return render(request, 'carrito/carrito.html', {'formulario_busqueda': formulario_busqueda, 'productos_carrito': listado_de_productos, 'form': formulario})


def eliminar_carrito(request, producto_id):
    ...
    # producto_a_eliminar = Carrito.objects.get(id=producto_id)
    # producto_a_eliminar.delete()
    # return redirect('carrito')

def editar_carrito(request, producto_id):
    ...
    # producto_a_editar = Carrito.objects.get(id=producto_id)
    # if request.method == 'POST':
    #     formulario = EditarProductoCarrito(request.POST)
    #     if formulario.is_valid():
    #         datos = formulario.cleaned_data
            
    #         producto_a_editar.producto= datos.get('producto')
    #         producto_a_editar.cantidad= datos.get('cantidad')
    #         producto_a_editar.precio= datos.get('precio')
            
    #         producto_a_editar.save()
    #         return redirect ('carrito')
    #     else:
    #         return render(request, 'carrito/editar_carrito.hmtl', {'formulario': formulario,  'producto': producto_a_editar})
    
    # form_editar_carrito = EditarProductoCarrito(initial={'producto': producto_a_editar.producto, 'cantidad': producto_a_editar.cantidad, 'precio': producto_a_editar.precio})
    # return render(request, 'carrito/editar_carrito.html', {'formulario_carrito': form_editar_carrito})




# clases basadas en vistas, mostrar productos del carrito




    
    
     #muestra formulario para crear producto carrito
class ListaCarritoView(ListView):
    model = Carrito
    context_object_name = 'productos_carrito'
    template_name = "carrito/carrito.html"

class CarritoCreateView ( CreateView):        
    model = Carrito
    template_name = "carrito/carrito.html"
    fields = ['producto', 'cantidad', 'precio']
    success_url = reverse_lazy('carrito')
    
    
    #edita el carrito

class CarritoUpdateView(UpdateView):
   model = Carrito
   template_name = "carrito/editar_carrito.html"
   fields = ['producto', 'cantidad', 'precio']
   success_url = reverse_lazy('carrito')

    
    #elimina producto del carrito

class CarritoDeleteView(DeleteView):
   model = Carrito
   template_name = "carrito/carrito.html"
   success_url = reverse_lazy('carrito')

    




