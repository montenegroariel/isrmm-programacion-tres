from datetime import date

class Persona:
    cantidad_piernas = 2 

    def __init__(self, fecha_nacimiento, genero, altura, peso):
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.altura = altura
        self.peso = peso 

    def caminar(self):
        print("estoy caminando")

    def hablar(self):
        print("estoy hablando")

    def calcular_edad(self):
        hoy = date.today()
        nacimiento = self.fecha_nacimiento

        edad = hoy.year - nacimiento.year
        if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
            edad -= 1

        return edad

        
class Alumno (Persona):
    def __init__(self, fecha_nacimiento, genero, altura, peso, curso=None):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.curso = curso
    
    def asignar_curso(self, curso):
        self.curso = curso

class Profesor (Persona):
    def __init__(self, fecha_nacimiento, genero, altura, peso, materia=None):
        super().__init__(fecha_nacimiento,genero, altura, peso)
        self.materia = materia

    def asignar_materia(self, materia):
        self.materia = materia

    




