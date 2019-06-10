from django.db import models

# Create your models here.

class Recurso(models.Model):
    codigoRecurso=models.CharField(max_length=10)
    nombreRecurso=models.CharField(max_length=25)
    tipoRecurso=models.CharField(max_length=20)
    descripcionRecurso=models.CharField(max_length=150)

class Ejemplar(models.Model):
    idRecurso=models.ForeignKey(Recurso,on_delete=models.CASCADE)
    codigoEjemplar=models.CharField(max_length=10)
    nombreEjemplar=models.CharField(max_length=25)
    descripcionEjemplar=models.CharField(max_length=10)
    disponible=models.BooleanField

class Herramienta(models.Model):
    nombreHerramienta=models.CharField(max_length=15)
    cantidadHerramienta=models.IntegerField
    canatidadDisponibles=models.IntegerField

class AsignacionHerramienta(models.Model):
    idProyecto=models.ForeignKey('proyecto.Proyecto',on_delete=models.CASCADE)
    Herramienta=models.ForeignKey(Herramienta,on_delete=models.CASCADE)
    fechaAsignacion=models.DateField(auto_now_add=True)
    fechaDisponible=models.DateField(auto_now_add=True)

class AsignacionoEjemplar(models.Model):
    idProyecto=models.ForeignKey('proyecto.Proyecto',on_delete=models.CASCADE)
    ejemplar=models.ForeignKey(Ejemplar,on_delete=models.CASCADE)
    fechaAsignacion=models.DateField(auto_now_add=True)
    fechaDisponible=models.DateField(auto_now_add=True)


