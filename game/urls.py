from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'reto', views.RetoViewSet)
router.register(r'jugador', views.JugadoresViewSet)
router.register(r'partida', views.PartidasViewSet)
router.register(r'usuario', views.UsuariosViewSet)

urlpatterns = [
    path('api',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
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
    path('barras', views.barras, name = 'barras'),
    path('consultPartidas', views.consultPartidas, name = 'consultPartidas'),
    #Path para grafica de burbuja
    path('bubbleChart', views.bubbleChart, name = 'bubbleChart'),
]