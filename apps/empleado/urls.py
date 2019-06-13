from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from apps.empleado.views import *
from django.contrib.auth.views import login

app_name="empleado"
urlpatterns = [
    url(r'^Empleado/$',login_required(Empleado),name="Empleado"),
    url(r'^NuevoEmpleado/$',login_required(crearEmpleado),name="NuevoEmpleado"),
   

]
