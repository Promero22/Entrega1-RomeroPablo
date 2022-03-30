from django import forms

class ProfesionalFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class EspecialidadFormulario(forms.Form):
    nombre = forms.CharField()
    numero = forms.IntegerField()

class SucursalFormulario(forms.Form):
    localidad= forms.CharField(max_length=30)
    direccion= forms.CharField(max_length=30)
    telefono= forms.CharField(max_length=30)
    email= forms.EmailField()