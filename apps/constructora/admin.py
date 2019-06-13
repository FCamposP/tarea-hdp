from django.contrib import admin
from apps.constructora.models import *
# Register your models here.
admin.site.register(Recurso)
admin.site.register(Ejemplar)
admin.site.register(Herramienta)
admin.site.register(AsignacionHerramienta)
admin.site.register(AsignacionoEjemplar)
admin.site.register(Proyecto)
admin.site.register(Cliente)
admin.site.register(Puesto)
admin.site.register(AsignacionPuestoProyecto)
admin.site.register(Tarea)
admin.site.register(Solicitud)
admin.site.register(DetalleSolicitud)
admin.site.register(AsignacionUsuario)
admin.site.register(Empleado)
admin.site.register(Contrato)
admin.site.register(Asistencia)