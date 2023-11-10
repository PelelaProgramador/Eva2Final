from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppEmpresa.models import producto
from AppEmpresa.forms import Formproducto
import datetime
from . import forms


# Create your views here.

def display(request):
    return HttpResponse("<h1>Hola Mundo!</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y Hora Actual: </b>" + str (dt)
    return HttpResponse(s)

def renderTemplate(request):
    # Lógica para renderizar tu plantilla y devolver una respuesta
    data = {"nombre": "Dwaynne Johnsson", "id": 1, "email": "LaRoca@hotmail.com"}
    return render(request, 'template.html', data)

def productoData(request):
    productos = producto.objects.all()
    data = {'productos' : productos}
    return render(request, 'productos.html', data)

def productoRegistrationView(request):
    form = forms.productoRegistrationForm()
    
    if request.method == 'POST':
        form = forms.productoRegistrationForm(request.POST)
        if form.is_valid():
            print("Form es Valido")
            print("Nombre: ", form.cleaned_data['nombre'])
            print("Litro: ", form.cleaned_data['litro'])
            print("Tamaño: ", form.cleaned_data['tamanio'])
            print("Precio: ", form.cleaned_data['precio'])
            print("Proveedor: ", form.cleaned_data['proveedor'])
            print("Tipo de agua: ", form.cleaned_data['tipoagua'])
            
    data = {'form' : form}
    return render(request,'productoRegistration.html', data)

def index(request):
    return render (request, 'index.html')

def listadoProductos(request):
    productos = producto.objects.all()
    data = {'productos': productos}
    return render(request, 'producto.html', data)

def agregarProducto(request):
    form = Formproducto()
    if request.method == 'POST' :
        form = Formproducto(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarProducto.html', data)

def eliminarProducto(request, id):
    Producto = producto.objects.get(id = id)
    Producto.delete()
    return redirect('/producto')

def actualizarProducto(request, id):
    Producto = producto.objects.get(id = id)    
    form = Formproducto(instance=Producto)
    if request.method == 'POST' : 
        form = Formproducto(request.POST, instance=Producto)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarProducto.html', data)
