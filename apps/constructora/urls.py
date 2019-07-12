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
    url(r'^solicitud/$',login_required(aprobarSolicitud),name="solicitud"),
    url(r'^verDetalleSolicitud/(?P<id_p>\d+)/$',login_required(verDetalleSolicitud),name="verDetalleSolicitud"),

     #vista Sebas
    url(r'^RecursosProyecto/$',login_required(listaRecursos),name="RecursosProyecto"),
    url(r'^Asistencia/$',login_required(mostrarAsistencia),name="Asistencia"),
    url(r'^recursosEmpleado/$',login_required(listarEmpleadosProyecto),name="recursosEmpleado"),
    url(r'^CambioActivo/(?P<id_asignacionPuestoProyecto>\d+)/$',login_required(activo), name="CambioActivo"),
    url(r'^CambioActivo1(?P<id_ejemplar>\d+)/$',login_required(activo1), name="CambioActivo1"),
    url(r'^CambioActivo2/(?P<id_herramienta>\d+)/$',login_required(activo2), name="CambioActivo2"),
    url(r'^registroAsistencia/(?P<id_asistencia>\d+)/$',login_required(registroAsistencia), name="registroAsistencia"),
    #fin

#fin URL Fc


    url(r'^contrato/$',login_required(verContrato),name="contrato"),
    url(r'^empleado/$',login_required(verEmpleado),name="empleado"),
    url(r'^verCliente/$',login_required(verCliente),name="verCliente"),
    url(r'^nuevoEmpleado/$',login_required(crearEmpleado),name="nuevoEmpleado"),
    url(r'^crearCliente/$',login_required(nuevoCliente),name="crearCliente"),
    url(r'^editarEmpleado/(?P<id_empleado>\d+)/$',login_required(editarEmpleado),name="editarEmpleado"),
    url(r'^editarCliente/(?P<id_cliente>\d+)/$',login_required(editarCliente),name="editarCliente"),
    url(r'^eliminarEmpleado/(?P<id_empleado>\d+)/$',login_required(eliminarEmpleado),name="eliminarEmpleado"),
    url(r'^eliminarCliente/(?P<id_cliente>\d+)/$',login_required(eliminarCliente),name="eliminarCliente"),
    url(r'^verPuesto/$',login_required(verPuesto),name="verPuesto"),    
    url(r'^crearPuesto/$',login_required(crearPuesto),name="crearPuesto"),
    url(r'^eliminarPuesto/(?P<id_puesto>\d+)/$',login_required(eliminarPuesto),name="eliminarPuesto"),
    url(r'^editarPuesto/(?P<id_puesto>\d+)/$',login_required(editarPuesto),name="editarPuesto"),

    #INICIO URLS MARCO
    #url(r'^recursolist/$',login_required(recursoList),name="recursoList"),
    url(r'^recursoList/$',login_required(recursoList),name="recursoList"),
    url(r'^agregarRecurso/$',login_required(recursoAgregar), name='agregarRecurso'),
    path('modificarRecurso/<str:codigoRecurso>/',login_required(recursoModificar), name='modificarRecurso'),
    path('ejemplarList/<str:codigoRecurso>/',login_required(ejemplarList), name='ejemplarList'),
    url(r'^herramientaList/$',login_required(herramientaList),name="herramientaList"),
    #FIN URLS MARCO

] 
