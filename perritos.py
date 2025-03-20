class perro():
   # nombre = "Pingo el Dios de la Destrucción"
   # edad = 8
   # raza = "labrador"
   # color = "negro"

    def __init__(self, nombre, edad, raza, color): #privado, variables globales#
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.color = color
    def comer(self):
        print(self.nombre, "está comiendo")

    def dormir(self):
        print(self.nombre, "está jugando")

#dog = perro()
#dog.comer()

perro_1 = perro("Pingo", 8, "Labrador", "Negro")
perro_2 =perro("Beyli", 6, "Chihuahua", "Café")

perro_1.comer()
perro_2.dormir()

