from django import forms
from .models import Registro
from django.utils.translation import ugettext_lazy as _

class CargarFormulario(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('anio','orden','contenido','cant_hojas','fecha_digit')
        labels = {
            'anio': _('Año:'),
            'orden': _('Orden:'),
            'contenido': _('Contenido:'),
            'cant_hojas': _('Páginas:'),
            'fecha_digit': _('Fecha digit.:')
        }