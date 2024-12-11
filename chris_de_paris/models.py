from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image

def validate_image(image):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.webp']
    if not any(image.name.endswith(ext) for ext in valid_extensions):
        raise ValidationError("La imagen debe ser en formato .jpg, .jpeg, .png o .webp.")
    
    if image.size > 5 * 1024 * 1024:
        raise ValidationError("El tamaño de la imagen no puede superar los 5MB.")

    try:
        img = Image.open(image)
        img.verify()  
    except (IOError, SyntaxError) as e:
        raise ValidationError("El archivo no es una imagen válida.")

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre", blank=False)
    descripcion = models.TextField(blank=False, verbose_name="Descripción")
    imagen = models.ImageField(upload_to='ChrisdeParis/', verbose_name="Imagen del producto", blank=False, validators=[validate_image])
    precio = models.IntegerField(verbose_name="Precio", blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    def delete(self, using=None, keep_parents=False):
        if self.imagen:
            self.imagen.delete(save=False)
        super().delete(using=using, keep_parents=keep_parents)

    class Meta:
        verbose_name = "Producto"  
        verbose_name_plural = "Productos"  

class LocalAsociado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre", blank=False)
    dirección = models.CharField(max_length=200, verbose_name="Dirección", blank=False)
    imagen = models.ImageField(upload_to='locales_asociados/', verbose_name="Logo", blank=True, validators=[validate_image])
    
    def __str__(self):
        return self.nombre
    
    def delete(self, using=None, keep_parents=False):
        if self.imagen:
            self.imagen.delete(save=False)
        super().delete(using=using, keep_parents=keep_parents)

    class Meta:
        verbose_name = "Local Asociado"
        verbose_name_plural = "Locales Asociados"