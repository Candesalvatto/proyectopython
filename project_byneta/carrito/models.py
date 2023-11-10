from django.db import models
from tienda.models import Producto

class Carrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)
    precio = models.IntegerField()
    cantidad= models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.producto} - {self.precio} - {self.cantidad}'