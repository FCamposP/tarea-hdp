from django.shortcuts import render,redirect
import hashlib
from django.views.generic import TemplateView, ListView
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
	if 'buscar' in request.GET:		
		if request.GET['buscarInput'] != "":
			palabraClave = request.GET['buscarInput']
			
			if Recurso.objects.filter(codigoRecurso__contains = palabraClave).exists():
				recurso = Recurso.objects.filter(codigoRecurso__contains = palabraClave)
				contexto={'recursos':recurso}
				return render(request, 'recursos/listaRecurso2.html', contexto)
			else:
				if Recurso.objects.filter(nombreRecurso__contains = palabraClave).exists():
					recurso = Recurso.objects.filter(nombreRecurso__contains = palabraClave)
					contexto={'recursos':recurso}
					return render(request, 'recursos/listaRecurso2.html', contexto)
				else:
					if Recurso.objects.filter(tipoRecurso__contains = palabraClave).exists():
						recurso = Recurso.objects.filter(tipoRecurso__contains = palabraClave)
						contexto={'recursos':recurso}
						return render(request, 'recursos/listaRecurso2.html', contexto)
					else:
						if Recurso.objects.filter(descripcionRecurso__contains = palabraClave).exists():
							recurso = Recurso.objects.filter(descripcionRecurso__contains = palabraClave)
							contexto={'recursos':recurso}
							return render(request, 'recursos/listaRecurso2.html', contexto)
		pass
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
	if 'buscar' in request.GET:		
		if request.GET['buscarInput'] != "":
			palabraClave = request.GET['buscarInput']
			
			if Ejemplar.objects.filter(codigoEjemplar__contains = palabraClave, idRecurso=recurso).exists():
				ejemplar = Ejemplar.objects.filter(codigoEjemplar__contains = palabraClave, idRecurso=recurso)
				contexto={'recurso':recurso, 'ejemplares':ejemplar}
				return render(request, 'ejemplares/listaEjemplar.html', contexto)
			else:
				if Ejemplar.objects.filter(nombreEjemplar__contains = palabraClave, idRecurso=recurso).exists():
					ejemplar = Ejemplar.objects.filter(nombreEjemplar__contains = palabraClave, idRecurso=recurso)
					contexto={'recurso':recurso, 'ejemplares':ejemplar}
					return render(request, 'ejemplares/listaEjemplar.html', contexto)
				else:
					if Ejemplar.objects.filter(descripcionEjemplar__contains = palabraClave, idRecurso=recurso).exists():
						ejemplar = Ejemplar.objects.filter(descripcionEjemplar__contains = palabraClave, idRecurso=recurso)
						contexto={'recurso':recurso, 'ejemplares':ejemplar}
						return render(request, 'ejemplares/listaEjemplar.html', contexto)
		pass

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
	if 'buscar' in request.GET:		
		if request.GET['buscarInput'] != "":
			palabraClave = request.GET['buscarInput']
			
			if Herramienta.objects.filter(codigoHerramienta__contains = palabraClave).exists():
				herramienta = Herramienta.objects.filter(codigoHerramienta__contains = palabraClave)
				contexto={'herramientas':herramienta}
				return render(request, 'herramientas/listaHerramientas.html', contexto)
			else:
				if Herramienta.objects.filter(nombreHerramienta__contains = palabraClave).exists():
					herramienta = Herramienta.objects.filter(nombreHerramienta__contains = palabraClave)
					contexto={'herramientas':herramienta}
					return render(request, 'herramientas/listaHerramientas.html', contexto)
				else:
					if Herramienta.objects.filter(descripcionHerramienta__contains = palabraClave).exists():
						herramienta = Herramienta.objects.filter(descripcionHerramienta__contains = palabraClave)
						contexto={'herramientas':herramienta}
						return render(request, 'herramientas/listaHerramientas.html', contexto)
		pass

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
def verPuesto(request):
	puesto = Puesto.objects.all()
	contexto = {'puesto':puesto}
	if 'buscar' in request.GET:		
		if request.GET['buscarInput'] != "":
			palabraClave = request.GET['buscarInput']
			
			if Puesto.objects.filter(nombrePuesto__contains = palabraClave).exists():
				puesto = Puesto.objects.filter(nombrePuesto__contains = palabraClave)
				contexto = {'puesto':puesto}
			else:
				if Puesto.objects.filter(descripcionPuesto__contains = palabraClave).exists():
					puesto = Puesto.objects.filter(descripcionPuesto__contains = palabraClave)
					contexto = {'puesto':puesto}
				
					

	else:
		puesto= Puesto.objects.all()
		contexto = {'puesto':puesto}



	

	
	

	return render(request,'Puestos/puesto.html' ,contexto)

