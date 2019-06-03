from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from apps.proyecto.views import *
from django.contrib.auth.views import login

app_name="proyectos"
urlpatterns = [
    url(r'^busquedaProyecto/$',login_required(buscarProyecto.as_view()),name="busquedaProyecto"),

]
