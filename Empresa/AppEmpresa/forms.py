from django import forms
from AppEmpresa.models import producto

class productoRegistrationForm(forms.Form):
    TIPOS = [('purificada', 'PURIFICADA'), ('dulce', 'DULCE'), ('destilada','DESTILADA')]
    EMPRESAS = [('aguas andinas ','AGUAS ANDINAS'), ('naturandes','NATURANDES')]


    nombre = forms.CharField(max_length=50)
    litro = forms.CharField(max_length=50)
    tamanio = forms.CharField(max_length=50)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    proveedor = forms.CharField(widget=forms.Select(choices=EMPRESAS))
    tipoagua = forms.CharField(widget=forms.Select(choices=TIPOS))


class Formproducto(forms.ModelForm):
    class Meta:
        model = producto
        fields = '__all__'