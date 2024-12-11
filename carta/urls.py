from django.urls import path
from . import views

#URLS APP: carta

urlpatterns = [
    path('', views.ver_carta, name='carta'),  
]