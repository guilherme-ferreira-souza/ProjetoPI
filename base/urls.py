from django.urls import path
from .views import IndexView, BaseView, CadsView

urlpatterns = [
    path('', IndexView.as_view(), name = 'home'),
    path('teste/', BaseView.as_view(), name = 'teste'),
    path('cadastro/', CadsView.as_view(), name = 'cadastro'),


]
