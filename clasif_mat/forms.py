from django import forms
from .models import Registro
from django.utils.translation import ugettext_lazy as _

class CargarFormulario(forms.ModelForm):
    
    class Meta:
        model = Registro
        fields = ('anio','estante','caja','contenido','estado_conservacion',
        'estado_escaneo','continente','cant_hojas',
        'archivo','observaciones')
        labels = {
            'anio': _('Año:'),
            'estante': _('Estante:'),
            'caja': _('Caja:'),
            'contenido': _('Contenido:'),
            'estado_conservacion':_('Estado de conservación:'),
            'estado_escaneo':_('Estado de escaneo:'),
            'continente':_('Tipo de continente:'),
            'cant_hojas': _('Páginas:'),
            'archivo': _('Archivo:'),
            'observaciones':_('Observaciones:')
        }
        help_texts = {
            'anio': _('Año de creación del documento.'),
            'estante': _('Donde esta el documento físico original.'),
            'caja': _('Nomenclatura de la caja donde esta el documento físico.'),
            'contenido': _('Tema de la documentación escaneada, normalmente el titulo.'),
            'estado_conservacion':_('Legibilidad del documento orientada al reconocimiento de texto.'),
            'continente':_('Tipo de encuadernado.'),
            'cant_hojas': _('Páginas totales del archivo escaneado'),
            'archivo': _('Seleccione el archivo a subir. Debe estar en formato PDF y su nombre sin espacios ni \ / : * ? " < > |'),
            'observaciones':_('Alguna información más, de interes para el equipo de investigación.')
        }