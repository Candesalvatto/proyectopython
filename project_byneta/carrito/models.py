from django.db import models

class Carrito(models.Model):
    producto = models.CharField(max_length=30)  #de models traeme charField, que va a ser caracteres
    precio = models.IntegerField()
    cantidad= models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.producto} - {self.precio} - {self.cantidad}'