from django.shortcuts import render
from .models import Registro

# Create your views here.
def lista_registros(request):
    registros = Registro.objects.order_by('fecha_digit')
    return render(request, 'clasif_mat/lista_registros.html',{'registros':registros})