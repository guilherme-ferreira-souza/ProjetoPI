from http.client import HTTPResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

from .models import User

# Create your views here.
'''
def view_home(request):
    return httpResponse('pag')

def view_about(request):
    return httpResponse('about')
'''




'''def view_home(request):
    return render (request, 'home.html')'''
  

class LoginView(TemplateView):
    template_name = 'base/pages/login.html'

class PerfilView(TemplateView):
    template_name = 'base/pages/perfil.html'

class PedidosView(TemplateView):
    template_name = 'base/pages/pedidos.html'

class BaseView(TemplateView):
    template_name = 'base/pages/home.html'

class CadView(TemplateView):
    template_name = 'base/pages/cadastro.html'

class CarView(TemplateView):
    template_name = 'base/pages/carrinho.html'

class EuroView(TemplateView):
    template_name = 'base/pages/europa.html'

class FavView(TemplateView):
    template_name = 'base/pages/favoritos.html'

class RetroView(TemplateView):
    template_name = 'base/pages/retro.html'

class SacView(TemplateView):
    template_name = 'base/pages/sac.html'

class SelecView(TemplateView):
    template_name = 'base/pages/selecoes.html'

class TesteView(TemplateView):
    template_name = 'teste.html'
    
def register(request):
    if request.method == 'GET':
        return render(request, "base/pages/cadastro.html")
    
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username).first()   
        if user:
            return render(request, "core/pages/permission.html")
        
        user = User.objects.create_user(username=username, email=email, password=password) 
        user.save()
        return render(request, "base/pages/home.html")