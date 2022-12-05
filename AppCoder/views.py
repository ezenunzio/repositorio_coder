from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
#Redirección
from django.urls import reverse_lazy

#Auth
from django.contrib.auth.views import LoginView, LogoutView
#.Los decoradores sirven para vistas basadas en funciones
from django.contrib.auth.decorators import login_required #valida que el usuario haya iniciado sesión antes de ejecutar 
#Los mixins sirven para vistas basadas en clases
from django.contrib.auth.mixins import LoginRequiredMixin

#Modelos
from .models import Curso, Profesor, Empleado, Avatar
#Formularios
from .forms import CrearCursoForm, CrearProfesorForm, CrearEmpleadoForm, SignUpForm, UserEditForm


# Create your views here.



'''
def mostrar_familia(request):
    
   f1 = Familia(nombre="Pablo", apellido="Nunzio", edad=55, cumpleanios='1967-04-11')
   f2 = Familia(nombre="Lisandro", apellido="Nunzio", edad=25, cumpleanios='1997-03-09')
   f3 = Familia(nombre="Ezequiel", apellido="Nunzio", edad=22,cumpleanios='2000-09-10')
   f4 = Familia(nombre="Carina", apellido="Martinez", edad=51, cumpleanios='1963-08-11')
   contexto = {'familia':[f1, f2, f3, f4]}
   return render(request, 'Examples/familiares.html',context=contexto)

def mostrar_referencias(request):
    return render(request, 'Examples/referencias.html')

def mostrar_repaso(request):
    return render(request, 'Examples/repaso.html') 
'''

#@login_required #--valida que el usuario haya iniciado sesión antes de ejecutar la vista 
def mostrar_index(request):

    "imagenes = Avatar.objects.filter(user=request.user.id)[0].imagen.url"

    return render(request, 'index.html')


def crear_curso(request):

    if request.method == "POST":
        
        formulario = CrearCursoForm(request.POST)

        if formulario.is_valid():
        
            formulario_limpio = formulario.cleaned_data

            curso = Curso(nombre=formulario_limpio['curso'], comision=formulario_limpio['comision'])    

            curso.save()

            return render(request, "index.html")

    else:

        formulario = CrearCursoForm()
        
    return render(request, "crear_curso.html", {"formulario": formulario})


def crear_profesor(request):
    
    if request.method == "POST":
        
        proForm = CrearProfesorForm(request.POST)

        if proForm.is_valid():
        
            formulario_limpio = proForm.cleaned_data

            profesor = Profesor(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], 
                    email=formulario_limpio['email'], profesion=formulario_limpio['profesion'])    

            profesor.save()

            return render(request, "index.html")

    else:

        proForm = CrearProfesorForm()
        
    return render(request, "crear_profesor.html", {"profesor": proForm})


def crear_empleado(request):
    
    if request.method == "POST":
        
        formulario = CrearEmpleadoForm(request.POST)

        if formulario.is_valid():
        
            formulario_limpio = formulario.cleaned_data

            empleado = Empleado(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], email=formulario_limpio['email'], puesto=formulario_limpio['puesto'], dni=formulario_limpio['dni'] )    

            empleado.save()

            return render(request, "index.html")

    else:

        formulario = CrearEmpleadoForm()
        
    return render(request, "crear_empleado.html", {"formulario": formulario})


def buscar_comision(request):

    if request.GET.get('comision', False): 
        comision = request.GET['comision'] 
        cursos = Curso.objects.filter(comision__icontains=comision) 
        return render(request, 'buscar_comision.html', {'cursos': cursos}) 
    else:
        if 'comision' in request.GET:
            respuesta = 'No hay datos'
        else:
            respuesta = 'Haga la búsqueda'
    return render(request, 'buscar_comision.html', {'respuesta': respuesta}) 


def buscar_profesor(request):
    
    if request.GET.get('email', False):
        email = request.GET['email']
        profesores = Profesor.objects.filter(email__icontains=email)

        return render(request, 'buscar_profesor.html', {'profesores': profesores})
    else:
        if 'email' in request.GET:
            respuesta = 'No hay datos'
        else:
            respuesta = 'Haga la búsqueda'
    return render(request, 'buscar_profesor.html', {'respuesta': respuesta}) 

def buscar_empleado(request):
    
    if request.GET.get('dni', False):
        dni = request.GET['dni']
        empleados = Empleado.objects.filter(dni__icontains=dni)

        return render(request, 'buscar_empleado.html', {'empleados': empleados})
    else:
        if 'dni' in request.GET:
            respuesta = 'No hay datos'
        else:
            respuesta = 'Haga la búsqueda'
    return render(request, 'buscar_empleado.html', {'respuesta': respuesta}) 


def mostrar_profesores(request):

    profesores = Profesor.objects.all
    context = {'profesores': profesores}

    return render(request, 'mostrar_profesores.html', context= context)


def eliminar_profesor(request, id_profesor ):

    profesor = Profesor.objects.get(id=id_profesor)

    profesor.delete()

    profesores = Profesor.objects.all
    context = {'profesores': profesores}

    return render(request, 'mostrar_profesores.html', context= context)


def actualizar_profesor(request, id_profesor):
        
    profesor = Profesor.objects.get(id=id_profesor)

    if request.method == "POST":
        
        proForm = CrearProfesorForm(request.POST)

        if proForm.is_valid():
        
            formulario_limpio = proForm.cleaned_data

            profesor.__set__(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], email=formulario_limpio['email'], profesion=formulario_limpio['profesion'])

            profesor.save()

            return render(request, "index.html")

    else:

        proForm = CrearProfesorForm(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email, 'profesion': profesor.profesion,})
        
    return render(request, "actualizar_profesor.html", {"profesor": proForm})

def editar_usuario(request):
    usuario = request.user

    if request.method == 'POST':
        usuario_form = UserEditForm(request.POST)

        if usuario_form.is_valid():
            informacion = usuario_form.cleaned_data()

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()

            return render(request, 'index.html')
    
    else:
        usuario_form = UserEditForm(initial = {
            'username': usuario.username,
            'email': usuario.email
            })
    return render(request, 'AppCoder/admin_update.html', {
        'form': usuario_form, 
        'usuario': usuario
        })


#Vistas basadas en Clases.
class CursoList(LoginRequiredMixin, ListView): ## LoginRequiredMixin es una clase que valida que el usuario haya iniciado sesión antes de ejecutar la vista
    model = Curso
    template_name = 'AppCoder/curso_list.html'


class CursoDetailView(DetailView):
    model = Curso
    template_name = 'AppCoder/curso_detail.html'


class CursoDeleteView(DeleteView):
    #Recordatorio: en success_url, utilizar el nombre de la url. Este permite redirigir a otro template
    #Ejemplo:
    #path("curso_list/", views.CursoList.as_view(), name='List')
    #en este caso utilizar el string del primer parámetro
    #antecedido de un /
    model = Curso
    success_url = '/curso_list'

class CursoUpdateView(UpdateView):
    model = Curso
    success_url = '/curso_list'
    fields = ['nombre', 'comision']

class CursoCreateView(CreateView):
    model = Curso
    success_url = '/curso_list'
    fields = ['nombre', 'comision']


#Register
class SignUpView(CreateView):

    form_class = SignUpForm
    success_url = reverse_lazy('Home')
    template_name = 'signup.html'


class AdminLoginView(LoginView):
    template_name = 'login.html'

class AdminLogoutView(LogoutView):
    template_name = 'logout.html'