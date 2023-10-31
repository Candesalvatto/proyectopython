from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from cuenta.forms import FormularioRegistrar, FormularioLoguin
from cuenta.models import Cliente



def registro(request):
    
    if request.method == 'POST':
        formulario_registro = FormularioRegistrar(request.POST)
        if formulario_registro.is_valid():
            datos = formulario_registro.cleaned_data
            
            nombre= datos.get('nombre')
            apellido= datos.get('apellido')
            email= datos.get('email')
            contrasena= datos.get('contrasena')
    
    
            cliente_registrado= Cliente(nombre=nombre, apellido=apellido, email=email, contrasena=contrasena)
            cliente_registrado.save()
            return redirect('loguin')
        
        else:
            return render(request, 'cuenta/registro.html', {'form': formulario_registro})
        
    formulario_registro = FormularioRegistrar()
    return render(request, 'cuenta/registro.html', {'form': formulario_registro})


def loguin(request):
    
    
    # nombre_a_buscar = request.GET.get('nombre')
    
    # if nombre_a_buscar:
    #     lista_clientes = Cliente.objects.filter(nombre__icontains= nombre_a_buscar)
    # else:
    #     lista_clientes = Cliente.objects.all()
        
    # return render(request, 'cuenta/loguin.html', {'lista_clientes': lista_clientes} )
    

    
    
    return render(request, 'cuenta/loguin.html', {'form': FormularioLoguin() })