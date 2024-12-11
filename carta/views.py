from django.shortcuts import render
from .models import MenuPDF

# Estas en las vistas de la APP: carta

def ver_carta(request):
    menu = MenuPDF.objects.last()  # Obtiene el PDF más reciente
    return render(request, 'carta.html', {'menu': menu})