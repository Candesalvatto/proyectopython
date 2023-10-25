from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# from inicio.models import Auto

# def crear_auto(request, marca, modelo, anio):
    
#     auto= Auto(marca = marca, modelo= modelo, anio= anio)
#     auto.save()
    
#     template = loader.get_template('mi_template.html')
#     template_renderizado = template.render({'auto': auto})
#     return HttpResponse(template_renderizado)


def index(request):
    datos={}
    
    template_index = loader.get_template('index.html')
    template_renderizado_index = template_index.render(datos)
    return HttpResponse(template_renderizado_index)