import RPi.GPIO as gpio #LIBRERIA PARA UTILIZAR LOS PUERTOS DE LIBRERIA
from time import sleep # ES PARA DAR PAUSA
led1 = 23               # definimos los pines de GPIO a utilizar
led2 = 24
led3 = 25
gpio.setmode(gpio.BCM) 
# modo BCM de la raspberry pi(Broadcom SOC channel)
gpio.setup(led1,gpio.OUT)
gpio.setup(led2,gpio.OUT)
gpio.setup(led3,gpio.OUT)

# coniguramos los puertos conectados a los leds como salida
while True:                     #bucle infinito
	gpio.output(led1,True)      # encendemos el led                 # pausa un segundo
	gpio.output(led2,True)    # apagamos el led                    # pausa de un segundo
	gpio.output(led3,True)
	sleep(0.5)
	gpio.output(led1,False)
	gpio.output(led2,False)
	gpio.output(led3,False)
	sleep(0.5)


# Ejercicio:
# hacer que los tres leds parpaden todos juntos con un intervalo
# de 0.5 segundos
# pista:     led2 = 24
#	         led3 = 25


###############################

import RPi.GPIO as gpio
from time import sleep

led1 = 23
led2 = 24
led3 = 25
gpio.setmode(gpio.BCM)
gpio.setup(led1,gpio.OUT)
gpio.setup(led2,gpio.OUT)
gpio.setup(led3,gpio.OUT)
"""while True:
	gpio.output(led1,True)
	sleep(1)
	gpio.output(led2,True)
	sleep(1)
	gpio.output(led3,True)
	sleep(1)
	gpio.output(led1,False)
	sleep(1)
	gpio.output(led2,False)
	sleep(1)
	gpio.output(led3,False)
	sleep(1) """

lista_c = [led1,led2,led3]    # Creamos una lista
while True:						# iniciamos un siclo interminable
	for encender in lista_c:   # 
		gpio.output(encender,True)
		sleep(0.5)
	for encender in lista_c:
		gpio.output(encender,False)
		sleep(1)
############################
from time import sleep
import Adafruit_DHT as dht
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)

def DHT11_data():
	humi , temp=dht.read_retry(dht.DHT11. 18)
	return humi, temp
while True:
	try:
		humedad, temperatura=DTH11_data()
		if humedad is not None and temperatura is not None:
			print("Humedad": ",Humedad "Temperatura":, "Temperatura)
		else:
			print("Error a la temperatura del sensor")
		sleep(20)
	except KeyboardInterrupt:
		gpio.cleanut()
		print("Programa Terminado")
		break
##########################################