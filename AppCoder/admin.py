from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos


admin.site.register(Profesional)

admin.site.register(Especialidad)

admin.site.register(Sucursal)

admin.site.register(Avatar)