"""mi_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import mostrar_index
from . import views 

urlpatterns = [
    path("", mostrar_index, name='Página Principal'), 
    path("crear_curso/", views.crear_curso, name='Crear Curso'), 
    path("crear_profesor/", views.crear_profesor, name='Crear Profesor'),
    path("crear_empleado/", views.crear_empleado, name='Crear Empleado'),
    path("buscar_comision/", views.buscar_comision, name='Buscar Comision'),
    path("buscar_profesor/", views.buscar_profesor, name='Buscar Profesor'),
    path("buscar_empleado/", views.buscar_empleado, name='Buscar Empleado'),
    path("mostrar_profesores/", views.mostrar_profesores, name='Mostrar Profesor'),
    path("eliminar_profesor/<id_profesor>", views.eliminar_profesor, name='Eliminar Profesor'),
    path("actualizar_profesor/<id_profesor>", views.actualizar_profesor, name='Actualizar Profesor'),
    path("curso_list/", views.CursoList.as_view(), name='List'),
    path("curso_detail/ <pk>", views.CursoDetailView.as_view(), name='Detail'),
]