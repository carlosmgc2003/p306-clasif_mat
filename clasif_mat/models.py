from django.db import models
from django.utils import timezone

ANIOS_VALIDOS = []
for i in range(1930,2000):
    ANIOS_VALIDOS.append((i,i))

ESTADO_CONSERVACION = [(None,"Seleccionar"),
    ("Malo","Malo"),
    ("Regular","Regular"),
    ("Bueno","Bueno"),
    ("Muy bueno","Muy bueno"),
    ("Excelente","Excelente")]

ESTADO_ESCANEO = [(None,"Seleccionar"),
    ("Completo","Completo"),
    ("Incompleto","Incompleto")]

CONTINENTE = [(None,"Seleccionar"),
    ("Libro","Libro o encuadernado"),
    ("Perforado","Perforado o carpeta de cartulina"),
    ("Anillado","Anillado")]

ESTANTES = []
ESTANTES.append((0,0))
for i in range(1,11):
    ESTANTES.append((i,i))

class Registro(models.Model):
    autor = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    anio = models.PositiveSmallIntegerField(choices = ANIOS_VALIDOS)
    estante = models.PositiveSmallIntegerField(choices = ESTANTES,default = 0)
    caja = models.CharField(blank = True,max_length = 10)
    contenido = models.CharField(max_length = 400)
    estado_conservacion = models.CharField(choices = ESTADO_CONSERVACION,default=None,max_length=20)
    estado_escaneo = models.CharField(choices = ESTADO_ESCANEO,default=None,max_length=20)
    continente = models.CharField(choices = CONTINENTE,default=None,max_length=20)
    cant_hojas = models.PositiveSmallIntegerField(default = 1)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    #Aca se guardará el archivo PDF(no validado)... Se concatena a lo determinado en setting.py MEDIA_ROOT
    archivo = models.FileField(upload_to = 'uploads/%Y/%m/%d/',default = '')
    observaciones = models.TextField(max_length=1000,blank=True,default = "")

   
    def __str__(self):
        return self.contenido +" de "+str(self.anio)+" escaneado por: "+str(self.autor)
