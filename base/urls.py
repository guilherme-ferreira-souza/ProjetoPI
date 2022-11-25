from django.urls import path
from .views import IndexView, BaseView, CadsView, SerieAView, BundesligaView, SelecoesView, PremierView, logView, TesteBund, TestePL, TesteSA, TesteSel

urlpatterns = [
    path('', BaseView.as_view(), name = 'home'),
    path('cadastro/', CadsView.as_view(), name = 'cadastro'),
    path('seriea/', SerieAView.as_view(), name = 'seriea'),
    path('bundes/', BundesligaView.as_view(), name = 'bundes'),
    path('selecoes/', SelecoesView.as_view(), name = 'selecoes'),
    path('PL/', PremierView.as_view(), name = 'PL'),
    path('log/', logView.as_view(), name = 'log'),
    path('bund2/', TesteBund.as_view(), name = 'bund'),
    path('sel2/', TesteSel.as_view(), name = 'sel'),
    path('PL2/', TestePL.as_view(), name = 'PL2'),
    path('SA2/', TesteSA.as_view(), name = 'SA2'),

]
