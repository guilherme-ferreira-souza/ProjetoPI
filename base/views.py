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