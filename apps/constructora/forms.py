from django import forms
from apps.constructora.models import Proyecto
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

