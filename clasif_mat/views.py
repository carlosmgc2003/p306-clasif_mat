from django.shortcuts import render, get_object_or_404, redirect
from .models import Registro
from .forms import CargarFormulario
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
@method_decorator(login_required, name='dispatch')
class VistaListaRegistros(ListView):
    model = Registro
    context_object_name = 'registros'
    template_name = 'lista_registros.html'

@method_decorator(login_required, name='dispatch')
class VistaEliminarRegistro(DeleteView):
    model = Registro
    success_url = reverse_lazy('home')
    template_name = 'registro_eliminar.html'

@login_required
def detalle_registro(request,pk):
    registro = get_object_or_404(Registro, pk=pk)
    return render(request, 'registro_detalle.html', {'registro':registro})

@method_decorator(login_required, name='dispatch')
class VistaNuevoRegistro(CreateView):
    def post(self,request):
        form = CargarFormulario(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.autor = request.user
            post.fecha_creacion = timezone.now()
            form.save()
            return redirect('detalle_registro',pk = post.pk)
        return render(request, 'nuevo_registro.html', {'form':form})
    
    def get(self, request):
        form = CargarFormulario(request.POST,request.FILES)
        return render(request, 'nuevo_registro.html', {'form':form})


@method_decorator(login_required, name='dispatch')
class VistaModificarRegistro(UpdateView):
    model = Registro
    fields = ('anio','contenido','estado_conservacion',
        'estado_escaneo','continente','cant_hojas',
        'archivo','observaciones')
    template_name = 'nuevo_registro.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'form'

    def form_valid(self,form):
        post = form.save(commit = False)
        post.autor = self.request.user
        post.save()
        return redirect('detalle_registro', pk = post.pk)



@login_required
def vista_pdf(request,year,month,day,name):
    path = "uploads/"+str(year)+"/"+str(month)+"/"+str(day)+"/"+name+".pdf"
    image_data = open(path, "rb").read()
    return HttpResponse(image_data, content_type="application/pdf")

