from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("" , views.home,name="home"), 
    path("agregar/",views.agregar,name="agregar"),
    pacth("eliminar/<int:tarea_id>/",views.eliminar,mane="elimnar"),

]