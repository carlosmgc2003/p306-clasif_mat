from django.contrib import admin
from .models import Registro

# Register your models here.
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('autor','anio','contenido','cant_hojas','archivo')
    search_fields = ('autor','anio')

admin.site.register(Registro, RegistroAdmin)