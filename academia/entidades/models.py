from django.db import models

# Create your models here.
from django.db import models

# Módelo de negocio de la aplicación.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"
    class Meta:
        ordering = ["nombre"] #ordering = ["-nombre"] orden descendente

class Estudiante(models.Model):
    nombre= models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ["nombre", "apellido"]


class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()
    def __str__(self):
        return f"{self.nombre}"
