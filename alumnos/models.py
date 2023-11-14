from django.db import models

# Create your models here.
class Alumno(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    nombres = models.CharField(max_length=100, blank=False, null=False)
    apellidos = models.CharField(max_length=100, blank=False, null=False)
    matricula = models.CharField(max_length=20, blank=False, null=False)
    promedio = models.DecimalField(max_digits=4, decimal_places=2, blank=False, null=False)