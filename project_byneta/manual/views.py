from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse



def manual(request):
    
    
    return render(request, 'manual/manual.html', {})
