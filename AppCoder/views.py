from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

from AppCoder.models import Avatar, Profesional, Sucursal, Especialidad
from AppCoder.forms import  ProfesionalFormulario, SucursalFormulario, EspecialidadFormulario, UserRegisterForm, UserEditForm, AvatarFormulario


# Create your views here.

# def inicio(request):

#     return render(request, "AppCoder/inicio.html")

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

#Para el login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):

    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                avatares=Avatar.objects.filter(user = request.user.id)
                
                for i in range(len(avatares)):
                    if avatares[i] =='':
                
                        return render(request, "AppCoder/inicio.html")
                
                    else:
                        return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url})
               
            else:
                return render(request, "AppCoder/mensaje.html", {"mensaje":"Datos incorrectos, por favor intenta loguearte nuevamente"})
           
        else:

            return render(request, "AppCoder/mensaje.html", {"mensaje":"Datos incorrectos, por favor intenta loguearte nuevamente"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})

def register(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/mensaje.html" ,  {"mensaje":"Usuario Creado! por favor selecciona Login para loguearte"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})

from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    
    avatares=Avatar.objects.filter(user = request.user.id)

    for i in range(len(avatares)):
        if avatares[i] =='':
                
            return render(request, "AppCoder/inicio.html")
                
        else:
            return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url})
    return render(request, "AppCoder/inicio.html")


# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()

            return render(request, "AppCoder/mensaje.html", {"mensaje":"Haz cambiado tus datos correctamente!"})

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miFormulario = AvatarFormulario(request.POST, request.FILES) #Aca llega toda la informacion
        avatares=Avatar.objects.filter(user = request.user.id)
        if miFormulario.is_valid():
            u=User.objects.get(username=request.user)
            avatar=Avatar(user=u, imagen=miFormulario.cleaned_data["imagen"])
            avatar.save()
            return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url}) #vuelve al inicio

    else:
        miFormulario = AvatarFormulario() #formulario para construir el html            
      
    return render(request, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario})

def mensaje(request):

    return render(request, "AppCoder/mensaje.html")

def about(request):

    return render(request, "AppCoder/about.html")

def index(request):

    return render(request, "AppCoder/index.html")

@login_required
def userDetalle(request):

    return render(request, "AppCoder/user_detalle.html")