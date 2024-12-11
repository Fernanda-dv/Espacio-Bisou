from django.shortcuts import render

# Estas en las vistas de la APP: main

#def ver_plantilla_base(request):  #No será necesaria
#    return render(request,'plantilla_base.html')

def ver_inicio(request): 
    return render(request,'inicio.html')

#def ver_emporio_bisou(request): 
#    return render(request,'emporio_bisou.html')


