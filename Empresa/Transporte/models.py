from django.db import models
from Personal.models import Personal

class Transporte(models.Model):
    ESTADOS = [
        ('en_servicio', 'En Servicio'),
        ('en_mantenimiento', 'En Mantenimiento'),
        # Agrega otros estados según sea necesario
    ]

    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    fecha_fabricacion = models.CharField(max_length=50)
    estado = models.CharField(max_length=50, choices=ESTADOS)
    costo_mantenimiento = models.DecimalField(max_digits=10, decimal_places=2)

    conductor = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name='transportes_conducidos')

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'Transporte'

