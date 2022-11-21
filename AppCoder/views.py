from django.shortcuts import render
from .models import Familia,Curso, Profesor
from .forms import CrearCursoForm, CrearProfesorForm
# Create your views here.



def mostrar_familia(request):
    
   f1 = Familia(nombre="Pablo", apellido="Nunzio", edad=55, cumpleanios='1967-04-11')
   f2 = Familia(nombre="Lisandro", apellido="Nunzio", edad=25, cumpleanios='1997-03-09')
   f3 = Familia(nombre="Ezequiel", apellido="Nunzio", edad=22,cumpleanios='2000-09-10')
   f4 = Familia(nombre="Carina", apellido="Martinez", edad=51, cumpleanios='1963-08-11')
   return render(request, 'familiares.html', {'familia':[f1, f2, f3, f4]})

def mostrar_index(request):
    return render(request, 'index.html')

    
def mostrar_referencias(request):
    return render(request, 'referencias.html')

def mostrar_repaso(request):
    return render(request, 'repaso.html')

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


def buscar_comision(request):

    if request.GET.get('comision', False):
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)

        return render(request, 'buscar_comision.html', {'cursos': cursos})
    else:
        respuesta = 'No hay datos'
    return render(request, 'buscar_comision.html', {'respuesta': respuesta}) 


def buscar_profesor(request):
    
    if request.GET.get('email', False):
        email = request.GET['email']
        profesores = Profesor.objects.filter(email__icontains=email)

        return render(request, 'buscar_profesor.html', {'profesores': profesores})
    else:
        respuesta = 'No hay datos'
    return render(request, 'buscar_profesor.html', {'respuesta': respuesta}) 