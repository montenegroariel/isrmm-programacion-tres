from abc import ABC, abstractmethod

# Definimos la clase abstracta heredando de ABC
class Vehiculo(ABC):
    
    def __init__(self, marca: str, modelo: str): # constructor
        self.marca = marca
        self.modelo = modelo
    
    # Un método normal que ya tiene funcionalidad
    def encender_electronica(self):
        return f"El sistema eléctrico de tu {self.marca} está listo."
    
    # Definimos un método abstracto (sin implementar)
    @abstractmethod
    def arrancar_motor(self):
        pass


class AutoGasolina(Vehiculo):
    def arrancar_motor(self):
        return f"El {self.marca} {self.modelo} hace: ¡Brum, brum! Motor de combustión encendido."

class AutoElectricot(Vehiculo):
    def arrancar_motor(self):
        return f"El {self.marca} {self.modelo} hace: ... (Silencio total). Motor eléctrico activo."

# No se puede crear un objeto de una clase abstracta
# mi_auto = Vehiculo('Ford', 'Mustang')

# Creamos los objetos reales
mi_auto = AutoGasolina("Ford", "Mustang")
mi_tesla = AutoElectricot("Tesla", "Model 3")

# Usamos el método común
print(mi_auto.encender_electronica()) 
# Resultado: El sistema eléctrico de tu Ford está listo.

# Usamos los métodos obligatorios (abstractos)
print(mi_auto.arrancar_motor())   # Resultado: ¡Brum, brum!...
print(mi_tesla.arrancar_motor())  # Resultado: ... (Silencio total)...