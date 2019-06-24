from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from apps.constructora.models import *
import datetime,time
from apps.constructora.forms import *
from django.urls import reverse_lazy,reverse
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
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
		form1 = RecursoForm_2(instance=recurso)
	else:
		form1 = RecursoForm_2(request.POST, instance=recurso)
		if form1.is_valid():
			form1.save()
		return redirect('constructora:recursoList')
	return render(request, 'recursos/agregarRecurso.html', {'form1':form1})

def ejemplarList(request, codigoRecurso):
	recurso = Recurso.objects.get(pk=codigoRecurso)
	if request.method == 'POST':
		if 'accion' in request.POST:
			accion = request.POST['accion']
			if accion == 'Agregar':	
				form=EjemplarForm(request.POST)
				if form.is_valid():
					ejemplar=Ejemplar()
					ejemplar.codigoEjemplar=request.POST['codigoEjemplar']
					ejemplar.idRecurso=recurso
					ejemplar.nombreEjemplar=request.POST['nombreEjemplar']
					ejemplar.descripcionEjemplar=request.POST['descripcionEjemplar']
					ejemplar.disponible='True'
					ejemplar.save()
					pass				
				pass
				return redirect('constructora:ejemplarList',recurso.pk)
			if accion == 'Eliminar':
				codigo_ejemplar = request.POST['ejemplar']
				ejemplar = Ejemplar.objects.get(codigoEjemplar = codigo_ejemplar)	
				ejemplar.delete()
				pass
				return redirect('constructora:ejemplarList',recurso.pk)
			pass
			if accion == 'Modificar':
				codigo_ejemplar = request.POST['ejemplar']
				ejemplar = Ejemplar.objects.get(codigoEjemplar = codigo_ejemplar)
				form1 = EjemplarForm(request.POST, instance=ejemplar)
				if form1.is_valid():
					form1.save()
					return redirect('constructora:ejemplarList',recurso.pk)
					pass
				pass
		pass		
	else:
		form = EjemplarForm()
	pass
	ejemplar = Ejemplar.objects.filter(idRecurso=recurso.codigoRecurso).order_by('codigoEjemplar')
	contexto = {'recurso':recurso, 'ejemplares':ejemplar, 'form':form}
	return render(request, 'ejemplares/listaEjemplar.html', contexto)

def herramientaList(request):
	if request.method == 'POST':
		if 'accion' in request.POST:
			accion = request.POST['accion']
			if accion == 'Agregar':	
				form=HerramientaForm(request.POST)
				if form.is_valid():
					herramienta=Herramienta()
					herramienta.codigoHerramienta=request.POST['codigoHerramienta']
					herramienta.nombreHerramienta=request.POST['nombreHerramienta']
					herramienta.cantidadHerramienta=request.POST['cantidadHerramienta']
					herramienta.canatidadDisponibles=request.POST['cantidadHerramienta']
					herramienta.descripcionHerramienta=request.POST['descripcionHerramienta']
					herramienta.save()
					pass				
				pass
				return redirect('constructora:herramientaList')
			if accion == 'Eliminar':
				codigo_herramienta = request.POST['herramienta']
				herramienta = Herramienta.objects.get(codigoHerramienta = codigo_herramienta)	
				herramienta.delete()
				pass
				return redirect('constructora:herramientaList')
			pass
			if accion == 'Modificar':
				codigo_herramienta = request.POST['herramienta']
				herramienta = Herramienta.objects.get(codigoHerramienta = codigo_herramienta)
				cant_n = request.POST['cantidadHerramienta']
				resta_cant = int(cant_n) - herramienta.cantidadHerramienta
				disp = herramienta.canatidadDisponibles + (resta_cant)
				herramienta.canatidadDisponibles = disp
				form1 = HerramientaForm(request.POST, instance=herramienta)
				if form1.is_valid():
					form1.save()
					return redirect('constructora:herramientaList')
					pass
				pass
		pass		
	else:
		form = HerramientaForm()
	pass	
	herramienta = Herramienta.objects.all().order_by('codigoHerramienta')
	contexto = {'herramientas':herramienta, 'form':form}
	return render(request, 'herramientas/listaHerramientas.html', contexto)
#FIN DE VISTAS MARCO


#INICIO DE VISTAS KILMER
def verEmpleado(request):
	empleados=Empleado.objects.all()
	contexto={'empleados':empleados}
	
	return render(request,'empleados/empleado.html',contexto)

