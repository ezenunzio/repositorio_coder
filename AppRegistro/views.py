from django.shortcuts import render
from django.views.generic.edit import CreateView
#Redirección
from django.urls import reverse_lazy

#Auth
from django.contrib.auth.views import LoginView, LogoutView
#.Los decoradores sirven para vistas basadas en funciones
from django.contrib.auth.decorators import login_required #valida que el usuario haya iniciado sesión antes de ejecutar 
#Los mixins sirven para vistas basadas en clases
from django.contrib.auth.mixins import LoginRequiredMixin

#Formularios
from .forms import SignUpForm, UserEditForm

# Create your views here.
#Register
class SignUpView(CreateView):

    form_class = SignUpForm
    success_url = reverse_lazy('Home')
    template_name = 'signup.html'


class AdminLoginView(LoginView):
    template_name = 'login.html'

class AdminLogoutView(LogoutView):
    template_name = 'logout.html'

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