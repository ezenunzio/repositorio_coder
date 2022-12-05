from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CrearCursoForm(forms.Form):

    #Especificar los campos
    curso = forms.CharField()
    comision = forms.IntegerField()


class CrearProfesorForm(forms.Form):   
    nombre= forms.CharField(min_length=5, max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)


class CrearEmpleadoForm(forms.Form):
        
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    puesto = forms.CharField(max_length=40)
    dni = forms.IntegerField()

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class UserEditForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        help_texts = {k: '' for k in fields}