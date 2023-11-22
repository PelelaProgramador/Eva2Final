from django.shortcuts import render, redirect
from Personal.models import Personal
from Personal.forms import PersonalForm
from . import forms

def listadoPersonal(request):
    personales = Personal.objects.all()
    data = {'personales': personales}
    return render(request, 'Personal/personal.html', data)

def agregarPersonal(request):
    form = PersonalForm()
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listado_personal')
    data = {'form': form}
    return render(request, 'Personal/AgregarPersonal.html', data)

def eliminarPersonal(request, id):
    persona = Personal.objects.get(id=id)
    persona.delete()
    return redirect('listado_personal')

def actualizarPersonal(request, id):
    persona = Personal.objects.get(id=id)
    form = PersonalForm(instance=persona)
    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
        return redirect('listado_personal')
    data = {'form': form}
    return render(request, 'Personal/agregarPersonal.html', data)
