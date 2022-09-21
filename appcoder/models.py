from django.db import models

# Create your models here.
class curso(models.Model):
    nonbre = models.CharField(max_length=40)
    camada = models.IntegerField()


class estudiante(models.Model):
    nonbre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class profesor(models.Model):
    nonbre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()   
    profesion= models.CharField(max_length=30)

class entregable(models.Model):
    nonbre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregable = models.BooleanField()