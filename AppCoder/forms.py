from django import forms

class FormularioProfesor(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    profesion = forms.CharField()    

class FormularioEstudiante(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()

class FormularioCurso(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()

class FormularioEntregable(forms.Form):
    nombre = forms.CharField()
    fechaDeEntrega = forms.DateField()
