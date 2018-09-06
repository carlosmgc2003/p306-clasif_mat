from django.db import models
from django.utils import timezone

ANIOS_VALIDOS = []
for i in range(1930,1991):
    ANIOS_VALIDOS.append((i,i))
# Create your models here.

ESTADO_CONSERVACION = [(0,"Seleccionar"),
    (1,"Malo"),
    (2,"Regular"),
    (3,"Bueno"),
    (4,"Muy bueno"),
    (5,"Excelente")]

ESTADO_ESCANEO = [(0,"Seleccionar"),
    (1,"Completo"),
    (2,"Incompleto")]

CONTINENTE = [(0,"Seleccionar"),
    (1,"Libro"),
    (2,"Perforado"),
    (3,"Anillado")]

class Registro(models.Model):
    autor = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    anio = models.PositiveSmallIntegerField(choices = ANIOS_VALIDOS)
    contenido = models.CharField(max_length = 400)
    estado_conservacion = models.PositiveSmallIntegerField(choices = ESTADO_CONSERVACION,default=0)
    estado_escaneo = models.PositiveSmallIntegerField(choices = ESTADO_ESCANEO,default=0)
    continente = models.PositiveSmallIntegerField(choices = CONTINENTE,default=0)
    cant_hojas = models.PositiveSmallIntegerField(default = 1)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    #Aca se guardará el archivo PDF(no validado)... Se concatena a lo determinado en setting.py MEDIA_ROOT
    archivo = models.FileField(upload_to = 'uploads/%Y/%m/%d/',default = '')
    observaciones = models.TextField(max_length=1000,null=True)

   
    def __str__(self):
        return self.contenido +" de "+str(self.anio)+" escaneado por: "+str(self.autor)
