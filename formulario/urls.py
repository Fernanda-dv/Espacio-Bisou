from django.urls import path
from . import views

#URLS APP: formulario

urlpatterns = [
    path('', views.ver_contacto, name='contacto'),  #Página de Contacto
    path('formulario', views.enviar_mail, name='formulario'), #Manejo del Formulario
]
