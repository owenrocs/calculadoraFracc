from django.shortcuts import render
from django.http import HttpResponse
from fractions import Fraction
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps
from django.shortcuts import redirect
from random import randrange
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

@csrf_exempt
def usuarios(request):
    if request.method == 'GET':
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
    
    elif request.method == 'POST':
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
    
    elif request.method == 'DELETE':
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
        res = cursor.execute("DELETE FROM usuarios WHERE grupo = ? AND grado = ? AND num_lista = ?", (grupo, grado, numero))
        conexion.commit()
        return HttpResponse("Usuario eliminado")


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
    res = cursor.execute("DELETE FROM usuarios WHERE grupo = ? AND grado = ? AND num_lista = ?", (grupo, grado, numero))
    conexion.commit()
    return HttpResponse("Usuario eliminado")

############ Clase en zoom martes

@csrf_exempt
#servicio endpoint de validación de usuarios
#entrada: { "id_usuario" :"usuario","pass" : "contrasenia"}
#salida: {"estatus":True}
@csrf_exempt
def valida_usuario(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    usuario  = eljson['id_usuario']
    contrasenia = eljson['pass']
    print(usuario+contrasenia)
    #con = sqlite3.connect("db.sqlite3")
    #cur = con.cursor()
    #res = cur.execute("SELECT * FROM usuarios WHERE id_usuario=? AND password=?",(str(usuario), str(contrasenia)))
    #si el usuario es correcto regresar respuesta exitosa 200 OK
    #en caso contrario regresar estatus falso
    return HttpResponse('{"estatus": true}')

def grafica(request):
    h_var = 'x'
    v_var = 'y'
    data = [['id_usuario', 'minutos_jugados', 'puntaje'],
            ['1', 10, 20],
            ['2', 20, 30],
            ['3', 30, 40],
            ['4', 40, 50],
            ['5', 50, 60],
            ['6', 60, 70]]
    # loop to append list of three random values to data object
    for i in range(7):
        data.append([randrange(101),randrange(101)])
    # convert data object to JSON
    h_var_JSON = json.dumps(h_var)
    v_var_JSON = json.dumps(v_var)
    modified_data = json.dumps(data)
    return render(request, 'charts.html', {'values':modified_data, 'h_titlw':h_var_JSON, 'v_title':v_var_JSON})
