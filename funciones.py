#Lucas Figueroa 1J 1er Parcial de labo

import re
import json


def traer_datos(ruta: str) -> list:
    """Funcion que recibe un parametro del tipo ``str`` especificando la ruta del archivo a leer\n
    Lee el archivo y retorna una lista ( `` list `` ) con todos los datos para trabajar."""
    with open(ruta, 'r') as archivo:
        datos = json.load(archivo)
    return datos['results']

def copiar_lista(lista:list)->list:
    """ Funcion que recibe una ``lista`` como parametro, y retorna una ``copia`` de la lista pasada por parametro """
    return lista.copy()


def pedir_asc_o_dec()-> str:
    """ Funcion que Consulta al usuario, el ``orden`` , se valida mediante un while y un match, retorna el ``orden esperado``. """
    
    asc_dec = input(" ordenar en orden ascendente: ingresa [asc] \n ordenar en orden descendente: ingresa [desc]\n\n ")
    while (not re.match(r"(asc|desc)", asc_dec)):
        asc_dec = input(
            " ingresar bien la opcion ordenar en orden ascendente: ingresa [asc] \n ordenar en orden descendente: ingresa [desc]\n\n ")
    return asc_dec


def ordenamiento(lista: list, orden: str, key: str):
    """ funcion que realiza un ``ordenamiento``. Recibe como parametro una ``lista a ordenar``, ``el orden`` en que se va a ordenar\n
     y una ``key`` que especifica ``en base a que elemento`` vamos a ordenar la lista. """
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if (orden == 'asc' and float(lista[j][key]) > float(lista[j+1][key])) or (orden == 'desc' and float(lista[j][key]) < float(lista[j+1][key])):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

#1
def listar_personajes_ordenados_altura(lista: list) -> list:
    """ Funcion que muestra los personajes ordenados ``en base a la altura``. Recibe como parametro ``la lista a ordenar`` \n
    y ``retorna la lista ya ordenada``. """
    asc_dec = pedir_asc_o_dec()
    ordenamiento(lista, asc_dec,'height')
    for elementos in lista:
        print(f"Nombre: {elementos['name']}  || Altura: {elementos['height']}")
    return lista

#2
def mas_alto_genero(genero:str,lista:list) -> dict:
    """ funcion que encuentra el mayor en las alturas en una lista en base al genero. Recibe como parametro el genero``str``\n
    y la ``lista``a iterar. retorna el ``diccionario mayor encontrado`` """  
    flag = True
    mayor = {}
    for elementos in lista:
        if(elementos['gender'] == genero and (flag == True or float(elementos['height']) > float(mayor['height']))):
                mayor = elementos
                flag = False
    return mayor

def mas_altos_cada_genero(lista:list):
    """ funcion que muestra los mas altos en cada genero .  Recibe una ``lista`` como parametro """
    lista_generos = ['n/a','female','male']
    for elementos in lista_generos:
        print("Nombre:  {}   Altura:  {}".format(mas_alto_genero(elementos,lista)['name'],mas_alto_genero(elementos,lista)['height']))

#3
def ordenar_y_listar_por_peso(lista:list):
    """ Funcion que ordena una lista, en base al peso. Recibe una ``lista`` como parametro """
    asc_dec = pedir_asc_o_dec()
    ordenamiento(lista, asc_dec,'mass')
    for elementos in lista:
        print(f"Nombre: {elementos['name']}  || Peso: {elementos['mass']}") 

