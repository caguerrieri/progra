from ast import Pass
from asyncore import write
from errno import EADDRNOTAVAIL
from operator import index, length_hint, truediv
from pickletools import long1
from re import A
from tkinter import W
from turtle import fd
2


def crear_matriz_vacia():
    fila = 50
    columna = 50
    matriz = [0]*fila
    for i in range (fila):
        matriz[i]= [0]*columna
    return matriz


def recuperar_asientos(archivo_asientos):
    try:
        archivo = open(archivo_asientos, "r")
        asientos = archivo.readlines()    
        matriz = []

        for i in range(len(asientos)):      
            linea = asientos[i][7:]           
            nueva_fila = []
            for caracter in linea:
                if caracter == "1" or caracter == "0":
                    nueva_fila.append(int(caracter))
            matriz.append(nueva_fila)
        archivo.close
    except IOError:
        matriz = crear_matriz_vacia()

    return matriz

def matriz_str (matriz):      
    matriz_str = str()
    a = 0
    for fila in matriz:
        cadena = "fila"
        if a < 10:
            cadena += "0" + str (a) + "\t"
        else:
            cadena += str(a)+ "\t"
        a+=1
        for elemento in fila:
            cadena  += str(elemento)
            cadena += " "
        cadena += "\n"
        matriz_str+=cadena
    return matriz_str


def guardar_asientos (matriz):   
    archivo=open("archivo.txt","w")
    archivo.write(matriz)
    archivo.close()
    return

def validar_dni(dni):
    len_valida = False
    es_numero = True
    if len(dni) == 7 or len(dni) == 8:
        len_valida = True
        for num in dni:
            if not(num in "0123456789"):
                es_numero = False 
    return len_valida and es_numero

def validar_nombre(nombre):
    len_valida = False
    es_caracter = True
    if len(nombre) >4:
        len_valida = True
        for caracter in nombre:
            if caracter in " ":
                es_caracter = False
    return len_valida and es_caracter

def validar_edad(edad):
    edad_valida = False
    es_numero = True
    for numero in edad:
        if not numero in ("0123456789"):
            es_numero = False
    if es_numero:
        edad = int(edad)
        if edad >= 10 and edad <= 110:
            edad_valida = True
    return edad_valida and es_numero

def pedir_edad():
    edad_valida = False
    while not edad_valida:
        edad = input("ingrese su edad: ")
        edad_valida = validar_edad(edad)
        if not edad_valida:
            print("Edad no valida ")
    return edad


def pedir_nombre():
    nombre_valido = False
    while not nombre_valido:
        nombre = input("ingrese su nombre: ")
        nombre_valido = validar_nombre(nombre)
        if not nombre_valido:
            print("Usuario no valido:")
    return nombre

def pedir_dni():
    dni_valido = False
    while not dni_valido:
        dni = input("Ingrese su DNI: ")
        dni_valido = validar_dni(dni)
        if not dni_valido:
            print("DNI no valido!")
    return dni



def comparar_dni_nombre (ventas, nombre_nuevo, dni_nuevo):
    valido = True
    if len(ventas) == 0:         
        valido = True
    else:
        print(ventas)
        for venta in ventas:
            print("esta es la venta:",venta)
            nombre_viejo = venta[1]
            dni_viejo = venta[3]
            if nombre_viejo == nombre_nuevo and dni_viejo != dni_nuevo:
                valido = False
            if dni_viejo == dni_nuevo and nombre_viejo != nombre_nuevo:
                valido = False

    return valido

    
def validacionfinal(ventas):         
    dni = pedir_dni()
    edad = pedir_edad()
    nombre = pedir_nombre()
    comparacion = comparar_dni_nombre(ventas,dni,nombre)
    while comparacion == False:
        dni = pedir_dni()
        edad = pedir_edad()
        nombre = pedir_nombre()
    lista = [nombre,edad,dni]
    return lista

ventas = []
ventas.append(["0002", "maxumo", "34", "36536847", "2000"])


def recupero_ventas(archivo_ventas):
    ventas_str = " "
    tickets = []
    ventas_lineas = []
    try:
        archivo = open(archivo_ventas,"r")
        ventas_str = archivo.read()
        todas_las_lineas = ventas_str.splitlines()
        print("ventas lineas:",todas_las_lineas)
        for i in range(0, len(todas_las_lineas), 5):
            nuevo_ticket = []
            for j in range(5):
                nuevo_ticket.append(todas_las_lineas[i+j])
            ventas_lineas.append(nuevo_ticket)
        archivo.close()
        print("Ventas acá:",ventas_lineas)
    except IOError:
        print("No existe el archivo. Se va a crear.")
        archivo = open(archivo_ventas, "w")
        archivo.close()
    return ventas_lineas

def verificar_asiento (matriz):
    fila = int(input("Ingrese el numero de fila que desee: "))
    while fila < 0 or fila > 49:
        fila = int(input("ingrese una fila valida (entre 0 y 49):"))
    columna = int(input("En que columna quiere estar: "))
    while columna < 0 or columna > 49:
        columna = int(input("ingrese una columna valida (entre 0 y 49):"))
    asiento = matriz[fila-1][columna-1]
    while asiento == 1:
        fila = int(input("ingrese el numero de fila que desee: "))
        columna = int(input("En que columna quiere estar: "))
    lista =[fila,columna]

    return lista          

def cambiar_asientos(matriz,lista):
    for dato in lista:
        fila = lista[0]
        columna = lista[1]
    for i in range(len(matriz)):
        matriz[fila][columna] = 1
    return matriz

def asiento_str(lista):
    fila = lista[0]
    columna = lista[1]
    lista_str = "F" + str(fila) + "A" + str(columna)
    return lista_str

