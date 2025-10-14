from django.shortcuts import render
from django.views.generic import (TemplateView)
from django.http import HttpResponse
from .models import Galeria

#Función para la pagina principal
def index(request):
#    return HttpResponse("<b> <h1> Hola Mundo. <small> Curso básico Django</small></h1> </b>")
    return render(request,'home/index.html')

def aboutus(request):
    return render(request,'home/aboutus.html')

def contact(request):
    return render(request, 'home/contact.html')

def ver_galeria(request):
    imagenes = Galeria.objects.all()
    return render(request, 'home/carousel.html', {'imagenes': imagenes})