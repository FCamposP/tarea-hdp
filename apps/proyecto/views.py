from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from apps.proyecto.models import *
import datetime
from apps.proyecto.forms import ProyectoForm
# Create your views here.

class buscarProyecto(TemplateView):
	template_name='proyecto/BuscarProyecto.html'


class asignacionRecurso(TemplateView):
	template_name='proyecto/AsignacionRecurso.html'


def editarProyecto(request):
	if request.method=='POST':
		form=ProyectoForm(request.POST)
		if form.is_valid():
			proyecto=llenarProyecto(form)
			proyecto.save()
			return redirect('/proyectos/busquedaProyecto')
	else:
		form=ProyectoForm

	contexto={'formpro':form}
	return render(request,'proyecto/EditarProyecto.html',contexto)

def llenarProyecto(pro):
	codigoPro="PROY"+str(Proyecto.objects.all().count()+1)
	proyec=Proyecto()
	proyec.idCliente=pro.idCliente
	proyec.codigoProyecto=codigoPro
	proyec.nombreProyecto=pro.nombreProyecto
	proyec.descripcionProyecto=pro.descripcionProyecto
	proyec.ubicacion=pro.ubicacion
	proyec.fechaInicioConstruccion=pro.fechaInicioConstruccion
	return proyec

class detalleProyecto(TemplateView):
	template_name='proyecto/DetalleProyecto.html'

class solicitarRecursos(TemplateView):
	template_name='proyecto/SolicitarRecursos.html'

class verProyecto(TemplateView):
	template_name='proyecto/VerProyecto.html'