def crear_ticket(ventas):
    viejo_ticket = len(ventas)
    nuevo_ticket_num = int(viejo_ticket) + 1
    nuevo_ticket_str = ""

    if nuevo_ticket_num < 10:
        nuevo_ticket_str = "000" + str(nuevo_ticket_num)
    elif nuevo_ticket_num < 100:
        nuevo_ticket_str = "00" + str(nuevo_ticket_num)
    elif nuevo_ticket_num < 1000:
        nuevo_ticket_str = "0" + str(nuevo_ticket_num)
    else:
        nuevo_ticket_str = str(nuevo_ticket_num)

    return nuevo_ticket_str

def realizar_venta (ventas, asiento):
    venta = []
    ticket = crear_ticket(ventas)
    venta.append(ticket)
    print(ticket)
    print("Venta:",venta)
    print("Ventas:",ventas)
    validados = validacionfinal(ventas)
    print(validados)
    venta.append(validados[0])
    venta.append(validados[1])
    venta.append(validados[2])
    venta.append(asiento)
    
    return venta





def actualizar_ventas(archivo_ventas, ventas_actualizadas):
    archivo = open(archivo_ventas, 'w')

    for venta in ventas_actualizadas:
        print("Una venta es:", venta)
        for dato in venta:        
            archivo.write(dato)
            archivo.write("\n")
    archivo.close()
    return

def generar_ticket(lista,ventas):
    del(ventas[2])
    fila = int(lista[0])
    vip=0
    if fila <=25:
        precio = 20000
    else:
        precio = 15000


    ventas.append(precio)

    return ventas

asientos = recuperar_asientos("asientos.txt")
a = verificar_asiento(asientos)
b = cambiar_asientos(asientos,a)
c = asiento_str (a)
ventas = recupero_ventas("ventas.txt")
datos = realizar_venta(ventas, c) #Hasta aca realizo una venta con todos sus requisitos por eso ya abro el archivo
ventas+=[datos]
actualizar_ventas("ventas.txt", ventas) #Aca registro la venta en el archivo
ticket = generar_ticket(a,datos)
print(ticket)


def busqueda_nombre(archivo_ventas):
    nombre = input("ingrese su nombre por favor:")
    archivo = open(archivo_ventas, "r")
    print(type(archivo))
    for a in archivo:
        print(a)
        if nombre in a:
            posicion = a[4]
            print(posicion)
            print("usted tiene un asiento en:", posicion)
        else:
            print("usted no tiene ningun asiento" )
print(busqueda_nombre("ventas.txt"))

#6

def es_vip(archivo_ventas, asiento_str, precio):
    vip=0
    esvip=False
    while precio==20000:
        vip+=1
        esvip=True
        nombrevip=pedir_nombre

def ordenar_nombre(es_vip, pedir_edad):
    pass
    


def lista_vip(archivo_ventas, ordenar_nombre):
    listavip=[]
    for i in archivo_ventas:
        str_aux=""
        for j in i[3][1:]:
            if j!="A":
                str_aux+=j
            else:
                break
        if int(str_aux)<24:
            listavip.append(i)
    listavip=ordenar_nombre(listavip)
    return lista_vip

#7

def promedio_edad(archivo_ventas, pedir_edad, matriz, fila, columna):
    lista_dni=[]
    for i in archivo_ventas:
        if i[0] not in lista_dni:
            lista_dni.append(i[1])
    sumaedad=0
    cont=0
    for i in range(fila[0:25]):
        for j in range(columna[0:]):
            while matriz[i][j]==1:
                cont+=1
                pedir_edad+=sumaedad
            print("Promedio de edad sector VIP: ", sumaedad/cont, "años" )
    for i in range(fila[25:]):
        for j in range(columna[0:]):
            while matriz[i][j]==1:
                cont+=1
                pedir_edad+=sumaedad
            print("Promedio de edad sector general: ", sumaedad/cont, "años")
    return promedio_edad


#8
def buscar_ticket_perdido(ticket, nuevo_ticket_str):
    archivo=open("ticket_NÚMERO.txt", "r")
    numero=int(input("Ingrese su número de ticket: "))
    while numero<1 or numero>2500:
        numero=int(input("Ingrese un número válido: "))
    if numero not in archivo:
        print("Este ticket no fue vendido")
    for numero in archivo:
        archivo.write("ticket_NÚMERO,txt", "r")
    
#9
def suma_ventas(archivo_ventas, ventas, matriz, lista_dni, fila, columna):
    for i in archivo_ventas:
        if i[0] not in lista_dni:
            lista_dni.append(i[1])
    sumaventas=0
    for i in range(fila[0:]):
        for j in range(columna[0:]):
            while matriz[i][j]==1:
                ventas+=sumaventas
    print("Total recaudado: ", sumaventas, "$")

#10
def es_menor(pedir_edad, pedir_nombre, matriz):
    for i in matriz:
        if pedir_edad<21:
            nombre=pedir_nombre
        return nombre
def lista_menor():
    pass
#11

def menu():
    print(matriz_str)
    menu=int(input("Ingrese una opción del 1 al 11: "))
    while menu<1 or menu>12:
        menu=int(input("Opción no válida, pruebe de nuevo: "))
    if menu==11:
        print("Gracias por su consulta. Adiós")    
        archivo.close()       
    while menu>=1 and menu<=10:
        if menu==2:
            recuperar_asientos
        elif menu==3:
            validacionfinal
        elif menu==4:
            realizar_venta
        elif menu==5:
            busqueda_nombre
        elif menu==6:
            lista_vip
        elif menu==7:
            promedio_edad
        elif menu==8:
            buscar_ticket_perdido
        elif menu==9:
            suma_ventas
        else:
            lista_menor


menu()
    