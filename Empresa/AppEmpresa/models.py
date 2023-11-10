from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator

# Create your models here.

class producto(models.Model):
    nombre = models.CharField(max_length=50, validators=[MinLengthValidator(2), MaxLengthValidator(50)])
    litro = models.CharField(max_length=50, validators=[MinLengthValidator(1), MaxLengthValidator(50)])
    tamanio = models.CharField(max_length=50, validators=[MinLengthValidator(1), MaxLengthValidator(50)])
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    proveedor = models.CharField(max_length=50, validators=[MinLengthValidator(2), MaxLengthValidator(50)])
    tipoagua = models.CharField(max_length=50, validators=[MinLengthValidator(2), MaxLengthValidator(50)])