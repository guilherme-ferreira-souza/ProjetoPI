from django.urls import path
from .views import IndexView, BaseView, CadsView

urlpatterns = [
    path('', BaseView.as_view(), name = 'home'),
    path('cadastro/', CadsView.as_view(), name = 'cadastro'),


]
