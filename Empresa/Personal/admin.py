from django.contrib import admin
from Personal.models import Personal

class PersonalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cargo', 'edad', 'experiencia', 'telefono', 'email']
    
# Register your models here.
admin.site.register(Personal, PersonalAdmin)