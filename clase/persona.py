
class Persona:                          # Definimos la clase, una receta para crear un objeto
                                        # o tambien la clase es la plantilla
    edad = 0   
    #nacionalidad = "brasil"               # Atributo de clase o propiedad de lo que vamos a crear
    def __init__(self, un_nombre):      # Metodo constructor __init__
                                        # metodos--> funciones dentro de una clase
        self.mi_nombre = un_nombre      # usamos self para referirnos al objeto mismo
        print("Hola naci, me llamo", self.mi_nombre)        #print opcional
    def cumple(self):                   # cumple es un metodo de la clase persona
        self.edad = self.edad + 1       # que aumenta la propiedad edad en 1
    
    def asignar_edad(seld, una_edad):    # asignar edad es un metodo que recibe un argumento numerico
                                        # y asigna a la propiedad edad del objeto
        self.edad = una_edad 
        print(self.edad)                 # pepe es un objeto de clase animal, perro es un objeto de clase animal
    
    def asig_n(self, una_nacionalidad):
        self.nacionalidad = una_nacionalidad
        print("ahora mi nacionalidad es",self.nacionalidad)
    def saludo (self):
        print("Hola soy", self.mi_nombre, "y mi nacionalidad es", self.nacionalidad)
    
pepe = Persona("Robert")
pepa = Persona("Claudia")
print(pepe.edad)
print(pepe.mi_nombre)

#print(pepa.nacionalidad)           # este me inprime la nacionalidad asignada por def
pepa.asig_n("Paraguaya")            # 
print(pepa.nacionalidad)

pepe.cumple()
print(pepe.edad)
print(pepa.mi_nombre)
pepa.cumple()
print(pepa.edad)

pepe.asig_n("Uruguaya")
pepe.saludo()

# Ej. agregar un metodo a la clase persona que asigne una nacionalidad y otro
# metodo saludar que imprima "hola soy ___ y mi nacionalidad es ___"
# Crear un objeto persona, y asignarle una nacionalidad y acerle saludar


    