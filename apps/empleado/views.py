from django.shortcuts import render

# Create your views here.
def Empleado(request):
	
	return render(request,'empleados/empleado.html')

def crearEmpleado(request):
	
	return render(request,'empleados/crearEmpleado.html')