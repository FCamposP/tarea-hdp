from django.contrib import admin

from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from apps.constuctora.views import *


urlpatterns = [
    url(r'^index/$',login_required(Vista.as_view()),name="index"),


]
