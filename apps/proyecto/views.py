from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class buscarProyecto(TemplateView):
	template_name='proyecto/BuscarProyecto.html'