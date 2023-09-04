from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()



class Cursos(models.Model):
    nombre = models.CharField(max_length=50)
    profesor = models.CharField(max_length=50)




class Mayorista(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    nroMayorista = models.CharField(max_length=50)

