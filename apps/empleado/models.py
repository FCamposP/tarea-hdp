from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    direccion=models.CharField(max_length=250)
    numTelefono=models.CharField(max_length=15)
    dui=models.CharField(max_length=15)
    nit=models.CharField(max_length=15)
    isss=models.CharField(max_length=15)

class Contrato(models.Model):
    empleado=models.ForeignKey(Empleado,on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=200)
    fechaContratacion=models.DateField(auto_now_add=True)
    periodoContrato=models.CharField(max_length=10)

class Asistencia(models.Model):
    puesto=models.ForeignKey('proyecto.Puesto',on_delete=models.CASCADE)
    fechaAsistencia=models.DateField(auto_now_add=True)
    asistencia=models.BooleanField
