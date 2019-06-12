from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from apps.proyecto.views import *
from django.contrib.auth.views import login

app_name="proyectos"
urlpatterns = [
    url(r'^busquedaProyecto/$',login_required(buscarProyecto),name="busquedaProyecto"),
    url(r'^nuevoProyecto/$',login_required(nuevoProyecto),name="nuevoProyecto"),
    url(r'^editarProyecto/$',login_required(editarProyecto),name="editarProyecto"),
    url(r'^asignacionRecurso/$',login_required(asignacionRecurso.as_view()),name="asignacionRecurso"),
    url(r'^recursosProyecto/$',login_required(recursosProyecto.as_view()),name="recursosProyecto"),
    url(r'^solicitarRecursos/$',login_required(solicitarRecursos.as_view()),name="solicitarRecursos"),
    url(r'^verProyecto/$',login_required(verProyecto.as_view()),name="verProyecto"),

]
