from django import forms
from .models import Registro
from django.utils.translation import ugettext_lazy as _

class CargarFormulario(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('anio','contenido','estado_conservacion',
        'estado_escaneo','continente','cant_hojas',
        'archivo','observaciones')
        labels = {
            'anio': _('Año:'),
            'contenido': _('Contenido:'),
            'estado_conservacion':_('Estado de conservación:'),
            'estado_escaneo':_('Estado de escaneo:'),
            'continente':_('Tipo de continente:'),
            'cant_hojas': _('Páginas:'),
            'archivo': _('Archivo:'),
            'observaciones':_('Observaciones:')
        }