from django import forms
from Personal.models import Personal
from Transporte.models import Transporte 

class PersonalRegistrationForm(forms.Form):
    CARGOS = [
        ('conductor', 'Conductor'),
        ('asistente', 'Asistente'),
        # Agrega otros cargos según sea necesario
    ]

    nombre = forms.CharField(max_length=50)
    cargo = forms.ChoiceField(choices=CARGOS)
    edad = forms.IntegerField()
    experiencia = forms.IntegerField()
    telefono = forms.CharField(max_length=15)
    email = forms.EmailField()
    

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'
