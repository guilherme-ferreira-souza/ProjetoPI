from django.urls import path
from .views import PerfilView, CadView, LoginView, PedidosView, BaseView, CarView, EuroView, FavView, RetroView, SacView, SelecView, TesteView, register

urlpatterns = [
    path('cadastro/', CadView.as_view()),
    path('perfil/', PerfilView.as_view()),
    path('login/', LoginView.as_view()),
    path('pedidos/', PedidosView.as_view()),
    path('', BaseView.as_view(), name = 'home'),
    path('torcedor/', BaseView.as_view(), name = 'torcedor'),
    path('carrinho/', CarView.as_view()),
    path('europeias/', EuroView.as_view(), name = 'euro'),
    path('favoritos/', FavView.as_view()),
    path('retro/', RetroView.as_view(), name = 'retro'),
    path('sac/', SacView.as_view()),
    path('selecoes/', SelecView.as_view(), name = 'selec'),
    path('teste/', TesteView.as_view(), name = 'teste'),
    path('cadastro/', register, name = 'cadastro'),

]
