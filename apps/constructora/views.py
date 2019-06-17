from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from apps.constructora.models import *
from apps.constructora.forms import *
from django.urls import reverse_lazy,reverse
import datetime
from apps.constructora.forms import ProyectoForm
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

class Vista(TemplateView):
	template_name='home/home.html'

#INICIO DE VISTAS MARCO

def recursoList(request):

	if 'accion' in request.POST:
		accion = request.POST['accion']
		codigo_recurso = request.POST['recurso']
		recurso = Recurso.objects.get(codigoRecurso = codigo_recurso)
		if accion == 'Eliminar':	
			recurso.delete()
			pass
		else:
			pass
		pass
	recurso = Recurso.objects.all().order_by('codigoRecurso')
	contexto = {'recursos':recurso}
	return render(request, 'recursos/listaRecurso2.html', contexto)	

def recursoAgregar(request):
	if request.method == 'POST':
		form = RecursoForm(request.POST)
		if form.is_valid():
			form.save()
			pass
		pass
		return redirect('constructora:recursoList')
	else:
		form = RecursoForm()
	return render(request, 'recursos/agregarRecurso.html', {'form':form})

def recursoModificar(request, codigoRecurso):
	recurso = Recurso.objects.get(pk=codigoRecurso)
	if request.method == 'GET':
		form1 = RecursoForm(instance=recurso)
	else:
		form1 = RecursoForm(request.POST, instance=recurso)
		if form1.is_valid():
			form1.save()
		return redirect('constructora:recursoList')
	return render(request, 'recursos/agregarRecurso.html', {'form1':form1})


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
	idUsuario=request.user.id
	pro=Proyecto.objects.filter(finalizado=False)
	pues=Puesto.objects.all()
	recursos=Recurso.objects.all()
	emp=Empleado.objects.filter(disponible=True)
	herramientas=Herramienta.objects.all()

	contexto={'proyectos':pro,'puestos':pues,'empleados':emp,'recursos':recursos,'herramientas':herramientas}
	return render(request,'proyecto/AsignacionRecurso.html',contexto)



def eliminarRecurso(request, id_p, tipo_rec):
	contexto={}
	if(tipo_rec==1):
		dato=AsignacionPuestoProyecto.objects.get(id=id_p)
		contexto={'dato':dato}
		if request.method=='POST':
			dato.delete()
			return redirect('constructora:asignacionRecurso')
			pass
		

	return render(request,'proyecto/EliminarRecurso.html',contexto)



def prueba(request):
	ejemplares=Ejemplar.objects.filter(idRecurso=request.GET['id_re'],disponible=True)
	
	data=serializers.serialize('json',ejemplares)
	print(data)
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