from django.shortcuts import render, redirect
from Transporte.models import Transporte
from Transporte.forms import TransporteForm
from . import forms

def listadoTransportes(request):
    transportes = Transporte.objects.all()
    data = {'transportes': transportes}
    return render(request, 'Transporte/transporte.html', data)

def agregarTransporte(request):
    form = TransporteForm()
    if request.method == 'POST':
        form = TransporteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listado_transportes')
    data = {'form': form}
    print(form)
    print(data)
    return render(request, 'Transporte/AgregarTransporte.html', data)

def eliminarTransporte(request, id):
    transporte = Transporte.objects.get(id=id)
    transporte.delete()
    return redirect('listado_transportes')

def actualizarTransporte(request, id):
    transporte = Transporte.objects.get(id=id)
    form = TransporteForm(instance=transporte)  
    if request.method == 'POST':
        form = TransporteForm(request.POST, instance=transporte)
        if form.is_valid():
            form.save()
        return redirect('listado_transportes')
    data = {'form': form}
    return render(request, 'Transporte/AgregarTransporte.html', data)