def crearPuesto(request):
	puesto = Puesto()
	puestos = Puesto.objects.all()
	codigo = ""
	if puestos:
		for c in puestos:
			codigo =  (c.id) + 1 
		codigo = "P" + str(codigo)
	else:
		codigo = "P" + str(1)
	if request.method=='POST':
		form = puestoForm(request.POST)
		if form.is_valid():
			puesto.codigoPuesto = codigo
			puesto.nombrePuesto = request.POST['nombrePuesto']
			puesto.descripcionPuesto = request.POST['descripcionPuesto']
			
			puesto.save()
			return redirect('constructora:verPuesto')
		
		
	else:
		form = puestoForm()
		
	contexto={'form':form}
	return render(request,'Puestos/crearPuesto.html', contexto)

def eliminarPuesto(request, id_puesto):
	puesto = Puesto.objects.get(id=id_puesto)
	if request.method == 'POST':
		puesto.delete()
		return redirect('http://127.0.0.1:8000/constructora/verPuesto/')
	contexto= {'puesto' : puesto}
	return render(request, 'Puestos/eliminarPuesto.html',contexto )

def editarPuesto(request, id_puesto):
	puesto = Puesto.objects.get(id = id_puesto)

	if request.method == 'GET':
		form = puestoForm(instance=puesto)
		
	else:
		
		form = puestoForm(request.POST, instance= puesto)
		
		
		if form.is_valid():
			form.save()
			
			
		return redirect('http://127.0.0.1:8000/constructora/verPuesto/')
	contexto={'form':form}
	return render(request ,'Puestos/editarPuesto.html', contexto)

def verCliente(request):
	
	clientes = Cliente.objects.all()
	contexto = {'cliente':clientes}
	if 'buscar' in request.GET:		
		if request.GET['buscarInput'] != "":
			palabraClave = request.GET['buscarInput']
			
			if Cliente.objects.filter(nombreCliente__contains = palabraClave).exists():
				clientes = Cliente.objects.filter(nombreCliente__contains = palabraClave)
				contexto = {'cliente':clientes}
			else:
				if Cliente.objects.filter(direccion__contains = palabraClave).exists():
					clientes = Cliente.objects.filter(direccion__contains = palabraClave)
					contexto = {'cliente':clientes}
				
					

	else:
		clientes = Cliente.objects.all()
		contexto = {'cliente':clientes}







	

	
	

	return render(request,'clientes/clientes.html', contexto)

def nuevoCliente(request):
	cliente = Cliente()
	clientes = Cliente.objects.all()
	codigo = ""
	if clientes:
		for c in clientes:
			codigo =  (c.id) + 1 
		codigo = "CL" + str(codigo)
	else:
		codigo = "CL" + str(1)
	if request.method=='POST':
		form = clienteForm(request.POST)
		if form.is_valid():
			cliente.codigoCliente = codigo
			cliente.nombreCliente = request.POST['nombreCliente']
			cliente.direccion = request.POST['direccion']
			cliente.email = request.POST['email']
			cliente.nit = request.POST['nit']
			cliente.giro = request.POST['giro']
			cliente.numTelefono = request.POST['numTelefono']
			cliente.save()
			return redirect('constructora:verCliente')
		
		
	else:
		form = clienteForm()
		
	contexto={'form':form}
	return render(request,'clientes/crearCliente.html', contexto)

def eliminarEmpleado(request, id_empleado):
	empleado = Empleado.objects.get(id=id_empleado)
	if request.method == 'POST':
		empleado.delete()
		return redirect('http://127.0.0.1:8000/constructora/empleado/')
	contexto= {'empleado' : empleado}
	return render(request, 'empleados/eliminarEmpleado.html',contexto )
	
def eliminarCliente(request, id_cliente):
	cliente = Cliente.objects.get(id=id_cliente)
	if request.method == 'POST':
		cliente.delete()
		return redirect('http://127.0.0.1:8000/constructora/verCliente/')
	contexto= {'cliente' : cliente}
	return render(request, 'clientes/eliminarCliente.html',contexto )

def verContrato(request):
	contrato = Contrato.objects.all()
	empleado = Empleado.objects.all()
	contexto = {'contrato':contrato, 'empleado':empleado}

	if 'buscar' in request.GET:		
		if request.GET['buscarInput'] != "":
			palabraClave = request.GET['buscarInput']
			
			if Contrato.objects.filter(descripcion__contains = palabraClave).exists():
				contrato = Contrato.objects.filter(descripcion__contains = palabraClave)
				empleado = Empleado.objects.all()
				contexto={'empleado':empleado,'contrato':contrato}
			else:
				if Contrato.objects.filter(periodoContrato__contains = palabraClave).exists():
					contrato = Contrato.objects.filter(periodoContrato__contains = palabraClave)
					empleado = Empleado.objects.all()
					contexto={'empleado':empleado,'contrato':contrato}
				else:
					if Contrato.objects.filter(fechaContratacion__contains = palabraClave).exists():
						contrato = Contrato.objects.filter(fechaContratacion__contains = palabraClave)
						empleado = Empleado.objects.all()
						contexto={'empleado':empleado,'contrato':contrato}

					

	else:
		empleado = Empleado.objects.all()
		contrato = Contrato.objects.all()
		contexto={'empleado':empleado,'contrato':contrato}
	return render(request,'empleados/contrato.html', contexto)

def verEmpleado(request):
	empleados = Empleado.objects.all()
	contexto={'empleados':empleados}
	if 'buscar' in request.GET:		
		if request.GET['buscarInput'] != "":
			palabraClave = request.GET['buscarInput']
			
			if Empleado.objects.filter(nombres__contains = palabraClave).exists():
				empleados = Empleado.objects.filter(nombres__contains = palabraClave)
				contexto={'empleados':empleados}
			else:
				if Empleado.objects.filter(apellidos__contains = palabraClave).exists():
					empleados = Empleado.objects.filter(apellidos__contains = palabraClave)
					contexto={'empleados':empleados}
				else:
					if Empleado.objects.filter(direccion__contains = palabraClave).exists():
						empleados = Empleado.objects.filter(direccion__contains = palabraClave)
						contexto={'empleados':empleados}
					

	else:
		empleados=Empleado.objects.all()
		contexto={'empleados':empleados}
		

	
	return render(request,'empleados/empleado.html',contexto)

def editarEmpleado(request, id_empleado):
	empleado = Empleado.objects.get(id = id_empleado)

	if request.method == 'GET':
		form = EmpleadoForm(instance=empleado)
		
	else:
		
		form = EmpleadoForm(request.POST, instance= empleado)
		
		
		if form.is_valid():
			form.save()
			
			
		return redirect('http://127.0.0.1:8000/constructora/empleado/')
	contexto={'formEmpleado':form}
	return render(request ,'empleados/editarEmpleado.html', contexto)

def editarCliente(request, id_cliente):
	cliente = Cliente.objects.get(id = id_cliente)

	if request.method == 'GET':
		form = clienteForm(instance=cliente)
		
	else:
		
		form = clienteForm(request.POST, instance= cliente)
		
		
		if form.is_valid():
			form.save()
			
			
		return redirect('http://127.0.0.1:8000/constructora/verCliente/')
	contexto={'form':form}
	return render(request ,'clientes/editarCliente.html', contexto)

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
def DatosProy(request):

	usuario = request.user.id
	Asig= ""
	Asig2= ""
	

	if AsignacionUsuario.objects.filter(usuario = usuario).exists():
		Asig = AsignacionUsuario.objects.get(usuario = usuario)
		Asig2 = Proyecto.objects.get(id = Asig.empleado_proyecto.proyecto_id)
		

	contexto = {'Asig2': Asig2}
	return render(request, 'proyecto/verProyecto.html', contexto)

def listarEmpleadosProyecto(request):

	# lineas para capturar el proyecto al que pertenece el usuario activo
	usuario = request.user.id
	Asig = AsignacionUsuario.objects.get(usuario = usuario)
	Asig2 = AsignacionPuestoProyecto.objects.get(id = Asig.empleado_proyecto.proyecto_id)
	proyecto = Asig2.proyecto
	# fin
	# extraccion de empleados
	empleados = AsignacionPuestoProyecto.objects.filter(proyecto_id = proyecto)
	contexto = {'empleados': empleados}
	return render(request,'proyecto/recursosEmpleado.html', contexto)

