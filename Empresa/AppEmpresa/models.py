from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from Transporte.models import Transporte

# Create your models here.

class producto(models.Model):
    TIPOS_AGUA = [
        ('purificada', 'PURIFICADA'),
        ('dulce', 'DULCE'),
        ('destilada', 'DESTILADA'),
    ]

    EMPRESAS_PROVEEDOR = [
        ('aguas andinas', 'AGUAS ANDINAS'),
        ('naturandes', 'NATURANDES'),
    ]

    nombre = models.CharField(max_length=50, validators=[MinLengthValidator(2), MaxLengthValidator(50)])
    litro = models.FloatField(validators=[MinValueValidator(0)])
    tamanio = models.CharField(max_length=50, validators=[MinLengthValidator(1), MaxLengthValidator(50)])
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    proveedor = models.CharField(max_length=50, choices=EMPRESAS_PROVEEDOR)
    tipoagua = models.CharField(max_length=50, choices=TIPOS_AGUA)

    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre
