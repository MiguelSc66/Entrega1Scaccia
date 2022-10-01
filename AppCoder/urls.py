from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("formuProfe/", formuProfe, name="formuProfes"),
    path("formuEs/", formuEstudiate, name="formuEstudiante"),
    path("formuEn/", formuEntregable, name="formuEntregable"),
    path("resultados/", buscar, name="resultado"),
    path("buscadorProfes", buscadorProfes, name="buscadorProfes"),
    ]



""""path("estudiantes/", estudiantes, name="Estudiantes"),
    path("profesores/", profesores, name="Profesores"),
    path("entregables/", entregables, name="Entregables"),
    path("curso/", curso1, name="Cursos"),"""