def activo(request,id_asignacionPuestoProyecto):
	asig = AsignacionPuestoProyecto.objects.get(id = id_asignacionPuestoProyecto)
	if request.method == 'POST':
		if asig.activo == True:
			asig.activo = False
			asig.save()
		else:
			asig.activo = True
			asig.save()				
		return redirect('http://127.0.0.1:8000/constructora/recursosEmpleado/')
	contexto = {'asig': asig}	
	return render(request, 'proyecto/CambioActivo.html',contexto)

def activo1(request,id_ejemplar):
	asig = AsignacionoEjemplar.objects.get(id = id_ejemplar)
	if request.method == 'POST':
		if asig.activo == True:
			asig.activo = False
			asig.save()
		else:
			asig.activo = True
			asig.save()				
		return redirect('http://127.0.0.1:8000/constructora/RecursosProyecto/')
	contexto = {'asig': asig}	
	return render(request, 'proyecto/CambioActivo.html',contexto)	

def activo2(request,id_herramienta):
	asig = AsignacionHerramienta.objects.get(id = id_herramienta)
	if request.method == 'POST':
		if asig.activo == True:
			asig.activo = False
			asig.save()
		else:
			asig.activo = True
			asig.save()				
		return redirect('http://127.0.0.1:8000/constructora/RecursosProyecto/')
	contexto = {'asig': asig}	
	return render(request, 'proyecto/CambioActivo.html',contexto)		


def listaRecursos(request):	
	
	# lineas para capturar el proyecto al que pertenece el usuario activo
	usuario = request.user.id
	Asig = AsignacionUsuario.objects.get(usuario = usuario)
	Asig2 = AsignacionPuestoProyecto.objects.get(id = Asig.empleado_proyecto.proyecto_id)
	proyecto = Asig2.proyecto
	example = AsignacionoEjemplar.objects.filter(idProyecto_id = proyecto)
	herra = AsignacionHerramienta.objects.filter(idProyecto_id= proyecto)
	contexto = {'ejemplar': example, 'tools': herra}
	return render(request, 'proyecto/RecursosProyecto.html', contexto)

def mostrarAsistencia(request):
	# lineas para capturar el proyecto al que pertenece el usuario activo
	usuario = request.user.id
	Asig = AsignacionUsuario.objects.get(usuario = usuario)
	Asig2 = AsignacionPuestoProyecto.objects.get(id = Asig.empleado_proyecto.proyecto_id)
	proyecto = Asig2.proyecto
	# fin 
	# extraccion de empleados	
	asistencia = Asistencia.objects.all()
	contexto = {'asistencias': asistencia}
	return render(request, 'proyecto/Asistencia.html' ,contexto)	

def registroAsistencia(request, id_asistencia):
	# lineas para capturar el proyecto al que pertenece el usuario activo
	usuario = request.user.id
	Asig = AsignacionUsuario.objects.get(usuario = usuario)
	Asig2 = AsignacionPuestoProyecto.objects.get(id = Asig.empleado_proyecto.proyecto_id)
	proyecto = Asig2.proyecto
	# fin 
	empleados = AsignacionPuestoProyecto.objects.filter(proyecto_id = proyecto)
	asig = AsignacionPuestoProyecto.objects.get(id = id_asistencia)
	if Asistencia.objects.filter(id= asig.id).exists():
		asig= None
	else:
		asistencia = Asistencia()
		asistencia.Asignacion_id = asig.id
		asistencia.fechaAsistencia = "2019-06-24"
		asistencia.asistencia = True
		asistencia.save()
		if request.method == 'POST':			
			return redirect('http://127.0.0.1:8000/constructora/recursosEmpleado/')

	contexto = { 'empleados': empleados}
	return render(request, 'proyecto/recursosEmpleado.html', contexto)

	
	
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
	if 'buscar' in request.GET:		
		if request.GET['buscarInput'] != "":
			palabraClave = request.GET['buscarInput']
			if	Proyecto.objects.filter(codigoProyecto__contains=palabraClave).exists():
				proyecto=Proyecto.objects.filter(codigoProyecto__contains=palabraClave)
				contexto={'proyectos':proyecto}
			else:
				if	Proyecto.objects.filter(nombreProyecto__contains=palabraClave).exists():
					proyecto=Proyecto.objects.filter(nombreProyecto__contains=palabraClave)
					contexto={'proyectos':proyecto}
				else:
					if	Proyecto.objects.filter(descripcionProyecto__contains=palabraClave).exists():
						proyecto=Proyecto.objects.filter(descripcionProyecto__contains=palabraClave)
						contexto={'proyectos':proyecto}
					else:
						if	Proyecto.objects.filter(ubicacion__contains=palabraClave).exists():
							proyecto=Proyecto.objects.filter(ubicacion__contains=palabraClave)
							contexto={'proyectos':proyecto}

	return render(request,'proyecto/BuscarProyecto.html',contexto)

