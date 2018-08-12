from django.shortcuts import render

# Create your views here.
def lista_registros(request):
    return render(request, 'clasif_mat/lista_registros.html',{})