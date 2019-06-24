from django import forms
from apps.constructora.models import *
import datetime

def validarFecha(date):
	if date.month<=9:
		fecha=str(date.year)+"-0"+str(date.month)+"-"+str(date.day)
	else:
		fecha=str(date.year)+"-"+str(date.month)+"-"+str(date.day)
	return fecha


fecha=validarFecha(datetime.datetime.now())
class ProyectoForm(forms.ModelForm):
    class Meta:
        model=Proyecto
        fields=[
            'idCliente',
            'nombreProyecto',
            'descripcionProyecto',
            'ubicacion',
            'fechaInicioConstruccion',
        ]
        labels={
            'idCliente':'Elija un Cliente',
            'nombreProyecto':'Nombre del Proyecto',
            'descripcionProyecto':'Descripción',
            'ubicacion':'Dirección',
            'fechaInicioConstruccion':'Fecha que iniciará',            
        }
        widgets={
            'idCliente':forms.Select(attrs={'class':'form-control'}),
            'nombreProyecto':forms.TextInput(attrs={'class':'form-control'}),
            'descripcionProyecto':forms.Textarea(attrs={'class':'form-control','rows':2}),
            'ubicacion':forms.Textarea(attrs={'class':'form-control','rows':2}),
            'fechaInicioConstruccion': forms.TextInput(attrs={'class':'form-control','type':'date', 'min':fecha}),            
        }

class RecursoForm(forms.ModelForm):

    class Meta:
        model = Recurso

        fields = [
            'codigoRecurso',
            'nombreRecurso',
            'tipoRecurso',
            'descripcionRecurso',

        ]
        labels = {
            'codigoRecurso' : 'Código',
            'nombreRecurso' : 'Nombre',
            'tipoRecurso' : 'Tipo de Recurso',
            'descripcionRecurso': 'Descripcion',
        }

        widgets = {
            'codigoRecurso' : forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el Código del Recurso'}),
            'nombreRecurso' : forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el Nombre del Recurso'}),
            'tipoRecurso' : forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el Tipo de Recurso'}),
            'descripcionRecurso' : forms.Textarea(attrs={'rows':5, 'class':'form-control','placeholder':'Escriba la descripción del Recurso'}),
        }

class RecursoForm_2(forms.ModelForm):

    class Meta:
        model = Recurso

        fields = [
            'codigoRecurso',
            'nombreRecurso',
            'tipoRecurso',
            'descripcionRecurso',

        ]
        labels = {
            'codigoRecurso' : 'Código',
            'nombreRecurso' : 'Nombre',
            'tipoRecurso' : 'Tipo de Recurso',
            'descripcionRecurso': 'Descripcion',
        }

        widgets = {
            'codigoRecurso' : forms.TextInput(attrs={'class':'form-control','readonly':'readonly','placeholder':'Escriba el Código del Recurso'}),
            'nombreRecurso' : forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el Nombre del Recurso'}),
            'tipoRecurso' : forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el Tipo de Recurso'}),
            'descripcionRecurso' : forms.Textarea(attrs={'rows':5, 'class':'form-control','placeholder':'Escriba la descripción del Recurso'}),
        }

class EjemplarForm(forms.ModelForm):

    class Meta:
        model = Ejemplar

        fields = [
            'codigoEjemplar',
            'nombreEjemplar',
            'descripcionEjemplar',

        ]
        labels = {
            'codigoEjemplar' : 'Código',
            'nombreEjemplar' : 'Nombre',
            'descripcionEjemplar': 'Descripcion',
        }

        widgets = {
            'codigoEjemplar' : forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el Código del Ejemplar'}),
            'nombreEjemplar' : forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el Nombre del Ejemplar'}),
            'descripcionEjemplar' : forms.Textarea(attrs={'rows':3, 'class':'form-control','placeholder':'Escriba la descripción del Ejemplar'}),
        }

class HerramientaForm(forms.ModelForm):

    class Meta:
        model = Herramienta

        fields = [
            'codigoHerramienta',
            'nombreHerramienta',
            'cantidadHerramienta',
            'descripcionHerramienta',

        ]
        labels = {
            'codigoHerramienta' : 'Código',
            'nombreHerramienta' : 'Nombre',
            'cantidadHerramienta' : 'Cantidad de herramientas',
            'descripcionHerramienta' : 'Descripcion',
        }

        widgets = {
            'codigoHerramienta' : forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el Código de la Herramienta'}),
            'nombreHerramienta' : forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el Nombre de la Herramienta'}),
            'cantidadHerramienta' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Escriba el numero de Herramientas','min':'0'}),
            'descripcionHerramienta' : forms.Textarea(attrs={'rows':3, 'class':'form-control','placeholder':'Escriba la descripción de la Herramienta'}),
        }


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=[
            'nombres',
            'apellidos',
            'direccion',
            'numTelefono',
            'dui',
            'nit',
            'isss',
        ]
        labels={
            'nombres':'Nombre: ',
            'apellidos':'Apellido: ',
            'direccion':'Direccion: ',
            'numTelefono':'Telefono: ',
            'dui':'Dui: ',            
            'nit':'Nit: ',
            'isss':'Isss: ',
        }
        widgets={
            'nombres':forms.TextInput(attrs={'class':'form-control'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'numTelefono':forms.TextInput(attrs={'class':'form-control'}),
            'dui':forms.TextInput(attrs={'class':'form-control'}),
            'nit':forms.TextInput(attrs={'class':'form-control'}),
            'isss':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class clienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=[
            
            'nombreCliente',
            'direccion',
            'email',
            'nit',
            'giro',
            'numTelefono',
        ]
        labels={

            
            'nombreCliente':'Nombre completo',
            'direccion':'Direccion',
            'email': 'Email',
            'nit': 'Nit',
            'giro': 'Giro',
            'numTelefono':'Telefono',

            
        }
        widgets={
            
            'nombreCliente':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'nit':forms.TextInput(attrs={'class':'form-control'}),
            'giro':forms.TextInput(attrs={'class':'form-control'}),
            'numTelefono':forms.TextInput(attrs={'class':'form-control'}),
            
        }


class ContratoForm(forms.ModelForm):
    class Meta:
        model=Contrato
        fields=[
            'descripcion',
            
            'periodoContrato',
            ]
      
        labels={
            'descripcion':'Descripción: ',
            
            'periodoContrato':'Periodo de contrato: ',
            
        }
        widgets={
            'descripcion':forms.Textarea(attrs={'class':'form-control','rows':2}),
            
            'periodoContrato':forms.TextInput(attrs={'class':'form-control'}),
            
        }