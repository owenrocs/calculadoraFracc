from django.shortcuts import render
from django.http import HttpResponse
from fractions import Fraction
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps
import sqlite3

# loads -> convierte un string a un objeto JSON
# dumps -> convierte un objeto JSON a un string

# Create your views here.
class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    def toJSON(self):
        return dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)
    

def index(request):
    #return HttpResponse('<h1> Hola Mundo! </h1>')
    return render(request, 'index.html')


def proceso(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    return HttpResponse('Hola ' + nombre)

def bienvenida(request):
    letrero = "Bienvenida"
    return HttpResponse(letrero)

@csrf_exempt
def suma(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
    num_resultado = (den1 * num2) + (den2 * num1)
    den_resultado = den1 * den2
    resultado = Fraccion(num_resultado,den_resultado)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")

@csrf_exempt
def resta(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
    num_resultado = (num1 * den2) - (den1 * num2)
    den_resultado = den1 * den2
    #resultado = Fraccion(num_resultado,den_resultado)
    resultado = Fraction(num_resultado,den_resultado)
    #resultado_json = resultado.toJSON()
    #return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")
    return HttpResponse(resultado, content_type = "text/json-comment-filtered")
    ##### IMPLEMENTACION DE LIBRERIA FRACTIONS #####  

#def multiplicacion(request):
#    #Obtener parametros de un endpoint
#    p = request.GET['p']
#    q = request.GET['q']
#    r = int(p) * int(q)
#    return HttpResponse("Multiplicacion: " + p + " * " + q + " = " + str(r))

@csrf_exempt
def multiplicacion(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
    num_resultado = num1 * num2
    den_resultado = den1 * den2
    resultado = Fraccion(num_resultado,den_resultado)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")

@csrf_exempt
def division(request):
    #Division por medio del metodo POST
    #Comando para usar formato unicode -> body codificado en UTF-8
    body_unicode = request.body.decode('utf-8')
    #Cargar el cuerpo de la peticion
    body = loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
    num_resultado = num1 * den2
    den_resultado = den1 * num2
    resultado = Fraccion(num_resultado,den_resultado)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")

def usuarios(request):
    #Conexion a la base de datos
    conexion = sqlite3.connect('db.sqlite3')
    #Crear un cursor
    cursor = conexion.cursor()
    # #Ejecutar una consulta
    res = cursor.execute("SELECT * FROM usuarios")
    #Obtener los resultados
    resultado = res.fetchall()
    # For para imprimir los resultados en forma de tabla
    #for fila in resultado:
    #    id, grupo, grado, numero = registro
    #Cerrar la conexion
    #conexion.close()
    #Retornar los resultados
    return render(request, 'usuarios.html', {'usuarios': resultado})

@csrf_exempt
def usuarios_p(request):
    #Comando para usar formato unicode -> body codificado en UTF-8
    body = request.body.decode('utf-8')
    body = loads(body)
    grupo = body['grupo']
    grado = body['grado']
    numero = body['numero']
    #print(str(grupo) + " " + str(grado) + " " + str(numero))
    conexion = sqlite3.connect('db.sqlite3')
    #Crear un cursor
    cursor = conexion.cursor()
    #Ejecutar un insert
    res = cursor.execute("INSERT INTO usuarios (grupo, grado, num_lista) VALUES (?,?,?)", (grupo, grado, numero))
    conexion.commit()
    return HttpResponse("Usuario agregado")

@csrf_exempt
def usuarios_d(request):
    #Comando para usar formato unicode -> body codificado en UTF-8
    body = request.body.decode('utf-8')
    body = loads(body)
    grupo = body['grupo']
    grado = body['grado']
    numero = body['numero']
    #print(str(grupo) + " " + str(grado) + " " + str(numero))
    conexion = sqlite3.connect('db.sqlite3')
    #Crear un cursor
    cursor = conexion.cursor()
    #Ejecutar un delete
    #sql_query = "DELETE FROM usuarios WHERE grupo = ? AND grado = ? AND num_lista = ?"
    res = cursor.execute("DELETE FROM usuarios WHERE grupo = ? AND grado = ? AND num_lista = ?", (grupo, grado, numero))
    conexion.commit()
    return HttpResponse("Usuario eliminado")