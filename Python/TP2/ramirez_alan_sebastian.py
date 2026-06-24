from datetime import date

class Persona:
    cantidad_de_piernas = 2

    def __init__(self, fecha_nacimiento, genero, altura, peso):
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.altura = altura
        self.peso = peso

    def caminar(self):
        pass

    def hablar(self):
        pass

    def calcular_edad(self):
        hoy = date.today()
        anyo, mes, dia = map(int, self.fecha_nacimiento.split("-"))
        return hoy.year - anyo - ((hoy.month, hoy.day) < (mes, dia))

class Alumno(Persona):
    def __init__(self, fecha_nacimiento, genero, altura, peso, curso=None):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.curso = curso

    def asignar_curso(self, curso):
        self.curso = curso

class Profesor(Persona):
    def __init__(self, fecha_nacimiento, genero, altura, peso, materia=None):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.materia = materia

    def asignar_materia(self, materia):
        self.materia = materia

#a = Alumno("2005-05-15", "Masculino", 1.75, 70)
#a.asignar_curso("Matemáticas")
#print(a.curso)
#p = Persona("1990-03-10", "Femenino", 1.65, 60)
#print(p.calcular_edad())
