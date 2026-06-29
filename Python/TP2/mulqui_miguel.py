from datetime import date

class persona:
    cantidad_de_piernas = 2

    def __init__(self,fecha_nacimiento,genero,altura,peso):
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.altura = altura
        self.peso = peso

    def caminar(self):
        print("La persona empezo a caminar")

    def hablar(self):
        print("La persona comenzo a hablar")

    def calcular_edad(self):
        fecha_hoy = date.today()
        edad = fecha_hoy.year - self.fecha_nacimiento.year
        if (fecha_hoy.month, fecha_hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad
    
class alumno(persona):

    def __init__(self, fecha_nacimiento, genero, altura, peso, curso):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.curso = curso

    def asignar_curso(self,curso):
        self.curso = curso

class profesor(persona):
    def __init__(self, fecha_nacimiento, genero, altura, peso, materia):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.materia = materia

    def asignar_materia(self,materia):
        self.materia = materia