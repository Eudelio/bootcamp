############## RoDI ################

import rodi
import time

robot = rodi.RoDI()                 #Instanciamos un objeto RoDI

# #robot.move_forward()                # mueve hacia adelante
# #time.sleep(1)                       # queda haciendo lo anterior por un segundo
# #robot.move_backward()               # mueve el robot para atras
# #time.sleep(2)                       # mueve el robot para atras por el S" indicado
# #robot.move_left()                   # hace un giro hacia la hizquierda
# #time.sleep(0.5)                     # hace el giro a la hizquierda por (0.5 S)
# #robot.move_right()                  # gira el robot para atras
# #time.sleep(0.5)                     # queda girando el robot por el S" indicado
# #robot.move_stop()


# # Ejercicio
# # Hacer que el robot haga un cuadro

# import rodi
# import time

# robot = rodi.RoDI()

# robot.move_forward()
# time.sleep(3)
# robot.move_left()
# time.sleep(0.50)
# robot.move_forward()
# time.sleep(3)
# robot.move_left()
# time.sleep(0.50)
# robot.move_forward()
# time.sleep(3)
# robot.move_left()
# time.sleep(0.50)
# robot.move_forward()
# time.sleep(3)
# robot.move_stop()

# ############

# # Ejercicio 2:
# # Dibujar un cuadrado utilizando menos lineas de codigo

# for movimiento in range(4):
#     robot.move_forward()
#     time.sleep(2)
#     robot.move_left()
#     time.sleep(0.5)
#     robot.move_stop()


# contador = 0                        # Contador empieza en 0 
# while contador <= 3:                # mientras contador sea menor o igual a 3 se va a ejecutar la funcion
#     contador = contador + 1         # contador empieza en 0 y va sumando hasta alcanzar la cantidad que le pedimos
#     robot.move_forward()            # mueve el robot hacia delante
#     time.sleep(2)                   # controla el tiempo que el Robot se mueve
#     robot.move_stop()               # para el robot
#     robot.move_left()               # 
#     time.sleep(0.5)
#     robot.move_stop()



#----------#
# Sensor de distancia

print(robot.see(), "Centimetros")

# distancia = 5
# while distancia == 5:
#     print(robot.see(), "Centimetros")

# while True:
#     print(robot.see(), "Centimetros")
#     robot.move_forward()

# try:                               # Intentar esto
#     while True:
#        print(robot.see(), "Centimetros")  # imprimimos la distancia recorrida por rodi
#        robot.move_forward()                # mover el robot hacia adelante

# except KeyboardInterrupt:           #exepto cuando hay una interrupcion por teclado
#      print("Finalizado")            
#      robot.move_stop()             # al apretar Ctrl+C para el robot


# Ejercicio utilizando un While True (bucle indefinido)
# hacer que RoDI avance si no encuentra un obstaculo en frente
distancia = True
# try:
#     while distancia == True:
#         print(robot.see(), "Centimetros")
#         if robot.see() > 10:
#             robot.move_forward()
#         else:
#             robot.move_stop()
#         if robot.see() == 15:
#             robot.move_right()
#             time.sleep(0.5)
#         else:
#             robot.move_stop()
#         if robot.see() <= 15:
#             robot.move_backward()
#             time.sleep(2)
#         else:
#             robot.move_stop()

# except KeyboardInterrupt:
#      print("Finalizado")            
#      robot.move_stop()  

#robot.move(50,50)   # hace que el robot reduzaca la velocidad

# Ejercicio Hacer que el robot siga un objeto. (pista: similar al anterior)

#  distancia = True
#  try:
#      while distancia == True:
#          for x in range(100):
#              robot.pixel(x,0,0)
#              time.sleep(0.1)
#              robot.pixel(0,x,0)
#              time.sleep(0.1)
#              robot.pixel(0,0,x)
#              time.sleep(0.1)
#          print(robot.see(), "Centimetros")
#          if robot.see() > 10:
#              robot.move_right()
#          if robot.see() < 10:
#              robot.move_forward()
#          else:
#              robot.move_stop()
#  except KeyboardInterrupt:
#       print("Finalizado")            
#       robot.move_stop()

# Desafio: hacer que el led de RoDI se prenta
# mostrando los colores del arcoiris

#  while True:
#      print(robot.light())            # sensor de luz de RoDI, muestra la cantidad
#                                       # de luz que detecta en el ambiente
#      time.sleep(0.5)
#      robot.sing(800,900)

# Seguidor de linea

while True:
    linea = robot.sense()               # lee ambos sensores y los almacena en una linea
    print(linea)                        
    print(linea[0])                     # lee el valor del sensor de la isquierda
    print(linea[1])                     # lee el valor del sensor de la derecha
    time.sleep(0.5)



