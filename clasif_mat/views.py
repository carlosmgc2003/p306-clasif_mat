from django.shortcuts import render, get_object_or_404
from .models import Registro

# Create your views here.
def lista_registros(request):
    registros = Registro.objects.order_by('fecha_digit')
    return render(request, 'clasif_mat/lista_registros.html',{'registros':registros})

def detalle_registro(request,pk):
    registros = get_object_or_404(Registro, pk=pk)
    return render(request, 'clasif_mat/registro_detalle.html', {'registros':registros})