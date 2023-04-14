from django.shortcuts import render
from rest_framework import viewsets
from . serializers import RetoSerializer,JugadorSerializer,UsuariosSerializer,PartidasSerializer
from .models import Reto,Jugadores,Usuarios,Partidas
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps
import sqlite3 
import requests
from random import randrange

# loads -> convierte un string a un objeto JSON
# dumps -> convierte un objeto JSON a un string

# Create your views here.
@csrf_exempt
def registro(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    username = body['username']
    password = body['password']
    group = body['group']
    datos = (username,password,group)
    message ={'message': 'Registro exitoso' }
    return HttpResponse(dumps(message),datos, content_type='application/json')

def juego(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    username = body['username']

    if username == 'eg_user' :
        message = {'message': 'Usuario autenticado'}
    else:
        message = {'message': 'Usuario no autenticado'}
    return HttpResponse(dumps(message), content_type='application/json')


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
        #role = 
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


### Tarea REST framework ###
class RetoViewSet(viewsets.ModelViewSet):
    queryset = Reto.objects.all() #all recupera todos los registro de la entidada Reto
    serializer_class = RetoSerializer
    
#### "METODO REST #####
class JugadoresViewSet(viewsets.ModelViewSet): #va hacer las 4 vistas(insertar, enlistar, etc) de tipo jugador
    queryset = Jugadores.objects.all() #select * from Calculadora.Jugadores
    serializer_class = JugadorSerializer

class PartidasViewSet(viewsets.ModelViewSet):
    queryset = Partidas.objects.all() #all recupera todos los registro de la entidada Reto
    serializer_class = PartidasSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all() #all recupera todos los registro de la entidada Reto
    serializer_class = UsuariosSerializer

# Graficas
def grafica(request):
    #h_var : The title for horizontal axis
    h_var = 'X'

    #v_var : The title for horizontal axis
    v_var = 'Y'

    #data : A list of list which will ultimated be used 
    # to populate the Google chart.
    data = [[h_var,v_var]]
    """
    An example of how the data object looks like in the end: 
        [
          ['Age', 'Weight'],
          [ 8,      12],
          [ 4,      5.5],
          [ 11,     14],
          [ 4,      5],
          [ 3,      3.5],
          [ 6.5,    7]
        ]
    The first list will consists of the title of horizontal and vertical axis,
    and the subsequent list will contain coordinates of the points to be plotted on
    the google chart
    """

    #The below for loop is responsible for appending list of two random values  
    # to data object
    for i in range(0,11):
        data.append([randrange(101),randrange(101)])

    #h_var_JSON : JSON string corresponding to  h_var
    #json.dumps converts Python objects to JSON strings
    h_var_JSON = dumps(h_var)

    #v_var_JSON : JSON string corresponding to  v_var
    v_var_JSON = dumps(v_var)

    #modified_data : JSON string corresponding to  data
    modified_data = dumps(data)

    #Finally all JSON strings are supplied to the charts.html using the 
    # dictiory shown below so that they can be displayed on the home screen
    return render(request,"charts.html",{'values':modified_data,\
        'h_title':h_var_JSON,'v_title':v_var_JSON})
## Dentro de grafica solo se hace la invocacion de servicio
# Las consultas de datos se hacen en los servicios CRUD
# Servicios CRUD

def barras(request):
    '''
    data = [
          ['Jugador', 'Minutos Jugados'],
          ['Ian', 1000],
          ['Héctor', 1170],
          ['Alan', 660],
          ['Manuel', 1030]
        ]
    '''
    data = []
    data.append(['Jugador', 'Minutos Jugados'])
    resultados = Reto.objects.all() #select * from reto;
    titulo = 'Videojuego Odyssey'
    titulo_formato = dumps(titulo)
    subtitulo= 'Total de minutos por jugador'
    subtitulo_formato = dumps(subtitulo)
    if len(resultados)>0:
        for registro in resultados:
            nombre = registro.nombre
            minutos = registro.minutos_jugados
            data.append([nombre,minutos])
        data_formato = dumps(data) #formatear los datos en string para JSON
        elJSON = {'losDatos':data_formato,'titulo':titulo_formato,'subtitulo':subtitulo_formato}
        return render(request,'barras.html',elJSON)
    else:
        return HttpResponse("<h1> No hay registros a mostrar</h1>")

# Consulta de datos para graficación con Google Charts    
def consultPartidas(request):
    entries = Partidas.objects.all()
    data = [['ID', 'Minutos jugados', 'Puntaje', 'ID Usuario', 'Tamaño (puntaje)']]
    for record in entries:
        idNum = str(record.id)
        minutos = int(record.minutos_jugados)
        puntaje = int(record.puntaje)
        id_usuario = str(record.id_usuario)    
        tamano = int(record.puntaje)    

        data.append([idNum, minutos, puntaje, id_usuario, tamano])
    data_json = dumps({'graphData': data})
    return HttpResponse(data_json, content_type='application/json')

#Funcion para graficar datos de partidas en graficas de burbuja
def bubbleChart(request):
    url = "http://127.0.0.1:8000/consultPartidas"
    response = requests.get(url)
    data = loads(response.content)['graphData']
    titulo = 'Videojuego Odyssey'
    titulo_formato = dumps(titulo)
    subtitulo= 'Total de minutos por jugador'
    subtitulo_formato = dumps(subtitulo)
    elJSON = {'graphData': data, 'titulo': titulo_formato, 'subtitulo': subtitulo_formato}
    return render(request,'bubble.html',elJSON)

'''
    # IDEA DE FORM PARA REGISTRO
    # Punto importante: Creacion de user_id

    def nuevoUsuarioAlumno(request):
        if (request.method == 'POST'):#POST
            form = CrearAlumnoForm(request.POST)
            if(form.is_valid()):
                # Atributos del formulario
                grupo = form.cleaned_data['grupo']
                listNumber = form.cleaned_data['listNumber']
                password = form.cleaned_data['password']
                # Atributo role predefinido y no modificable en el form
                role = 'alumno'
                # Creacion de user_id como un string
                userID = grupo + '_' +listNumber
                return HttpResponse('Nuevo usuario creado '+user_id)

                ### Creación de registro directo en BD
                # nuevo_registro = Alumno.objects.create(user_id=userID, password=password, grupo=grupo, list_num=listNumber, role=role)
                # nuevo_registro.save()

                #invoca el servicio de creación de usuario
                #Creación de registro usando api REST
                url = "http://127.0.0.1:8000/apireto/"
                header = {
                "Content-Type":"application/json"
                }
                payload = {   
                "user_id": userID,
                "password": password,
                "grupo": grupo,
                "list_num": listNumber,
                "role": role
                }
                result = requests.post(url,  data= dumps(payload), headers=header)
                if result.status_code == 201:
                    return HttpResponse('Nuevo usuario creado '+nombre_usuario)
                else:
                    return HttpResponse('Error al crear el usuario ')
                
        else:#GET
            form = CrearAlumnoForm
            return render(request, 'crearReto.html',{'form':form})

    class CrearAlumnoForm(forms.Form):
        grupo = forms.CharField(label='Grupo', max_length=2)
        listNumber = forms.CharField(label='Numero de lista', max_length=3)
        password = forms.CharField(label='Contraseña', max_length=20)

'''