def asignacionRecurso(request,id_p):#se necesita id del proyecto para asignar y recuperar asignados
	#asignaciones ya realizadas al proyecto
	empA= AsignacionPuestoProyecto.objects.filter(proyecto=id_p)
	maqA=AsignacionoEjemplar.objects.filter(idProyecto=id_p)
	herrA=AsignacionHerramienta.objects.filter(idProyecto=id_p)
	#objetos para asignar
	pues=Puesto.objects.all()
	recursos=Recurso.objects.all() 
	emp=Empleado.objects.filter(disponible=True)
	herramientas=Herramienta.objects.all()
	cantidadMenor=False
	nuevoUser=''
	nuevaContra=''
	esEncargado=False

	if 'btnEmpleado' in request.POST:
		asignacionE=AsignacionPuestoProyecto()
		empleado=Empleado.objects.get(id=request.POST['selectEmpleado'])
		asignacionE.empleado=empleado 

		asignacionE.puesto=Puesto.objects.get(id=request.POST['selectPuesto'])
		asignacionE.proyecto=Proyecto.objects.get(id=id_p)
		asignacionE.salario=request.POST['inputSalario']
		asignacionE.save()
		if asignacionE.puesto.nombrePuesto=="Encargado":
			proy=Proyecto.objects.get(id=id_p)
			asigUsuario=AsignacionUsuario()
			usuario= User.objects.create_user("Encargado"+proy.codigoProyecto, 'myemail@crazymail.com', proy.codigoProyecto)
			usuario.save()
			asigUsuario.usuario=usuario
			asigUsuario.empleado_proyecto=asignacionE
			asigUsuario.tipo_usuario="Encargado"
			asigUsuario.descripcion="Es el responsable de la gestion del proyecto a su cargo"
			asigUsuario.save()
			nuevoUser=usuario.username
			nuevaContra=proy.codigoProyecto
			esEncargado=True
			for x in pues:
				if x.nombrePuesto=='Encargado':
					print(x.nombrePuesto)
					x.delete()
			pues.save()
		else:
			pues=Puesto.objects.all()

				


		pass
		empleado.disponible=False
		empleado.save()
	if 'btnEjemplar' in request.POST:
		asignacionM=AsignacionoEjemplar()
		asignacionM.idProyecto=Proyecto.objects.get(id=id_p)
		ejemplar=Ejemplar.objects.get(codigoEjemplar=request.POST['selectEjemplar'])
		asignacionM.ejemplar=ejemplar
		ejemplar.disponible=False
		asignacionM.fechaAsignacion= time.strftime("%c")
		asignacionM.save()
		pass

	if 'btnHerramienta' in request.POST:
		cantidad=request.POST['inputCantidad']
		herramienta=Herramienta.objects.get(codigoHerramienta=request.POST['selectHerramienta'])
		cantidadDis=herramienta.canatidadDisponibles
		if int(cantidad)<cantidadDis:
			asignacionH=AsignacionHerramienta()
			asignacionH.idProyecto=Proyecto.objects.get(id=id_p)
			asignacionH.Herramienta=Herramienta.objects.get(codigoHerramienta=request.POST['selectHerramienta'])
			asignacionH.fechaAsignacion=time.strftime("%c")
			asignacionH.cantidadAsignada=cantidad

			herramienta.canatidadDisponibles=int(cantidadDis)-int(asignacionH.cantidadAsignada)
			herramienta.save()
			asignacionH.save()
		else:
			cantidadMenor=True
		#eliminar empleado 
	if 'accionE' in request.POST:
		accion = request.POST['accionE']
		id_asignacion = request.POST['elimEmpleado']
		dato=AsignacionPuestoProyecto.objects.get(id=id_asignacion)
		if accion == 'Eliminar':	
			dato.delete()
			pass
		else:
			pass
		pass
		#eliminar recurso
	if 'accionR' in request.POST:
		accion = request.POST['accionR']
		id_asignacion = request.POST['elimRec']
		dato=AsignacionoEjemplar.objects.get(id=id_asignacion)
		if accion == 'Eliminar':	
			dato.delete()
			pass
		else:
			pass
		pass

	if 'accionH' in request.POST:
		accion = request.POST['accionH']
		id_asignacion = request.POST['elimHerr']

		dato=AsignacionHerramienta.objects.get(id=id_asignacion)
		if accion == 'Eliminar':	
			dato.delete()
			pass
		else:
			pass
		pass
	contexto={'esEncargado':esEncargado,'nuevaContra':nuevaContra,'nuevoUser':nuevoUser, 'esMenor':cantidadMenor, 'puestos':pues,'empleados':emp,'recursos':recursos,'herramientas':herramientas,'empA':empA,'maqA':maqA,'herrA':herrA}
	return render(request,'proyecto/AsignacionRecurso.html',contexto)




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

