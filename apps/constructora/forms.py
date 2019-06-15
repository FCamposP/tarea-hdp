from django import forms
from apps.constructora.models import Proyecto, Recurso, Ejemplar, Herramienta
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
        model = Materia

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
            'descripcionRecurso' : forms.Textarea(attrs={'rows':3, 'class':'form-control','placeholder':'Escriba la descripción del Recurso'}),
        }

class EjemplarForm(forms.ModelForm):

    class Meta:
        model = Materia

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
        model = Materia

        fields = [
            'codigoHerramienta'
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
            'cantidadHerramienta' : forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el numero de Herramientas'}),
            'descripcionEjemplar' : forms.Textarea(attrs={'rows':3, 'class':'form-control','placeholder':'Escriba la descripción de la Herramienta'}),
        }