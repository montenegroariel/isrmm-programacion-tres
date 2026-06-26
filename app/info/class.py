class Auto:

    ruedas = 4 #MD5

    def __init__(self, color, marca): # constructor
        self.color = color
        self.marca = marca

    def acelerar(self, km): # metodo instance
        print(f'el auto acelera a {km} km')

    def pintar(self, color_elegido):
        self.color = color_elegido
        print(f'Ahora el auto es {self.color}')

    @classmethod
    def poner_ruedas(cls, cantidad): # metodo clase
        print(f'Puso {cantidad} ruedas')
        cls.ruedas = 5

    @staticmethod # El metodo estatico no modifica atributos
    def tocar_bocina(): # metodo estatico
        print('BEEP BEEP')

ferrari = Auto('rojo', 'Ferrari') # Instanciar a una clase
ferrari.acelerar(200)
ferrari.pintar('azul')
Auto.poner_ruedas(4)
fiat = Auto('verde','Fiat')
Auto.tocar_bocina()
print(Auto.ruedas)