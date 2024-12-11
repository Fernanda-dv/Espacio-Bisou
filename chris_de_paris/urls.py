from django.urls import path
from . import views

# URLS chris_de_paris
urlpatterns = [
    path('', views.ver_chris_de_paris, name='ChrisdeParis'), 
]

