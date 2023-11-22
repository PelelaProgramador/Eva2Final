from django import forms
from Personal.models import Personal 
from Transporte.models import Transporte

class TransporteRegistrationForm(forms.Form):
    ESTADOS = [
        ('en_servicio', 'En Servicio'),
        ('en_mantenimiento', 'En Mantenimiento'),
        # Agrega otros estados según sea necesario
    ]

    nombre = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=50)
    capacidad = forms.IntegerField()
    fecha_fabricacion = forms.CharField(max_length=50)
    estado = forms.ChoiceField(choices=ESTADOS)
    costo_mantenimiento = forms.DecimalField(max_digits=10, decimal_places=2)
    

class TransporteForm(forms.ModelForm):
    class Meta:
        model = Transporte
        fields = '__all__'
