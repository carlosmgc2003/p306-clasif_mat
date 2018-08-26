from django import forms
from .models import Registro
from django.utils.translation import ugettext_lazy as _

class CargarFormulario(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('anio','contenido','cant_hojas','archivo')
        labels = {
            'anio': _('Año:'),
            'contenido': _('Contenido:'),
            'cant_hojas': _('Páginas:'),
            'archivo': _('Archivo:')
        }