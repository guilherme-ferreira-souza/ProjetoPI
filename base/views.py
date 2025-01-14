import email
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

class IndexView(TemplateView):
    template_name = 'base/index.html'

class BaseView(TemplateView):
    template_name = 'teste.html'

class CadsView(TemplateView):
    template_name = 'base/pages/cadastro.html'

class SerieAView(TemplateView):
    template_name = 'base/pages/SerieA.html'

class SelecoesView(TemplateView):
    template_name = 'base/pages/selecoes.html'

class PremierView(TemplateView):
    template_name = 'base/pages/PL.html'

class BundesligaView(TemplateView):
    template_name = 'base/pages/bundesliga.html'

class logView(TemplateView):
    template_name = 'base/pages/pag log.html'

class TesteBund(TemplateView):
    template_name = 'testebund2.html'

class TestePL(TemplateView):
    template_name = 'testePL2.html'

class TesteSA(TemplateView):
    template_name = 'testeSA2.html'

class TesteSel(TemplateView):
    template_name = 'testesel2.html'

