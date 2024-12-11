from django.db import models

class MenuPDF(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_menu = models.CharField(max_length=200, verbose_name="Nombre del Menú", blank=False)
    archivo = models.FileField(upload_to='menus/', verbose_name="Archivo PDF del Menú", blank=False)
    fecha_subida = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Subida")

    class Meta:
        verbose_name = "Menú PDF"
        verbose_name_plural = "Menús PDF"

    def __str__(self):
        return f"{self.nombre_menu} - Subido el {self.fecha_subida.strftime('%d-%B-%Y')}"

    def delete(self, using=None, keep_parents=False):
        if self.archivo:
            self.archivo.delete(save=False)
        super().delete(using=using, keep_parents=keep_parents)