from django.shortcuts import render
from .models import Nav, Servicio, QuieneSomos

# Create your views here.
def Home(request):
    navbar = Nav.objects.all()  
    context = {'navbar':navbar}
    return render(request, 'ring/Home.html', context)

def Servicios(request):
    navbar = Nav.objects.all()
    servicios =  Servicio.objects.all()
    context = {'navbar':navbar, 'servicio':servicios}
    return render(request, 'ring/Servicios.html', context)

def QuienesSomos(request):
    navbar = Nav.objects.all()
    nosotros =  QuieneSomos.objects.all()
    context = {'navbar':navbar, 'nosotros':nosotros}
    return render(request, 'ring/QuienesSomos.html', context)