#4
def buscar_personajes(lista:list):
    """ Funcion que ``busca los personajes`` en base al ``input del usuario``, dicho input puede ser ``aproximado``\n
     no necesariamente exacto para realizar la busqueda. Recibe una lista como parametro y ``muestra`` el personaje encontrado """
    
    patron = r"[a-zA-Z\- 0-9]{2,}"
    usuario_input = input("ingresa un personaje a buscar ... \n")
    
    if re.match(patron,usuario_input):
        bandera = True
        for personajes in lista:
            nombres = personajes['name']
            if re.search(usuario_input.lower(), nombres.lower()):
                print( f"\n::::::::::::::Star Wars App::::::::::::::\n\n"
                      f"Nombre: {personajes['name']}\nAltura: {personajes['height']}\n"
                    f"Peso: {personajes['mass']}\nGenero: {personajes['gender']}")
                bandera = False

        if bandera == True:
            print("Error,nombre mal ingresado")
            
    else:
        print("Error,Nombre mal ingresado")
#5
def guardar(nombre:str,lista:list):
    """ Funcion que guarda en un archivo ``.csv`` los datos de la lista. Recibe como parametro el ``nombre`` a ponerle al archivo\n
     y una ``lista`` para iterar y escribir su contenido en el ``archivo`` """
    with open(f"archivo_{nombre}.csv",'w') as archivo:
        datos = []
        for elemento in lista:
            datos.append(f"{elemento['name']},{elemento['height']},{elemento['mass']},"
                         f"{elemento['gender']}")
            lineas = "\n".join(datos)
            
        archivo.write(",".join(lista[0].keys())+'\n')
        archivo.write(lineas)
        
#formatear salida 

def validar_lista_vacia(lista:list)->bool:
    """ Funcion que ``valida`` si la lista esta vacia o no. Recibe como parametro la ``lista``. Retorna ``True`` O ``False`` dependiendo el ``len`` """
    if len(lista) > 0:
        return True
    else:
        return False


def validar_opcion_menu(string:str)->int:
    """ Funcion que valida las opciones del menu. Recibe como parametro un ``str`` proporcionado por el usuario\n
     dicho string lo ``validamos`` para que sea el resultado esperado. Retorna el input matcheado casteado a ``int``. """
    if(re.search(r"^[1-6]$",string)):
        return int(string)
    else:
        print("opcion invalida. Selecciona Otra Vez.")
        return -1

def validar_ejecutado_1(opcion:int):
    if opcion == 1:
        return True
    else:
        return print("Error. Tiene que ingresar antes a la opcion 1 ") 
    
def pedir_nombre_usuario()->str:
    patron = r"[a-zA-Z]+"
    input_user = input("ingresa un nombre para el archivo: \n\n")
    while not re.match(patron,input_user):
        input_user = input("Error . ingresa un nombre valido para el archivo: \n\n")
    return input_user
    
def menu(lista:list):
    """ Funcion menu la cual muestra todos nuestras opciones e itera en un bucle while esperando a que el usuario\n
     ingrese a una opcion """
    if validar_lista_vacia(lista):
        opcion = None
        ejecutado = 0
        while(opcion!=6):
            opcion = validar_opcion_menu(input("\n\n1 listar_personajes_ordenados_altura\n"
                    "2 mas_altos_cada_genero\n"
                    "3 ordenar_y_listar_por_peso\n"
                    "4 buscar_personajes\n"
                    "5 guardar\n"
                    "6 Salir\n\n"))
            
            if opcion == 1: 
                lista = listar_personajes_ordenados_altura(lista)
                ejecutado = 1
            elif(opcion == 2):mas_altos_cada_genero(lista)
            elif(opcion == 3):ordenar_y_listar_por_peso(lista)
            elif(opcion == 4):buscar_personajes(lista)
            elif(opcion == 5):
                if validar_ejecutado_1(ejecutado):
                    guardar(pedir_nombre_usuario(),lista)
                
    else:
        print('Error al ejecutar el programa."LISTA VACIA" Verifique si la lista tiene datos para operar.')


def stark_wars_app():
    """ Funcion principal ``Star Wars App``, Realiza la ``carga de los datos`` para comenzar a operar con el ``menu de inicio: menu()`` """
    lista_star_wars = traer_datos("RUTA DEL JSON")
    lista_star_wars_copy = lista_star_wars.copy()
    menu(lista_star_wars_copy)