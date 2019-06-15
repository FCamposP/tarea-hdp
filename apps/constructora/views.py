from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from apps.constructora.models import *
import datetime
from apps.constructora.forms import ProyectoForm
from django.core import serializers
from django.http import HttpResponse
# Create your views here.

class Vista(TemplateView):
	template_name='home/home.html'

#INICIO DE VISTAS MARCO




#FIN DE VISTAS MARCO


#INICIO DE VISTAS KILMER
def ListaEmpleado(request):
	
	return render(request,'empleados/empleado.html')

def crearEmpleado(request):
	
	return render(request,'empleados/crearEmpleado.html')

#FIN VISTAS KILMER


#INICIO VISTAS SEBASTIAN


#FIN VISTAS SEBASTIAN 


#INICIO VISTAS FC

def editarProyecto(request,id_p):
	clie="";nombreP='';descripcionP='';ubicacion=""
	datosProy=Proyecto.objects.get(id=id_p)
	clientes=Cliente.objects.all()
	if request.method=='POST':
		proyecto=Proyecto.objects.get(id=id_p)
		proyecto.idCliente=Cliente.objects.get(nombreCliente=request.POST['selectCliente'])
		proyecto.nombreProyecto=request.POST['nombrePro']
		proyecto.descripcionProyecto=request.POST['descripcion']
		proyecto.ubicacion=request.POST['ubicacion']
		proyecto.save()
		return redirect('constructora:busquedaProyecto')
	contexto={'proyecto':datosProy,'clientes':clientes}
	return render(request,'proyecto/EditarProyecto.html',contexto)


def buscarProyecto(request):
	proyectos=Proyecto.objects.all()
	contexto={'proyectos':proyectos}
	return render(request,'proyecto/BuscarProyecto.html',contexto)

def asignacionRecurso(request):
	pro=Proyecto.objects.filter(finalizado=False)
	pues=Puesto.objects.all()
	recursos=Recurso.objects.all()
	emp=Empleado.objects.filter(disponible=True)
	herramientas=Herramienta.objects.all()
	contexto={'proyectos':pro,'puestos':pues,'empleados':emp,'recursos':recursos,'herramientas':herramientas}
	return render(request,'proyecto/AsignacionRecurso.html',contexto)

def obtenerEjemplares(request):
	id_recurso=request.GET['id']
	return redirect('constructora:busquedaProyecto')
	ejem=Ejemplar.objects.filter(idRecurso=id_recurso,disponible=True)
	data=serializers.serialize('json',ejem,
	fields=('id','codigoEjemplar','nombreEjemplar','descripcionEjemplar'))
	return HttpResponse(data,content_type='application/json')


def nuevoProyecto(request):
	if request.method=='POST':
		form=ProyectoForm(request.POST)
		if form.is_valid():
			codigoPro="PROY"+str(Proyecto.objects.all().count()+1)
			proyec=Proyecto()
			
			proyec.idCliente=Cliente.objects.get(id=request.POST['idCliente'])
			proyec.codigoProyecto=codigoPro
			proyec.nombreProyecto=request.POST['nombreProyecto']
			proyec.descripcionProyecto=request.POST['descripcionProyecto']
			proyec.ubicacion=request.POST['ubicacion']
			proyec.fechaInicioConstruccion=request.POST['fechaInicioConstruccion']	
			proyec.save()		
			return redirect('constructora:busquedaProyecto')
	else:
		form=ProyectoForm

	contexto={'formpro':form}
	return render(request,'proyecto/NuevoProyecto.html',contexto)

class recursosProyecto(TemplateView):
	template_name='proyecto/RecursosProyecto.html'

class solicitarRecursos(TemplateView):
	template_name='proyecto/SolicitarRecursos.html'

class verProyecto(TemplateView):
	template_name='proyecto/VerProyecto.html'

#FIN VISTAS FC