def solicitarRecursos(request): 
	usuario=request.user
	encontrado=True
	try:
		solicitante=AsignacionUsuario.objects.get(usuario=usuario).empleado_proyecto
	except AsignacionUsuario.DoesNotExist:
		solicitante=None
		encontrado=False
	print(solicitante)
	asigPuesPro=AsignacionPuestoProyecto.objects.get(id=solicitante.id)
	proyecto=Proyecto.objects.get(id=asigPuesPro.proyecto.id)
	contexto={'j':'k','proyecto':proyecto}
	puestos =Puesto.objects.all()
	recursos=Recurso.objects.all()
	herramientas=Herramienta.objects.all()

	if 'btnSolicitar' in request.POST:
		soli=Solicitud()
		soli.solicitante=solicitante
		soli.fechaSolicitud=time.strftime("%c")
		soli.save()
		for x in puestos:
			if str(x.codigoPuesto) in request.POST:
				detalle=DetalleSolicitud()
				detalle.solicitud=Solicitud.objects.latest('id')
				detalle.tiporecurso='Puesto'
				detalle.recurso=str(x.nombrePuesto)
				detalle.cantidad=request.POST[x.codigoPuesto]
				detalle.save()
		for x in recursos:
			if str(x.codigoRecurso) in request.POST:
		
				detalle=DetalleSolicitud()
				detalle.solicitud=Solicitud.objects.latest('id')
				detalle.tiporecurso='Maquinaria'
				detalle.recurso=str(x.nombreRecurso)
				detalle.cantidad=request.POST[x.codigoRecurso]
				detalle.save()
		for x in herramientas:
			if str(x.codigoHerramienta) in request.POST:
				detalle=DetalleSolicitud()
				detalle.solicitud=Solicitud.objects.latest('id')
				detalle.tiporecurso='Herramienta'
				detalle.recurso=str(x.nombreHerramienta)
				detalle.cantidad=request.POST[x.codigoHerramienta]
				detalle.save()
		return redirect('constructora:recursosProyecto')
		# verificar para puestos
		

	return render(request,'proyecto/SolicitarRecursos.html',contexto)

class verProyecto(TemplateView):
	template_name='proyecto/VerProyecto.html'

def ConseguirTipoRecurso(request): #funcion para recuperar datos en solicitar recursos
	opcion= request.GET['opcion']

	if opcion=='1':
		puestos=Puesto.objects.all()
		data=serializers.serialize('json',puestos)
	if opcion=='2':
		recursos=Recurso.objects.all()
		data=serializers.serialize('json',recursos)
	if opcion=='3':
		herramientas=Herramienta.objects.all()
		data=serializers.serialize('json',herramientas)


	return HttpResponse(data,content_type='application/json')

def conseguirElemento(request):
	opcion= request.GET['opcion']
	elemento=request.GET['elemento']

	if opcion=='1':
		puesto=Puesto.objects.get(id=elemento)
	
		data=serializers.serialize('json',[puesto])


	if opcion=='2':
		recurso=Recurso.objects.get(codigoRecurso=elemento)
		data=serializers.serialize('json',[recurso])
		print(data)

	if opcion=='3':
		herramienta=Herramienta.objects.get(codigoHerramienta=elemento)
		data=serializers.serialize('json',[herramienta])

	return HttpResponse(data,content_type='application/json')


