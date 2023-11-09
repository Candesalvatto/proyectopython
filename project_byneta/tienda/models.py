from django.db import models

        
class ProductoAccesorios(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True)
    
    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.descripcion} - {self.precio}'
    
class ProductoAutobronceante(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', default='default.jpg')
    
    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.descripcion} - {self.precio}'
    
class ProductoBruma(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', default='default.jpg')
    
    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.descripcion} - {self.precio}'
    


    
    

    





