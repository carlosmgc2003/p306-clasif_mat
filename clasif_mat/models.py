from django.db import models
from django.utils import timezone

ANIOS_VALIDOS = []
for i in range(1930,1991):
    ANIOS_VALIDOS.append((i,i))
# Create your models here.

class Registro(models.Model):
    autor = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    anio = models.PositiveSmallIntegerField(choices = ANIOS_VALIDOS)
    contenido = models.CharField(max_length = 400, help_text = "Breve descripcion hasta 400 carácteres.")
    cant_hojas = models.PositiveSmallIntegerField(default = 1)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    #Aca se guardará el archivo PDF(no validado)... Se concatena a lo determinado en setting.py MEDIA_ROOT
    archivo = models.FileField(upload_to = 'uploads/%Y/%m/%d/',default = '',help_text = "Archivo PDF sin espacios ni carácteres especiales en el nombre.")

   
    def __str__(self):
        return self.contenido +" de "+str(self.anio)+" escaneado por: "+str(self.autor)+" en: "+str(self.fecha_digit)
