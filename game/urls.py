from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proceso', views.proceso, name = 'proceso'),
    path('bienvenida', views.bienvenida, name = 'bienvenida'),
    path('suma', views.suma, name = 'suma'),
    path('resta', views.resta, name = 'resta'),
    path('multiplicacion', views.multiplicacion, name = 'multiplicacion'),
    path('division', views.division, name = 'division'),
    path('usuarios', views.usuarios, name = 'usuarios'),
    path('usuarios_p', views.usuarios_p, name = 'usuarios_p'),
    path('usuarios_d', views.usuarios_d, name = 'usuarios_d'),
    path('valida_usuario', views.valida_usuario, name = 'valida_usuario'),
    path('grafica', views.grafica, name = 'grafica'),
]