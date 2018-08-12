from django.db import models
from django.utils import timezone

# Create your models here.
class Registro(models.Model):
    autor = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    anio = models.PositiveSmallIntegerField()
    orden = models.PositiveIntegerField()
    contenido = models.CharField(max_length = 200)
    cant_hojas = models.PositiveSmallIntegerField()
    fecha_digit = models.DateTimeField(blank = True, null = True)
    def digitalizacion(self):
        self.fecha_digit = timezone.now()
        self.save()
    
    def __str__(self):
        return self.contenido