from django.urls import path
from . import views

#URLS APP: main

urlpatterns = [
    #path('plantilla_base/', views.ver_plantilla_base, name='plantilla_base'), #Prueba
    path('', views.ver_inicio, name='inicio'),  
    #path('emporio_bisou/', views.ver_emporio_bisou, name='EmporioBisou') #Proximamente
]