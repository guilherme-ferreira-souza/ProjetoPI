from django.urls import path
from .views import IndexView, BaseView, CadsView, SerieAView, BundesligaView, SelecoesView, PremierView, logView

urlpatterns = [
    path('', BaseView.as_view(), name = 'home'),
    path('cadastro/', CadsView.as_view(), name = 'cadastro'),
    path('seriea/', SerieAView.as_view(), name = 'seriea'),
    path('bundes/', BundesligaView.as_view(), name = 'bundes'),
    path('selecoes/', SelecoesView.as_view(), name = 'selecoes'),
    path('PL/', PremierView.as_view(), name = 'PL'),
    path('log/', logView.as_view(), name = 'log'),

]
