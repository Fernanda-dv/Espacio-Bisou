from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# URLS Proyecto General

urlpatterns = [
    path('gestion_bisou/', admin.site.urls), #Por seguridad se cambia esta ruta
    path('', include('main.urls')), 
    path('chris_de_paris/', include('chris_de_paris.urls')),
    path('contacto/', include('formulario.urls')), 
    path('carta/', include('carta.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)