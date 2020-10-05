from django.db import models

class Desarrollo(models.Model):
    nombre_desarrollo = models.CharField(max_length=100)
    ubicacion_desarrollo = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_desarrollo

class Leads(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30, blank=False, unique=True)
    email = models.EmailField(max_length=250)
    desarrollo = models.ForeignKey(
        Desarrollo,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)