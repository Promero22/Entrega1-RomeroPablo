from django.db import models

# Create your models here.

class Profesional(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Profesión {self.profesion}"

class Especialidad(models.Model):

    nombre=models.CharField(max_length=30)
    numero = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Numero: {self.numero}"

class Sucursal(models.Model):
    localidad= models.CharField(max_length=30)
    direccion= models.CharField(max_length=30)
    telefono= models.IntegerField()
    email= models.EmailField()

    def __str__(self):
        return f"Localidad: {self.localidad} - Direccion: {self.direccion} - Telefono: {self.telefono} - E-Mail: {self.email}"