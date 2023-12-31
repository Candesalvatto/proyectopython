from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse
from tienda.models import Producto
from tienda.forms import FormularioAccesorios, FormularioAutobronceantes, FormularioBrumas, FormularioProducto
from carrito.models import Carrito






def brumas(request):
    productos = Producto.objects.filter(tipo='bruma')
    form = FormularioBrumas() 
    return render(request, 'tienda/brumas.html', {'productos': productos, 'form': form})

def autobronceantes(request):
    productos = Producto.objects.filter(tipo='autobronceante')
    form = FormularioAutobronceantes() 
    return render(request, 'tienda/autobronceantes.html', {'productos': productos, 'form': form})

def accesorios(request):   
    productos = Producto.objects.filter(tipo='accesorio')
    form = FormularioAccesorios() 

    return render(request, 'tienda/accesorios.html', {'productos': productos, 'form': form})

def editar_producto(request, producto_id):   
    producto = Producto.objects.get(id=producto_id)

    return render(request, 'tienda/editar_producto.html', {'producto': producto})

def eliminar_producto(request, producto_id):   
    producto = Producto.objects.get(id=producto_id)
    mensaje = messages
    if request.method == 'POST':
        producto.delete()
        print('----el producto ha sido eliminado------')
        if producto.tipo == 'bruma':
            url_productos = 'brumas'
        elif producto.tipo == 'accesorio':
            url_productos = 'accesorios'
        else:
            producto.tipo = 'autobronceante'
            url_productos = 'autobronceantes'
        return redirect(url_productos)
    else:
        print('-----vuelva a intentarlo-----')

    return render(request, 'tienda/eliminar_producto.html', {'producto': producto})



def detalle_producto(request, producto_id):   
    producto = Producto.objects.get(id=producto_id)
    if producto.tipo == 'bruma':
        url_productos = 'brumas'
    elif producto.tipo == 'accesorio':
        url_productos = 'accesorios'
    else:
        producto.tipo = 'autobronceante'
        url_productos = 'autobronceantes'


    return render(request, 'tienda/detalle_producto.html', {'producto':producto, 'url_productos': url_productos})

@login_required
def agregar_al_carrito(request, producto_id):
    if not request.user.is_authenticated:
        return redirect('loguin')
    
    producto = get_object_or_404(Producto, id=producto_id)
    print(producto)
    carrito, creado = Carrito.objects.get_or_create(
        usuario=request.user, producto= producto, nombre_producto=producto.nombre, precio=producto.precio, cantidad=1, imagen= producto.imagen)

    if not creado:
        carrito.cantidad += 1


    carrito.save()
    return redirect('carrito')

def agregar_producto(request):
    if request.method == 'POST':
        form = FormularioProducto(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)  
            producto.save()

            if producto.tipo == 'bruma':
                url_productos = 'brumas'
            elif producto.tipo == 'accesorio':
                url_productos = 'accesorios'
            else:
                producto.tipo = 'autobronceante'
                url_productos = 'autobronceantes'

            return redirect(url_productos)  
        form = FormularioProducto()

    return render(request, 'tienda/agregar_producto.html', {'form': form})


    
class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = "tienda/editar_producto.html"
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'cantidad', 'tipo']

    
    def form_valid(self, form):
        producto = form.save()
        span = messages
        print('------producto editado----------')
        span.success(self.request, '¡EL PRODUCTO HA SIDO EDITADO SATISFACTORIAMENTE!', extra_tags='editado')
        return redirect('eliminar_producto', producto_id=producto.id)
    





















