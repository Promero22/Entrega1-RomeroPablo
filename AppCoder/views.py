from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

from AppCoder.models import Profesional, Sucursal, Especialidad
from AppCoder.forms import  ProfesionalFormulario, SucursalFormulario, EspecialidadFormulario


# Create your views here.

def inicio(request):

    return render(request, "AppCoder/inicio.html")

def SucursalFormulario(request):

      if request.method == "POST":

            miFormulario = SucursalFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  sucursal = Sucursal(localidad=informacion["localidad"], direccion=informacion["direccion"], telefono=informacion["telefono"], email=informacion["email"])
                  sucursal.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = SucursalFormulario()

      return render(request, "AppCoder/sucursalFormulario.html", {"miFormulario": miFormulario})

def ProfesionalFormulario(request):

      if request.method == "POST":

            miFormulario = ProfesionalFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  profesional = Profesional(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
                  profesional.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = ProfesionalFormulario()

      return render(request, "AppCoder/profesionalFormulario.html", {"miFormulario": miFormulario})

def EspecialidadFormulario(request):

      if request.method == "POST":

            miFormulario = EspecialidadFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  especialidad = Especialidad(nombre=informacion["nombre"], numero=informacion["numero"])
                  especialidad.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = EspecialidadFormulario()

      return render(request, "AppCoder/especialidadFormulario.html", {"miFormulario": miFormulario})
 

from django.views.generic import ListView

class SucursalList(ListView):

    model = Sucursal
    template_name = "AppCoder/sucursal_list.html"

class ProfesionalList(ListView):

    model = Profesional
    template_name = "AppCoder/profesional_list.html"

class EspecialidadList(ListView):

    model = Especialidad
    template_name = "AppCoder/especialidad_list.html"

from django.views.generic.detail import DetailView

class SucursalDetalle(DetailView):

    model = Sucursal
    template_name = "AppCoder/sucursal_detalle.html"

class ProfesionalDetalle(DetailView):

    model = Profesional
    template_name = "AppCoder/profesional_detalle.html"

class EspecialidadDetalle(DetailView):

    model = Especialidad
    template_name = "AppCoder/especialidad_detalle.html"

from django.views.generic.edit import CreateView

class SucursalCreacion(CreateView):

    model = Sucursal
    success_url = "/AppCoder/sucursal/list"
    fields = ['localidad', 'direccion', 'telefono', 'email']

class ProfesionalCreacion(CreateView):

    model = Profesional
    success_url = "/AppCoder/profesional/list"
    fields = ['nombre', 'apellido', 'email', 'profesion']

class EspecialidadCreacion(CreateView):

    model = Especialidad
    success_url = "/AppCoder/especialidad/list"
    fields = ['nombre', 'numero']

from django.urls import reverse_lazy

from django.views.generic.edit import UpdateView

class SucursalUpdate(UpdateView):

    model = Sucursal
    success_url = "/AppCoder/sucursal/list"
    fields = ['localidad', 'direccion', 'telefono', 'email']

class ProfesionalUpdate(UpdateView):

    model = Profesional
    success_url = "/AppCoder/profesional/list"
    fields = ['nombre', 'apellido', 'email', 'profesion']    

class EspecialidadUpdate(UpdateView):

    model = Especialidad
    success_url = "/AppCoder/especialidad/list"
    fields = ['nombre', 'numero']  

from django.views.generic.edit import DeleteView

class SucursalDelete(DeleteView):

    model = Sucursal
    success_url = "/AppCoder/sucursal/list"

class ProfesionalDelete(DeleteView):

    model = Profesional
    success_url = "/AppCoder/profesional/list"

class EspecialidadDelete(DeleteView):

    model = Especialidad
    success_url = "/AppCoder/especialidad/list"

#Funciones para busquedas
def busquedaEspecialidad(request):
      return render(request, "AppCoder/busquedaEspecialidad.html")

def buscar(request):

    
    if request.GET["numero"]:

        numero = request.GET["numero"]
        especialidades= Especialidad.objects.filter(numero__icontains=numero)

        return render(request, "AppCoder/resultadosPorBusqueda.html", {"especialidades":especialidades, "numero":numero})
    else:

        respuesta= "No enviaste datos"

    #No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)