def crearEmpleado(request):
	empleadoContrato = Empleado()
	contratoFinal = Contrato()
	if request.method=='POST':
		form = EmpleadoForm(request.POST)
		formC = ContratoForm(request.POST)
		if form.is_valid():
			
			empleadoContrato.nombres = request.POST['nombres']
			empleadoContrato.apellidos = request.POST['apellidos']
			empleadoContrato.direccion	= request.POST['direccion']
			empleadoContrato.numTelefono = request.POST['numTelefono']
			empleadoContrato.dui =  request.POST['dui']
			
			empleadoContrato.nit= request.POST['nit']
			empleadoContrato.isss = request.POST['isss']


		if formC.is_valid():
			empleadoContrato.save()
			contratoFinal.empleado	= empleadoContrato
			contratoFinal.descripcion	= request.POST['descripcion']
			contratoFinal.periodoContrato	= request.POST['periodoContrato']
			
			contratoFinal.save()
			return redirect('constructora:empleado')
		
	else:
		form = EmpleadoForm()
		formC = ContratoForm()
	contexto={'formEmpleado':form,'formContrato':formC}
	return render(request,'empleados/crearEmpleado.html', contexto)

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

def asignacionRecurso(request,id_p):
	empA= AsignacionPuestoProyecto.objects.filter(proyecto=id_p)
	maqA=AsignacionoEjemplar.objects.filter(idProyecto=id_p)
	herrA=AsignacionHerramienta.objects.filter(idProyecto=id_p)
	pues=Puesto.objects.all()
	recursos=Recurso.objects.all()
	emp=Empleado.objects.filter(disponible=True)
	herramientas=Herramienta.objects.all()

	if 'btnEmpleado' in request.POST:
		asignacionE=AsignacionPuestoProyecto()
		asignacionE.empleado=Empleado.objects.get(id=request.POST['selectEmpleado'])
		asignacionE.puesto=Puesto.objects.get(id=request.POST['selectPuesto'])
		asignacionE.proyecto=Proyecto.objects.get(id=id_p)
		asignacionE.salario=request.POST['inputSalario']
		asignacionE.save()
		pass
	
	if 'btnEjemplar' in request.POST:
		asignacionM=AsignacionoEjemplar()
		asignacionM.idProyecto=Proyecto.objects.get(id=id_p)
		asignacionM.ejemplar=Ejemplar.objects.get(codigoEjemplar=request.POST['selectEjemplar'])
		asignacionM.fechaAsignacion= time.strftime("%c")
		asignacionM.save()
		pass

	if 'btnHerramienta' in request.POST:
		asignacionH=AsignacionHerramienta()
		asignacionH.idProyecto=Proyecto.objects.get(id=id_p)
		asignacionH.Herramienta=Herramienta.objects.get(codigoHerramienta=request.POST['selectHerramienta'])
		asignacionH.fechaAsignacion=time.strftime("%c")
		asignacionH.cantidadAsignada=request.POST['inputCantidad']
		herramienta=Herramienta.objects.get(codigoHerramienta=request.POST['selectHerramienta'])
		cantidad=herramienta.canatidadDisponibles
		herramienta.canatidadDisponibles=int(cantidad)-int(asignacionH.cantidadAsignada)
		herramienta.save()
		asignacionH.save()


	contexto={'puestos':pues,'empleados':emp,'recursos':recursos,'herramientas':herramientas,'empA':empA,'maqA':maqA,'herrA':herrA}
	return render(request,'proyecto/AsignacionRecurso.html',contexto)




def eliminarRecurso(request,id_pro, id_p, tipo_rec):
	contexto={}
	if(tipo_rec=='1'):
		dato=AsignacionPuestoProyecto.objects.get(id=id_p)
		
		contexto={'dato':dato}
		if request.method=='POST':
			dato.delete()
			return redirect('http://127.0.0.1:8000/constructora/asignacionRecurso/'+id_pro+'/')
			pass

	if(tipo_rec=='2'):

		dato=AsignacionoEjemplar.objects.get(id=id_p)
		
		contexto={'dato':dato}
		if request.method=='POST':
			dato.delete()
			return redirect('http://127.0.0.1:8000/constructora/asignacionRecurso/'+id_pro+'/')
			pass

	if(tipo_rec=='3'):

		dato=AsignacionHerramienta.objects.get(id=id_p)
		
		contexto={'dato':dato}
		if request.method=='POST':
			dato.delete()
			return redirect('http://127.0.0.1:8000/constructora/asignacionRecurso/'+id_pro+'/')
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