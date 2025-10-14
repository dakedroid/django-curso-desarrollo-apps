from django.contrib import admin
from .models import Carrera, Estudiante

#Clases decoradoras para mejorar la vista en el admin
class EstudianteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'appat',
        'apmat',
        'curp',
        'matricula',
        'carrera',
    )
    #Atributo para busqueda por campo. Debemos separar por comas cada elemento
    search_fields = ('nombre',)
    list_filter = ('carrera',)

class CarreraAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'clave',
        'modalidad',
    )
    #Atributo para busqueda por campo. Debemos separar por comas cada elemento
    search_fields = ('nombre',)

admin.site.register(Carrera,CarreraAdmin)
admin.site.register(Estudiante,EstudianteAdmin)
