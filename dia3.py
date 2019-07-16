############## CONDICIONALES ##############
# == igual
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que
# != distinto o no igual

# Pregunta 1

a = 5
if a > 3:
    print("si, a es mayor a 3")
    print("chau!")
else:
    print("No, a no es mayor a 3")


nota = 47
if nota >= 60:
    print("Pasaste!!!")
else:
    print("Hule ya :)")



# Ej. Crear una funcion que reciba como parametro una
# nota de 1 al 100 e imprima si pasaste o te aplazaste (se aprueba con 61)

nota = 78
def suma_nota(nota_a):
    if nota_a >= 61:
        print("Aprobado.!!!")
    else:
        print("Reprobado")
suma_nota(nota)

######
nota = 56                      #esta es la nota del alumno
def suma_nota(nota_a):          #con el def se crea un variable para guardar o almacenar informacion
    if nota_a >= 61:            #el if funciona para saber o comparar si es mayor o menor o viseversa
        print("Aprobaste.!!!")     #print dentro de if para imprimir el resultado de las comparaciones
    else:                           #else es para si NO es mayor 
        print("Reprobaste :)")      #print dentro de ELSE es para imprimir el dato
suma_nota(nota)                     #llamada de la funcion para poder pasar la informacion guardada en el variable de suma_nota


a = 6
if a > 5 and a < 10:
    print("a es mayor a 5 y menor a 10")
else:
    print("a no es mayor a 5 y menor a 10")

######

a = 3
if a > 5 and a < 10:
    print("a es mayor a 5 y menor a 10")
else:
    print("a no es mayor a 5 y menor a 10")

######

a = 7
if a > 5 and a < 10 and a != 7:
    print("a es mayor a 5 y menor a 10 y distinto que 7")
else:
    print("a no esta en el rango, alguna de las 3 condiciones no se cumplieron")

#######
a = 7
if a > 5 or a < 10:
    print("a es mayor a 5 o menor a 10")
else:
    print("a no es mayor que 5 ni menor a 10")

a = 6
if a > 5 or a < 10:
    print("a es mayor a 5 o menor a 10")
else:
    print("a no es mayor que 5 ni menor a 10")

############ CONDICIONALES ##########
False
True
print(7>4)
print(7<4)

edad = 7

if edad > 18:
    print("Deberia estar en la univercidad")
elif edad > 13:
    print("Deberia estar en la secundaria")
elif edad > 6:
    print("Deberia estar en la primaria")
else:
    print("Deberia estar en su cuna")

#Anidado
if edad > 18:
    print("Univercidad")
else:
    if edad > 13:
        print("Secundaria")
    else:
        if edad > 6:
            print("primaria")
        else:
            print("bbdlc")
# Practica

edad = 22
if edad > 20:
    print("Univercidad")
else:
    if edad > 15:
        print("Secundaria")
    else:
        if edad > 8:
            print("primaria")
        else:
            print("bbdlc")


#Ej. Crear una funcion puntaje que reciba como parametro una nota
# del 1 al 100 e imprima que nota sacaste
# nota < 60         ----->1
# nota entre 60 y 70 ---->2
# nota entre 71 y 75 ---->3
# nota entre 76 y 85 ---->4
# nota mayor que 85 ----->5

def cal_final(nota):
    if nota <= 60:
        print("cal_f. 1")
        return 1
    elif nota < 70:
        print("cali_f. 2")
        return 2
    elif nota < 75:
        print("Cali_f. 3")
        return 3
    elif nota >= 76:
        print("Cal_f. 4")
        return 4
    elif nota >=85:
        print("Cal_f. 5")
        return 5

cal_final(80)
    
#####
def paso_examen(nota):
    if nota >= 35:
        return True
    elif nota < 31:
        return True
    elif nota < 27:
        return True
    elif nota < 24:
        return True
    elif nota > 21:
        return False

print(paso_examen(3))

nota = cal_final(27)

if paso_examen(nota) == True:
    print("Felicitaciones pasaste")
else:
    print("Te aplazaste")


#nombre = input("Ingresa tu nombre: ")
#print("Hola", nombre)

edad = 27
print("Tenes" + str(edad))
saludo = "cordial"
print(saludo)

# Ej. Pedir al usuario que ingrese tres numeros y multiplicarlos
# entre si, imprimir el resultado


# numero1 = input("Dame un numero")
# numero2 = input("dame otro numero")
# numero3 = input("otro mas")

# producto = int(numero1)*int(numero2)*int(numero3)
# print(producto)

# Ej. Pedir al usuario un numero del 1 al 100 y llamar a la 
# funcion que retornaba la nota que creamos hace rato 
# utilizando el valor ingresado por el usuario





######### Bucle while == Mientras #####

# x = 0
# while x != 5:
#     print("Hola esto es un bucle while")
#     x = int(input("ingresa un numero:"))
#     print("El valor de x es", x)
# print("Termino")


# contador = 0

# while contador < 10:
#     print("Sigo en el bucle while")
#     contador = contador + 1
#     print("Se repitio", contador, "veces")


# contador = 10

# while contador > 0:
#     print("Sigo en el bucle while")
#     contador = contador - 1
#     print("Te quedan", contador, "oportunidades")


# Usando while pedir al usuario 5 ingredientes para hacer una pizza
# y agregar a una lista al final

# ingr_pizza = 0                      # Inicializamos la compra en 0
# ing_lista = []                       # Creamos una lista 
# while ingrediente < 5:
#     print("Ingrediente")
#     ingre_num = ("agrega un ingrediente: ")
#     ing_lista.append(input(ingre_num))
#     ingrediente = ingrediente + 1
# print("los ingredientes son:", ing_lista)


# Adivinanza
#numero_secreto = 7

# adivino = False

# while adivino == False:
#     apuesta = input("Adivina el numero secreto:")
#     if int(apuesta) == numero_secreto:
#         print("GANASTE!!!")
#         adivino = True
#     else:
#         print("Perdeu Maiky")

# Ej. Crear un juego de adivinar el nummero como el de arriba y
# darle pista al usuario si el numero que ingreso es mayor o menor
# al numero de adivinar 
# pista usar elif

numero_secreto = 45
adivino = True

while adivino == True:
    apuesta = input("Adivina el numero secreto:")
    if int(apuesta) == numero_secreto:
        print("Ganaste")
        adivino = False
    elif int(apuesta) > numero_secreto:
        print("el numero ingrsado es mayor que numero secreto")
    elif int(apuesta) < numero_secreto:
        print("el numero ingresado es menor que numero secreto")

# DESAFIO
# Ej.2 Buscar como gener un numero aleatorio para numero_secreto

numero_secreto = 20
prova = False

while prova == True:
    prova = input("Adivina el numero secreto:" )
    if int(prova) == numero_secreto:
        print("ADJUDICADO")
        prova = True
    elif int(prova) > numero_secreto:
        print("has Ganado")
    elif int(prova) < numero_secreto:
        print("has Perdido")

