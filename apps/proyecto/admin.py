from django.contrib import admin
from apps.proyecto.models import *
# Register your models here.

admin.site.register(Proyecto)
admin.site.register(Cliente)
admin.site.register(Puesto)
admin.site.register(AsignacionPuestoProyecto)
admin.site.register(Tarea)
admin.site.register(Solicitud)
admin.site.register(DetalleSolicitud)
