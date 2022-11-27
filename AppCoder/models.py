from django.db import models

# Create your models here.
class Familia(models.Model):

    nombre = models.TextField(max_length=40)
    apellido = models.TextField(max_length=40)
    edad = models.IntegerField()
    cumpleanios = models.DateField()


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()

    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.nombre}, Comisión: {self.comision}'


class Profesor(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Correo: {self.email}'

    def __set__(self, nombre, apellido, email, profesion):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.profesion = profesion


class Empleado(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    puesto = models.CharField(max_length=40)
    dni = models.IntegerField()

    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Puesto Laboral: {self.puesto}, DNI: {self.dni}'



    

