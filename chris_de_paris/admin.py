from django.contrib import admin
from django.contrib import messages
from .models import Producto, LocalAsociado

@admin.action(description='Eliminar productos seleccionados (RECOMENDADO)')
def eliminar_productos(modeladmin, request, queryset):
    for producto in queryset:
        nombre_producto = producto.nombre 
        if producto.imagen:
            producto.imagen.delete(save=False)
        producto.delete()
        messages.success(request, f"'{nombre_producto}' ha sido eliminado.")

@admin.action(description='Eliminar locales seleccionados (RECOMENDADO)')
def eliminar_locales(modeladmin, request, queryset):
    for local in queryset:
        nombre_local = local.nombre 
        if local.imagen: 
            local.imagen.delete(save=False)
        local.delete()
        messages.success(request, f"'{nombre_local}' ha sido eliminado.")

class ProductoAdmin(admin.ModelAdmin):
    actions = [eliminar_productos]
    list_display = ('nombre', 'descripcion', 'imagen', 'precio')
    search_fields = ('nombre',)

class LocalAsociadoAdmin(admin.ModelAdmin):
    actions = [eliminar_locales] 
    list_display = ('id', 'nombre', 'dirección')  
    search_fields = ('nombre', 'dirección') 
    list_filter = ('nombre',)  
    ordering = ('nombre',)

admin.site.register(Producto, ProductoAdmin)  
admin.site.register(LocalAsociado, LocalAsociadoAdmin)