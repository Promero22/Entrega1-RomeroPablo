from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('profesional/list', views.ProfesionalList.as_view(), name='PList'),
    path(r'^(?P<pk>\d+)$', views.ProfesionalDetalle.as_view(), name='PDetail'),
    path(r'^nuevo$', views.ProfesionalCreacion.as_view(), name='PNew'),
    path(r'^editar/(?P<pk>\d+)$', views.ProfesionalUpdate.as_view(), name='PEdit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ProfesionalDelete.as_view(), name='PDelete'),
    path('sucursal/list', views.SucursalList.as_view(), name='SList'),
    path('sucursal/<int:pk>', views.SucursalDetalle.as_view(), name='SDetails'),
    path('sucursal/nuevo', views.SucursalCreacion.as_view(), name='SNew'),
    path('sucursal/editar/<int:pk>', views.SucursalUpdate.as_view(), name='SEdit'),
    path('sucursal/eliminar/<int:pk>', views.SucursalDelete.as_view(), name='SDelete'),
    path('especialidad/list', views.EspecialidadList.as_view(), name='EList'),
    path('especialidad/<int:pk>', views.EspecialidadDetalle.as_view(), name='EDetails'),
    path('especialidad/nuevo', views.EspecialidadCreacion.as_view(), name='ENew'),
    path('especialidad/editar/<int:pk>', views.EspecialidadUpdate.as_view(), name='EEdit'),
    path('especialidad/eliminar/<int:pk>', views.EspecialidadDelete.as_view(), name='EDelete'),
    path('buscar/', views.buscar),
    path('busquedaEspecialidad', views.busquedaEspecialidad, name='BusquedaEspecialidad'),  
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    path('mensaje', views.mensaje ,name="Mensaje"),
    path('about', views.about ,name="About"),
    path('index', views.index ,name="Index"),
    path('userDetalle', views.userDetalle ,name="UserDetalle"),
]


