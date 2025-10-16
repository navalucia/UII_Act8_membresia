from django.db import models

class Membresia(models.Model):
    id_membresia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    costo_mensual = models.DecimalField(max_digits=8, decimal_places=2)
    acceso_limitado = models.BooleanField(default=False)
    acceso_entrenador = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - ${self.costo_mensual}"
