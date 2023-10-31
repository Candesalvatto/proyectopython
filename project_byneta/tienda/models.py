from django.db import models

class Producto(models.Model):
    # nombre = models.CharField()
    # descripcion = models.TextField()
    # precio = models.DecimalField()
    ...
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)



