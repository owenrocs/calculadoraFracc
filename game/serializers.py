from rest_framework import serializers
from . models import Reto,Jugadores,Usuarios,Partidas

# Create your models here.

class RetoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reto
        fields = ('id','nombre','minutos_jugados')

#Serializar los campos - conversion de JSON a un registro de la base de datos
class JugadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jugadores
        fields = ('id','grupo','num_lista')

class UsuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('id','password')

class PartidasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partidas
        fields = ('id','fecha','id_ususario','minutos_jugados','puntaje')