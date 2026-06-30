from datetime import date

class Persona:
    cantidad_de_piernas = 2

    def __init__(self, fecha_nacimiento, genero, altura, peso):
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.altura = altura
        self.peso = peso

    def __str__(self):
        return (f"Género: {self.genero}, "
                f"Altura: {self.altura} m, "
                f"Peso: {self.peso} kg")

    def caminar(self):
        return "La persona está caminando."

    def hablar(self, mensaje="Hola"):
        return f'La persona dice: "{mensaje}"'

    def calcular_edad(self):
        hoy = date.today()

        edad = hoy.year - self.fecha_nacimiento.year - (
            (hoy.month, hoy.day) <
            (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )

        return edad


class Alumno(Persona):

    def __init__(self, fecha_nacimiento, genero, altura, peso):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.curso = None

    def asignar_curso(self, nuevo_curso):
        self.curso = nuevo_curso
        return f"Curso '{self.curso}' asignado correctamente."


class Profesor(Persona):

    def __init__(self, fecha_nacimiento, genero, altura, peso):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.materia = None

    def asignar_materia(self, nueva_materia):
        self.materia = nueva_materia
        return f"Materia '{self.materia}' asignada correctamente."




