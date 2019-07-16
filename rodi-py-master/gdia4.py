
import rodi
import time
from random import randint
robot = rodi.RoDI()

distancia = True
try:
    while True:
        linea = robot.sense()
        print(linea)
        print(linea[0])
        print(linea[1])
        if linea[0] < 10     and linea[1] < 10:           # Significa que esta adentro
            robot.move_forward()
        elif linea[0] < 10 and linea[1] < 10:                                            # esta por salir
            robot.move_backward()
            time.sleep(0.5)       
        elif robot.see() < 10:
            robot.move_stop()
            robot.move_right()
        elif robot.see() <10:
            robot.move_forward()

        
        x=randint(0,255)
        robot.pixel(x,0,0)
        time.sleep(0.01)
        robot.pixel(0,x,0)
        time.sleep(0.01)
        robot.pixel(0,0,x)
        time.sleep(0.01)
        print(robot.see(), "centimetro")
        
except KeyboardInterrupt:
    print("PARA LOCO")
    robot.move_stop()

#while True:

#  print(linea[0.5])
