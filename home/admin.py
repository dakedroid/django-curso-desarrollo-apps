from django.contrib import admin
from .models import Galeria

#Clases decoradoras para mejorar la vista en el admin
class GaleriaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'fecha_subida',
    )

# Register your models here.
admin.site.register(Galeria,GaleriaAdmin)