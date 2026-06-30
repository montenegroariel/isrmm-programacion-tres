# Clase Persona
class Persona:

    
    cantidad_piernas = 2

    def __init__(self, fecha_nacimiento, genero, altura, peso):
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.altura = altura
        self.peso = peso

    
    def caminar(self):
        print("La persona está caminando")

    def hablar(self):
        print("La persona está hablando")

    def calcular_edad(self, anio_actual):
        edad = anio_actual - self.fecha_nacimiento
        return edad


# Clase Alumno
class Alumno(Persona):

    def __init__(self, fecha_nacimiento, genero, altura, peso, curso):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.curso = curso

    def asignar_curso(self, curso):
        self.curso = curso
        print("Curso asignado:", self.curso)


# Clase Profesor
class Profesor(Persona):

    def __init__(self, fecha_nacimiento, genero, altura, peso, materia):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.materia = materia

    def asignar_materia(self, materia):
        self.materia = materia
        print("Materia asignada:", self.materia)


# Crear un alumno
alumno1 = Alumno(2005, "Masculino", 1.75, 70, "3° Año")

alumno1.caminar()
alumno1.hablar()
print("Edad:", alumno1.calcular_edad(2026))
alumno1.asignar_curso("4° Año")


# Crear un profesor
profesor1 = Profesor(1980, "Femenino", 1.68, 65, "Matemática")

profesor1.caminar()
profesor1.hablar()
print("Edad:", profesor1.calcular_edad(2026))
profesor1.asignar_materia("Programación")