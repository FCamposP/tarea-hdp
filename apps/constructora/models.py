from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recurso(models.Model):
    codigoRecurso=models.CharField(max_length=10,primary_key=True)
    nombreRecurso=models.CharField(max_length=25)
    tipoRecurso=models.CharField(max_length=20)
    descripcionRecurso=models.CharField(max_length=150)
    def __str__(self): 
    	return self.nombreRecurso   

class Ejemplar(models.Model):
    codigoEjemplar=models.CharField(max_length=10,primary_key=True)
    idRecurso=models.ForeignKey(Recurso,on_delete=models.CASCADE)
    nombreEjemplar=models.CharField(max_length=25)
    descripcionEjemplar=models.CharField(max_length=100)
    disponible=models.BooleanField(default=True)
    def __str__(self):  
    	return self.codigoEjemplar   

class Herramienta(models.Model):
    codigoHerramienta=models.CharField(max_length=10,primary_key=True)
    nombreHerramienta=models.CharField(max_length=15)
    cantidadHerramienta=models.IntegerField(default=0)
    canatidadDisponibles=models.IntegerField(default=0)
    descripcionHerramienta=models.CharField(max_length=100)
    def __str__(self): 
    	return self.nombreHerramienta  

class Cliente(models.Model):
    codigoCliente=models.CharField(max_length=10)
    nombreCliente=models.CharField(max_length=50)
    direccion=models.CharField(max_length=200)
    email=models.EmailField(max_length=30)
    nit=models.CharField(max_length=14)
    giro=models.CharField(max_length=50)
    numTelefono=models.CharField(max_length=8)
    def __str__(self): 
    	return self.nombreCliente   

class Proyecto(models.Model):
    idCliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    codigoProyecto=models.CharField(max_length=10)
    nombreProyecto=models.CharField(max_length=25)
    descripcionProyecto=models.CharField(max_length=250)
    ubicacion=models.CharField(max_length=200)
    fechaInicioConstruccion=models.DateField(null=True)
    fechaFinalizacion=models.DateField(null=True)
    finalizado=models.BooleanField(default=False)
    def __str__(self): 
    	return self.nombreProyecto 

class AsignacionHerramienta(models.Model):
    idProyecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    Herramienta=models.ForeignKey(Herramienta,on_delete=models.CASCADE)
    fechaAsignacion=models.DateField(auto_now_add=True)
    fechaDisponible=models.DateField(auto_now_add=True)
    cantidadAsignada=models.IntegerField(default=0)
    activo= models.BooleanField(default=True)

class AsignacionoEjemplar(models.Model):
    idProyecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    ejemplar=models.ForeignKey(Ejemplar,on_delete=models.CASCADE)
    fechaAsignacion=models.DateField(auto_now_add=True)
    fechaDisponible=models.DateField(auto_now_add=True) 
    activo=models.BooleanField(default=True)

class Puesto(models.Model): 
    codigoPuesto=models.CharField(max_length=10)
    nombrePuesto=models.CharField(max_length=25)
    descripcionPuesto=models.CharField(max_length=150)
    def __str__(self): 
    	return self.nombrePuesto 

class Empleado(models.Model):
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    direccion=models.CharField(max_length=250)
    numTelefono=models.CharField(max_length=8)
    dui=models.CharField(max_length=9)
    nit=models.CharField(max_length=14)
    isss=models.CharField(max_length=15)
    disponible=models.BooleanField(default=True)
    def __str__(self): 
    	return self.nombres 

class AsignacionPuestoProyecto(models.Model):
    empleado=models.ForeignKey(Empleado,on_delete=models.CASCADE)
    puesto=models.ForeignKey(Puesto,on_delete=models.CASCADE)
    proyecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    salario=models.DecimalField(max_digits=9,decimal_places=2)
    activo=models.BooleanField(default=True)
    def __str__(self): 
    	return self.proyecto.nombreProyecto+"-"+self.puesto.nombrePuesto+"-"+self.empleado.nombres

class Tarea(models.Model):
    codigoPuesto=models.ForeignKey(Puesto,on_delete=models.CASCADE)
    nombreActividad=models.CharField(max_length=25)
    descripcion=models.CharField(max_length=150)
    tiempoEstimado=models.CharField(max_length=35)
    def __str__(self): 
    	return self.nombreActividad 

class Solicitud(models.Model):
    fechaSolicitud=models.DateField(auto_now_add=True)
    solicitante=models.ForeignKey(AsignacionPuestoProyecto,on_delete=models.CASCADE)
    aprobado=models.BooleanField(default=False)

class DetalleSolicitud(models.Model):
    solicitud=models.ForeignKey(Solicitud,on_delete=models.CASCADE)
    tiporecurso=models.CharField(max_length=150)
    recurso=models.CharField(max_length=150)
    cantidad=models.IntegerField(default=0)
    asignado=models.BooleanField(default=False)

class AsignacionUsuario(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    empleado_proyecto=models.OneToOneField(AsignacionPuestoProyecto,on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=25)
    descripcion_tipo_usuario = models.CharField(max_length=150)
    def __str__(self): 
    	return self.empleado_proyecto.proyecto.nombreProyecto+"-"+self.empleado_proyecto.puesto.nombrePuesto+"-"+self.empleado_proyecto.empleado.nombres

class Contrato(models.Model):
    empleado=models.ForeignKey(Empleado,on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=200)
    fechaContratacion=models.DateField(auto_now_add=True)
    periodoContrato=models.CharField(max_length=10)

class Asistencia(models.Model):
    Asignacion=models.ForeignKey(AsignacionPuestoProyecto,on_delete=models.CASCADE, default= "", editable = False)
    fechaAsistencia=models.DateField(auto_now_add=True)
    asistencia=models.BooleanField(default=True)
