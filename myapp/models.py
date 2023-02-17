from django.db import models

# Create your models here.
class Estacion(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    empty_slots = models.IntegerField()
    free_bikes = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    numero = models.IntegerField()
    tipo = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    tipologia = models.CharField(max_length=200)
    titular = models.CharField(max_length=200)
    inversion = models.CharField(max_length=200)
    fecha_presentacion = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)