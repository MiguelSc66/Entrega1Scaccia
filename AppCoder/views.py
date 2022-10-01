from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,  Context
from AppCoder.models import *
from AppCoder.forms import *



def inicio(request): 

	return render(request, "AppCoder/inicio.html")
"""""
def estudiantes(request):
	
	return render(request, "ProyectoCoder/estudiantes.html")

def profesores(request): 
	
	return render(request, "ProyectoCoder/profesores.html")

def entregables(request):
	
	ente1 = entregables(nombre="examen 1", fechaDeEntrega="2022-03-30")
	ente1.save()
	
	return render(request, "ProyectoCoder/entregables.html")


def curso1(request):
	return render(request, "ProyectoCoder/curso.html")
"""
def formuProfe(request):
	if request.method=="POST":
		formulario1 = FormularioProfesor(request.POST)
		if formulario1.is_valid(): #manera de ver si tenemos errores
			
			info = formulario1.cleaned_data
			
			ProfesorF = profesor(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"], profesion=info["profesion"])

			ProfesorF.save() #se realiza el gaurdado en la base de datos

			return render(request, "AppCoder/inicio.html") #nos vuelve a mostrar la pagina del formulario vacio o la podemos redireccionar a otra parte de la pagina
	
	else:
		formulario1 = FormularioProfesor() # mustra el formulario vacio
	
	return render(request, "AppCoder/formuP.html", {"form1":formulario1})

def formuEstudiate(request):
	if request.method=="POST":
		formulario2 = FormularioEstudiante(request.POST)
		if formulario2.is_valid(): #manera de ver si tenemos errores
			
			info = formulario2.cleaned_data
			
			estudianteF = estudiantes1(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"])

			estudianteF.save() #se realiza el gaurdado en la base de datos

			return render(request, "AppCoder/inicio.html") #nos vuelve a mostrar la pagina del formulario vacio o la podemos redireccionar a otra parte de la pagina
	
	else:
		formulario2 = FormularioEstudiante() # mustra el formulario vacio
	
	return render(request, "AppCoder/formuEs.html", {"form2":formulario2})

def formuEntregable(request):
	if request.method=="POST":
		formulario3 = FormularioEntregable(request.POST)
		if formulario3.is_valid(): #manera de ver si tenemos errores
			
			info = formulario3.cleaned_data
			
			entregableF = entregable(nombre=info["nombre"], fechaDeEntrega=info["fechaDeEntrega"])

			entregableF.save() #se realiza el gaurdado en la base de datos

			return render(request, "AppCoder/inicio.html") #nos vuelve a mostrar la pagina del formulario vacio o la podemos redireccionar a otra parte de la pagina
	
	else:
		formulario3 = FormularioEntregable() # mustra el formulario vacio
	
	return render(request, "AppCoder/formuEn.html", {"form3":formulario3})

def buscadorProfes(request):
	
	return render(request, "AppCoder/buscadorProfe.html")

def buscar(request):
	if request.GET["nombre"]:
		nombre = request.GET["nombre"]
		profe = profesor.objects.filter(nombre__icontains=nombre)

		return render(request, "AppCoder/resultados.html", {"profes":profe, "nombre":nombre})
	else:
		mensaje = "No enviste los datos"
	return HttpResponse(mensaje)

