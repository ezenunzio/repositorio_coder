from django.shortcuts import render
#Auth
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class AdminLoginView(LoginView):
    template_name = 'usuarios/login.html'

class AdminLogoutView(LogoutView):
    template_name = 'usuarios/logout.html'