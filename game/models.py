from django.db import models

# Create your models here.

class Reto(models.Model):
    nombre = models.CharField(max_length=30)
    minutos_jugados = models.IntegerField()

class Jugadores(models.Model):
    grupo = models.CharField(max_length=2)
    num_lista = models.IntegerField()

class Usuarios(models.Model):
    password = models.CharField(max_length=30)

class Partidas(models.Model):
    fecha = models.CharField(max_length=30)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, db_column='id_usuario')
    minutos_jugados= models.CharField(max_length=30)
    puntaje = models.CharField(max_length=30)