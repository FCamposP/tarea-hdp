from django.contrib import admin
from apps.recurso.models import *
# Register your models here.

admin.site.register(Recurso)
admin.site.register(Ejemplar)
admin.site.register(Herramienta)
admin.site.register(AsignacionHerramienta)
admin.site.register(AsignacionoEjemplar)

