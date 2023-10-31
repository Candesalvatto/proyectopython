from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=30)  #de models traeme charField, que va a ser caracteres
    contrasena= models.IntegerField(max_length=30)


    def __str__(self):
        return f'{self.id} - {self.usuario} - {self.contrasena}'
    
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)  
    apellido= models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    contrasena= models.IntegerField(max_length=20)
    
    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.apellido} - {self.email} - {self.contrasena}'

    

    
