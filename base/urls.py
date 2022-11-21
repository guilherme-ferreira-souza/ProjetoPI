from django.urls import path
from .views import IndexView, BaseView, SobreView

urlpatterns = [
    path('', IndexView.as_view(), name = 'home'),
    path('teste/', BaseView.as_view(), name = 'teste'),
    path('sobre/', SobreView.as_view(), name = 'sobre'),


]
