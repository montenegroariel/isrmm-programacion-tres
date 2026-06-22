class Animal:

    def __init__(self, edad, color): # constructor
        self.edad = edad
        self.color = color

    def nacer(self): # metodo instance
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')

class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo
        
    def hablar(self):
        print("pio")

    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')

print(Pajaro.__bases__) # muestra de que clase hereda

print(Animal.__subclasses__()) # muestra las clases que heredan

piolin = Pajaro(3,'amarillo', 60)
mi_animal = Animal(5, 'negro')

# llamar metodos
piolin.hablar()
piolin.volar(10)