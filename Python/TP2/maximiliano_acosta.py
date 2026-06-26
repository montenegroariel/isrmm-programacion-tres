class Persona:
    Cantidad_de_Piernas = 2

    def __init__(self, fecha_nacimiento, genero, altura, peso):
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.altura = altura
        self.peso = peso

    def caminar(self):
        print("esta persona esta caminando tranqui")

    def hablar(self):
        print("La persona está hablando")

    def calcular_edad(self, año_actual):
        # aca borra los 2 primeros valores de una fecha formato dd/mm/yyyy y deja solo año
        año_nacimiento = int(self.fecha_nacimiento.split("/")[2])
        edad = año_actual - año_nacimiento
        return edad


class Alumno(Persona):
    def __init__(self, fecha_nacimiento, genero, altura, peso, curso):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.curso = curso

    def asignar_curso(self, nuevo_curso):
        self.curso = nuevo_curso
        print(f"Curso asignado: {self.curso}")


class Profesor(Persona):
    def __init__(self, fecha_nacimiento, genero, altura, peso, materia):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.materia = materia

    def asignar_materia(self, nueva_materia):
        self.materia = nueva_materia
        print(f"Materia asignada: {self.materia}")