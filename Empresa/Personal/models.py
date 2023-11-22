from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator

class Personal(models.Model):
    CARGOS = [
        ('conductor', 'Conductor'),
        ('asistente', 'Asistente'),
        # Agrega otros cargos según sea necesario
    ]

    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50, choices=CARGOS)
    edad = models.IntegerField()
    experiencia = models.IntegerField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        app_label = 'Personal'


