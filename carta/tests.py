from django.test import TestCase
from .models import MenuGeneral  

class MenuGeneralTestCase(TestCase):
    
    # Método de configuración inicial que se ejecuta antes de cada prueba
    def setUp(self):
        # Creación de objeto de prueba
        self.menu_item = MenuGeneral.objects.create(
            nombre="Plato de Prueba",
            descripcion="Descripción del plato de prueba",
            precio=2000,
            categoria='plato_principal'
        )

    # Prueba 1: Verificar que el objeto se creó correctamente
    def test_creacion_menu_item(self):
        item = MenuGeneral.objects.get(nombre="Plato de Prueba")
        self.assertEqual(item.descripcion, "Descripción del plato de prueba")
        self.assertEqual(item.precio, 2000)
        self.assertEqual(item.categoria, 'plato_principal')

    # Prueba 2: Comprobar que se puede actualizar el precio del objeto
    def test_actualizacion_precio(self):
        self.menu_item.precio = 2500  # Cambiar el precio
        self.menu_item.save()         # Guardar el cambio
        item_actualizado = MenuGeneral.objects.get(nombre="Pizza Margherita")
        self.assertEqual(item_actualizado.precio, 2500)

    # Prueba 3: Verificar que la categoría asignada es válida
    def test_categoria_valida(self):
        categorias_validas = ['entrada', 'plato_principal', 'postre', 'bebida']
        self.assertIn(self.menu_item.categoria, categorias_validas)