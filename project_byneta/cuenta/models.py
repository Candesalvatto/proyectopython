from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    usuario = models.CharField(max_length=30)  #de models traeme charField, que va a ser caracteres
    contrasena= models.CharField(max_length=30)


    def __str__(self):
        return f'{self.id} - {self.usuario} - {self.contrasena}'
    
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)  
    apellido= models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    contrasena= models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.apellido} - {self.email} - {self.contrasena}'

    
class DatosExtra(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   direccion = models.CharField(max_length=50)
   ciudad = models.CharField(max_length=50)
   pais = models.CharField(max_length=50)
   telefono = models.IntegerField( null=True, blank=True)
   avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    
