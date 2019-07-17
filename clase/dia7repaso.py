class Animal(Dino):
    vivo = False
    def __init__(self):
        self.vivo = True
    
    def esta_vivo(self):
        if self.vivo == True:
            print("Estoy vivo")
        else:
            self.vivo == False
            print(eh_morido)

class Dino:
    ojos = 2
    patas = 4
    def __init__(self, un_nombre, un_color, patas, un_genero):
        self.nombre = un_nombre
        self.color = un_color
        self.genero = un_genero
        print("Naci")
    def saludar(self):
        print("Hola me llamo", self.nombre, "tengo", self.patas, "patas y soy", self.color)

    def cortar_patas(self, cantidad_de_patas_acortar=1):
         self.patas = self.patas - cantidad_de_patas_acortar
    
    def decir_genero(self):
         print("Hola soy", self.nombre, "y me identifico como", self.genero)

pepe = Dino("Pepito", "Verde", 4, "Macho")
print(pepe.nombre)
pepe.cortar_patas()
pepe.saludar()
pepe.decir_genero()

pepa = Dino("Pepita", "Rosa", 2, "Hembra")
print(pepa.nombre)
pepa.cortar_patas()
pepa.saludar()
pepa.decir_genero()

class TRex(Dino):
    def __init__(self, nombre, patas, color=None)
    self.nombre = nombre
    self.patas = patas
    self.color = color
    print("Hola soy TRex y me llamo", self.nombre)

pepeT = TRex("Roberto el TREX")
print(robert.ojos)

robert.saludar()
robert.decir_genero()

robert.esta_vivo()








