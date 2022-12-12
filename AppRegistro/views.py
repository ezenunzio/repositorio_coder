from django.shortcuts import render
from django.views.generic.edit import CreateView
#Redirección
from django.urls import reverse_lazy

#Formularios
from .forms import SignUpForm, UserEditForm

# Create your views here.
#Register
class SignUpView(CreateView):

    form_class = SignUpForm
    success_url = reverse_lazy('Home')
    template_name = 'usuarios/signup.html'


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
    return render(request, 'publicaciones/admin_update.html', {
        'form': usuario_form, 
        'usuario': usuario
        })