def aprobarSolicitud(request): 
	aprobados=[]
	solicitudes=Solicitud.objects.filter(aprobado=False)
	verificacion=False
	for x in solicitudes:
		detalleSoli=DetalleSolicitud.objects.filter(solicitud=x,asignado=False)
		if detalleSoli.count()>0:
			aprobados.append(x)
	
	contexto={'solicitudes':aprobados}
	return render(request,'proyecto/AprobarSolicitud.html',contexto)

def verDetalleSolicitud(request,id_p):
	soli=Solicitud.objects.get(id=id_p)
	proyecto=Proyecto.objects.get(id=soli.solicitante.proyecto.id)
	empleados=Empleado.objects.filter(disponible=True)
	ejemplares=list(Ejemplar.objects.filter(disponible=True))
	herramientasDisponibles=[]
	herramientasTodas=Herramienta.objects.all()
	for h in herramientasTodas:
		if(h.canatidadDisponibles>0):
			herramientasDisponibles.append(h)

	puestos=DetalleSolicitud.objects.filter(solicitud=id_p,tiporecurso='Puesto',asignado=False)
	maquinas=DetalleSolicitud.objects.filter(solicitud=id_p,tiporecurso='Maquinaria',asignado=False)
	herramientas=DetalleSolicitud.objects.filter(solicitud=id_p,tiporecurso='Herramienta',asignado=False)
	contexto={'puestos':puestos,'maquinas':maquinas,'herramientas':herramientas,'proyecto':proyecto,'empleados':empleados,'ejemplares':ejemplares,'herramientasD':herramientasDisponibles}

	if 'btnEmpleado' in request.POST:
		asignacionP=AsignacionPuestoProyecto()
		detalleSoli=DetalleSolicitud.objects.get(id=request.POST['recurso'])
		
		puest=Puesto.objects.get(nombrePuesto=str(detalleSoli.recurso))
		empleado=Empleado.objects.get(id=request.POST['selectEmpleado1'])
		asignacionP.empleado=empleado
		empleado.disponible=False
		empleado.save()
		asignacionP.puesto=puest
		asignacionP.proyecto=proyecto
		asignacionP.salario=request.POST['inputSalario']
		asignacionP.save()
		detalleSoli.cantidad=detalleSoli.cantidad-1
		detalleSoli.save()
		
		if detalleSoli.cantidad==0:
			detalleSoli.asignado=True
			detalleSoli.save()

	if 'btnEjemplar' in request.POST:
		detalleSoli=DetalleSolicitud.objects.get(id=request.POST['maquinaE'])

		asignacionE=AsignacionoEjemplar()
		asignacionE.idProyecto=proyecto
		asignacionE.fechaAsignacion=time.strftime("%c")
		asignacionE.ejemplar=Ejemplar.objects.get(codigoEjemplar=request.POST['selectEjemplar1'])
		asignacionE.save()
		detalleSoli.cantidad=detalleSoli.cantidad-1
		detalleSoli.save()
		
		if detalleSoli.cantidad==0:
			detalleSoli.asignado=True
			detalleSoli.save()

	if 'btnHerramientaR' in request.POST:
		cantidad=int(request.POST['inputCantidad'])
		if cantidad>0:
			detalleSoli=DetalleSolicitud.objects.get(id=request.POST['herrRe'])
			herramienta=Herramienta.objects.get(nombreHerramienta=str(detalleSoli.recurso))
			if cantidad < herramienta.canatidadDisponibles:
				asignacionHerr=AsignacionHerramienta()
				asignacionHerr.idProyecto=proyecto
				asignacionHerr.Herramienta=herramienta
				asignacionHerr.cantidadAsignada=cantidad
				herramienta.canatidadDisponibles-=cantidad
				herramienta.fechaAsignacion=time.strftime("%c")
				asignacionHerr.save()
				detalleSoli.cantidad=detalleSoli.cantidad-cantidad
				detalleSoli.save()
				
				if detalleSoli.cantidad==0:
					detalleSoli.asignado=True
					detalleSoli.save()

	return render(request,'proyecto/DetalleSolicitud.html',contexto)

def ReasignarEjemplar(request):
	
	detalleSoli=DetalleSolicitud.objects.get(id=request.GET['id_re'])
	recurso=Recurso.objects.get(nombreRecurso=str(detalleSoli.recurso))

	ejemplares=Ejemplar.objects.filter(idRecurso=recurso.codigoRecurso,disponible=True,)
	
	data=serializers.serialize('json',ejemplares)
	print(data)
	return HttpResponse(data,content_type='application/json')
	
#FIN VISTAS FC