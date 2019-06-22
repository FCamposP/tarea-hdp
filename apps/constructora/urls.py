from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from apps.constructora.views import *
from django.contrib.auth.views import login

app_name="constructora" 
urlpatterns = [
    url(r'^index/$',login_required(Vista.as_view()),name="index"),
    #   URL Fc
    url(r'^busquedaProyecto/$',login_required(buscarProyecto),name="busquedaProyecto"),
    url(r'^nuevoProyecto/$',login_required(nuevoProyecto),name="nuevoProyecto"),
    url(r'^editarProyecto/(?P<id_p>\d+)/$',login_required(editarProyecto),name="editarProyecto"),
    url(r'^asignacionRecurso/(?P<id_p>\d+)/$',login_required(asignacionRecurso),name="asignacionRecurso"),
    url(r'^recursosProyecto/$',login_required(recursosProyecto.as_view()),name="recursosProyecto"),
    url(r'^solicitarRecursos/$',login_required(solicitarRecursos),name="solicitarRecursos"),
    url(r'^verProyecto/$',login_required(verProyecto.as_view()),name="verProyecto"),
    url(r'^prueba/$',login_required(prueba),name="prueba"),
    url(r'^ConseguirTipoRecurso/$',login_required(ConseguirTipoRecurso),name="ConseguirTipoRecurso"),
    url(r'^conseguirElemento/$',login_required(conseguirElemento),name="conseguirElemento"),
    url(r'^editarEmpleado/(?P<id_empleado>\d+)/$',login_required(editarEmpleado),name="editarEmpleado"),
    url(r'^eliminarEmpleado/(?P<id_empleado>\d+)/$',login_required(eliminarEmpleado),name="eliminarEmpleado"),

     #vista Sebas
    url(r'^recursosProyecto/$',login_required(recursosProyecto.as_view()),name="recursosProyecto"),
    url(r'^MuestrAsistencias/$',login_required(mostrarAsistencia),name="MuestrAsistencias"),
    url(r'^registroAsistencias/$',login_required(registroAsistencia),name="registroAsistencias"),
    #fin

#fin URL Fc


    url(r'^contrato/$',login_required(verContrato),name="contrato"),
    url(r'^empleado/$',login_required(verEmpleado),name="empleado"),
    url(r'^nuevoEmpleado/$',login_required(crearEmpleado),name="nuevoEmpleado"),
    

    #INICIO URLS MARCO
    #url(r'^recursolist/$',login_required(recursoList),name="recursoList"),
    url(r'^recursoList/$',login_required(recursoList),name="recursoList"),
    url(r'^agregarRecurso/$',login_required(recursoAgregar), name='agregarRecurso'),
    path('modificarRecurso/<str:codigoRecurso>/',login_required(recursoModificar), name='modificarRecurso'),
    path('ejemplarList/<str:codigoRecurso>/',login_required(ejemplarList), name='ejemplarList'),
    #FIN URLS MARCO

] 
