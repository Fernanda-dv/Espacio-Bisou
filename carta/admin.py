from django.contrib import admin
from .models import MenuPDF

@admin.register(MenuPDF)
class MenuPDFAdmin(admin.ModelAdmin):
    list_display = ('nombre_menu', 'archivo', 'fecha_subida')
    ordering = ('-fecha_subida',)