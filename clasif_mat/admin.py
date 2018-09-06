from django.contrib import admin
from .models import Registro

# Register your models here.
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('anio','contenido','estado_conservacion',
        'estado_escaneo','continente','cant_hojas',
        'archivo','observaciones')
    search_fields = ('autor','anio')

admin.site.register(Registro, RegistroAdmin)