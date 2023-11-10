from django.contrib import admin
from AppEmpresa.models import producto

class productoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'litro', 'tamanio','precio','proveedor','tipoagua']

# Register your models here.
admin.site.register(producto, productoAdmin)