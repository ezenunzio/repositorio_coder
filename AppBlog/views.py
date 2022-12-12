from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def mostrar_index(request):
    
    "imagenes = Avatar.objects.filter(user=request.user.id)[0].imagen.url"

    return render(request, 'index.html')
    
class HomePageView(TemplateView):
    template_name = 'index.html'
    
    
class PostList(LoginRequiredMixin, ListView): ## LoginRequiredMixin es una clase que valida que el usuario haya iniciado sesión antes de ejecutar la vista
    model = Post
    template_name = 'publicaciones/post_list.html'
    paginate_by = 8
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.postobjects.all()
        return context
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'publicaciones/post_detail.html'


class PostDeleteView(DeleteView):
    #Recordatorio: en success_url, utilizar el nombre de la url. Este permite redirigir a otro template
    #Ejemplo:
    #path("curso_list/", views.CursoList.as_view(), name='List')
    #en este caso utilizar el string del primer parámetro
    #antecedido de un /
    model = Post
    success_url = '/post_list'

class PostUpdateView(UpdateView):
    model = Post
    success_url = '/post_list'
    fields = ['category', 'title','content','imagen']

class PostCreateView(CreateView):
    model = Post
    success_url = '/post_list'
    fields = ['nombre', 'comision']
    
