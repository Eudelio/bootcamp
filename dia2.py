#Tipo de dato String/cadena/str de texto
"Esto es un String"
#Tipo de dato Integer/Entero/int
105
#Listas
#Lista Vacia
["Marce", 33, "Programador"] #Lista de 3 elementos
#Variables
nombre = "Marce"
edad = 30+3
edad_mal = "30+3"
variable_lista = ["Hola", nombre, 99]
#Acceder a un elemento de la Lista
print(variable_lista [0], edad, variable_lista [2] )
#Acciones/operaciones sobre listas
variable_lista.append("rugby") #agregar elemento a lista al final

variable_lista [2] = 50
print(variable_lista [2])

print (variable_lista)

#Bucles / Loop Ciclos
#Imprimir cada elemento de una lista
for loquesea in variable_lista:
    print(loquesea)


# Imprimir los numeros del 1 al 10
for cualquiercosa in range(10):
    for cualquiercosa in range(1,11):
        print(cualquiercosa + 1)
        print (cualquiercosa)
# Imprimir el ultimo elemento de una lista sin saber cuantos
# Elementos tiene, solucion general
otra_lista = [5, "Hola que tal", "Chau", 4]
otra_lista.append("AAAA")
print(otra_lista)
print(otra_lista [len(otra_lista)-1])
dim_lista = len(otra_lista)
print("-------------------")
print("La dimension de otra_lista", dim_lista)
indice_del_ultimo = dim_lista - 1
print("El indice del ultimo elemento es", indice_del_ultimo)



print(otra_lista[indice_del_ultimo])




#Solucion de una linea 

print(otra_lista[len(otra_lista)-1])

#esto es equivalente
for numero in range(1,11):
    print(numero)
# a esto
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print(numero)
# imprimir Hola 10 veces
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print("Hola", numero) #imprimir numero es opcional

#imprimir el numero de resultado de la suma de los numeros
#del 1 al 10 -> 55
#acumuladores 
challenge=[1,2,3,4,5,6,7,8,9,10]  #se crea una lista
a=0                                #se crea una variable de base
for x in challenge:           #se crea un ciclo que va a correr la 
    a=a+x                      #se va acumulando las sumas parciales

print(a)

sumatoria=0          #variable inicializada en cero
for valor in range(1,11):
    sumatoria=sumatoria + valor
print(sumatoria)

########## FUNCIONES ##########

#def nombre_de_la_funcion(argumento):
def suma(num1, num2):
    resultado = num1+num2
    return resultado

#Equivalente a la de arriba
def suma2(num1, num2):
    return num1 + num2

print (suma(5,10))
resul = suma (5,8)
print(resul)

# Crear una funcion resta, que reciba como parametro dos numeros
# y retorne la resta de esos numeros
# luego llamar a la funcion e imprimir el resultado

def resta(num1, num2):
    resultado = num1-num2
    return resultado

print(resta(6,12))

# Crear una funcion saludo2 que reciba como parametro nombre y edad
# e imprime "hola soy____ y tengo____ anhos"
# llamar varias veces a la funcion con distintos valores
# Nota: retornar algo es opcionanal


def saludo2(nombre, edad):
    print("Hola soy", nombre, "y tengo", edad, "anhos")
saludo2("Claudio",36)

# Ej. Crear una funcion suma_lista que reciba como argumento una lista de numero
# lista de numero y retorne la suma de sus elementos
# Pista: usar for y una variable acumulador

listita = [1,2,3,4,5] #1+2+3+4+5=15

def suma_lista(serio):          #esta parte se agrupa dentro de
    suma1 = 0
    for x in serio:
        suma1 = suma1+x
    return suma1
argumento = suma_lista(listita)
print(argumento)

listota = [100,5,5]             #el valor de de retorno seria 110

# Pista 2, la llamada deberia ser:
#suma_lista(listita)
#suma_lista(listota)

# Ej.2 lista al cuadrado
# Crear una funcion que reciba una lista de numero como parametro
# y retorne una lista con los numeros al cuadrado
# lista_cuadrado(listita)   --> [1,4,9,16,25]


def lista_cuadrada(entrada):
    a = []
    for x in entrada:
        a.append(x * x)
    return a
entrada = [1,4,9,16,25]
argumento = lista_cuadrada(entrada)
print(argumento)

def lista_cuadrada(vista1):                     #cree este ejercicio
    a = []
    for vista3 in vista1:
        a.append(vista3 * vista3)
    return a
vista1 = [4,6,8,10,20]
creador = lista_cuadrada(vista1)
print(creador)

#####################

# Ej. eliminar todos los elementos de una lista utilizando "for"

grupo5 = ["N","F1","F2","A"]
print("antes"),grupo5
for j in range(len(grupo5)):
    grupo5.pop ()
print("despues",grupo5)

# Crear una funcion de suma_cuadrado que reciba una lista de numeros
# y retorne el valor de la suma de cada numero al cuadrado
# [1,2,3,4] --> 1+4+9+16 -> 30

lista_libro = [1,2,3,4]

def suma_cuadrada(lista_l):
    suma = 0
    for lista1 in lista_l:
        suma = suma + (lista1* lista1)
        return suma
print(suma_cuadrado())


def suma_cuadrada(visto1):
    a = []
    for visto2 in visto1:
        a.append(visto2)
    return a
visto3 = [1+4+9+16]
visto4 = suma_cuadrada(visto3)
print(visto4)

 #############

ingr_pan = ["harina","levadura","sal","azucar","agua"]
def impr_lista(ingredientes):
    for producto in ingredientes:
        print(producto)
impr_lista(ingr_pan)

############

