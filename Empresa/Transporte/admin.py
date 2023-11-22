from django.contrib import admin
from Transporte.models import Transporte

class TransporteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'modelo', 'capacidad', 'fecha_fabricacion', 'estado', 'costo_mantenimiento']
# Register your models here.
admin.site.register(Transporte, TransporteAdmin)
