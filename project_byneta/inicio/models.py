from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=30)  #de models traeme charField, que va a ser caracteres
    modelo = models.CharField(max_length=30)
    anio = models.IntegerField() #numeros

    def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo}'
