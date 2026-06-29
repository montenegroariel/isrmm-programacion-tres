from datetime import date


class Persona:
    from datetime import date
    piernas = 2
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
        fecha_hoy = date.today()
        edad = fecha_hoy.year - self.fecha_nacimiento.year
        if (fecha_hoy.month, fecha_hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad

class Alumno(Persona):
    def __init__(self, fecha_nacimiento, genero, altura, peso, curso):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.curso = curso

    def asignar_curso(self, curso):
        self.curso = curso


class Profesor(Persona):
    def __init__(self, fecha_nacimiento, genero, altura, peso, materia):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.materia = materia

    def asignar_materia(self, materia):
        self.materia = materia



