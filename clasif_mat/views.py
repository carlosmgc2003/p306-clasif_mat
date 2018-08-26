from django.shortcuts import render, get_object_or_404, redirect
from .models import Registro
from .forms import CargarFormulario
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def lista_registros(request):
    registros = Registro.objects.order_by('fecha_creacion')
    return render(request, 'lista_registros.html',{'registros':registros})

@login_required
def detalle_registro(request,pk):
    registros = get_object_or_404(Registro, pk=pk)
    return render(request, 'registro_detalle.html', {'registros':registros})

@login_required
def registro_nuevo(request):
    if request.method == "POST":
        form = CargarFormulario(request.POST,request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            post = form.save(commit = False)
            post.autor = request.user
            post.fecha_creacion = timezone.now()
            form.save()
            return redirect('detalle_registro',pk = post.pk)
    else:
        form = CargarFormulario()
    return render(request, 'nuevo_registro.html', {'form':form})

@login_required
def vista_pdf(request,year,month,day,name):
    path = "uploads/"+str(year)+"/"+str(month)+"/"+str(day)+"/"+name+".pdf"
    image_data = open(path, "rb").read()
    return HttpResponse(image_data, content_type="application/pdf")