from django.shortcuts import render
from .models import Producto, LocalAsociado

# Estas en las vistas de la APP: chris_de_paris

def ver_chris_de_paris(request):
    productos = Producto.objects.all()  
    locales = LocalAsociado.objects.all()
    return render(request, 'chris_de_paris.html', {'productos': productos, 'locales': locales})
