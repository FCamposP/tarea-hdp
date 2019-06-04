from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class buscarProyecto(TemplateView):
	template_name='proyecto/BuscarProyecto.html'


class asignacionRecurso(TemplateView):
	template_name='proyecto/AsignacionRecurso.html'


class editarProyecto(TemplateView):
	template_name='proyecto/EditarProyecto.html'

class detalleProyecto(TemplateView):
	template_name='proyecto/DetalleProyecto.html'

class solicitarRecursos(TemplateView):
	template_name='proyecto/SolicitarRecursos.html'

