from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def view(request):
    return HttpResponse('Bienvenido')

def other_view(request):
    fecha = datetime.now()
    return HttpResponse(f'{fecha}')

def saludo(request, nombre, apellido):
    return HttpResponse(f'Hola {nombre} {apellido}')

def template(request):
    
    datos={
        'nombre': 'Candela',
        'apellido': 'Salvatto',
        'numeros': []
    }
    
    #V1 MANERA NO OPTIMA
    # archivo = open(r'C:\Users\User\Desktop\by_neta\templates\mi_template.html', 'r') SOLO ESPECIFICADO PARA NUESTRA COMPUTADORA
    # template = Template(archivo.read())
    # archivo.close()
    
    # contexto = Context(datos)
    # template_renderizado = template.render(contexto)
    
    #V2 CARGADORES 
    template = loader.get_template('mi_template.html') #(de loader cargame el template mi_template.html)
    template_renderizado = template.render(datos)
    
    
    
    
    return HttpResponse(template_renderizado)

def accesorios(request):

    archivo = open(r'C:\Users\User\Desktop\by_neta\templates\accesorios.html', 'r')
    template = Template(archivo.read())
    archivo.close()
    
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

