from django.db import models
from apps.empleado.models import Empleado
from apps.recurso.models import Recurso
# Create your models here.

class Cliente(models.Model):
    codigoCliente=models.CharField(max_length=10)
    nombreCliente=models.CharField(max_length=50)
    direccion=models.CharField(max_length=200)
    email=models.EmailField(max_length=55)
    nit=models.CharField(max_length=15)
    giro=models.CharField(max_length=50)
    numTelefono=models.CharField(max_length=15)
    def __str__(self): 
    	return self.nombreCliente    

class Puesto(models.Model):
    codigoPuesto=models.CharField(max_length=10)
    nombrePuesto=models.CharField(max_length=25)
    descripcionPuesto=models.CharField(max_length=150)
    salario=models.DecimalField(max_digits=9,decimal_places=2)

class Proyecto(models.Model):
    idCliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    codigoProyecto=models.CharField(max_length=10)
    nombreProyecto=models.CharField(max_length=25)
    descripcionProyecto=models.CharField(max_length=250)
    ubicacion=models.CharField(max_length=200)
    fechaInicioConstruccion=models.DateField(null=True)
    fechaFinalizacion=models.DateField(null=True)

class AsignacionPuestoProyecto(models.Model):
    empleado=models.ForeignKey(Empleado,on_delete=models.CASCADE)
    puesto=models.ForeignKey(Puesto,on_delete=models.CASCADE)
    proyecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE)

class Tarea(models.Model):
    codigoPuesto=models.ForeignKey(Puesto,on_delete=models.CASCADE)
    nombreActividad=models.CharField(max_length=25)
    descripcion=models.CharField(max_length=150)
    tiempoEstimado=models.CharField(max_length=35)

class Solicitud(models.Model):
    fechaSolicitud=models.DateField(auto_now_add=True)
    solicitante=models.OneToOneField(Puesto,on_delete=models.CASCADE)


class DetalleSolicitud(models.Model):
    solicitud=models.ForeignKey(Solicitud,on_delete=models.CASCADE)
    recurso=models.ForeignKey(Recurso,on_delete=models.CASCADE)
    cantidad=models.IntegerField