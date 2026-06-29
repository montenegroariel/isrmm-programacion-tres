

class Persona:
    cantidad_de_piernas = 2  # atributo de clase

    def __init__(self, fecha_nacimiento, genero, altura, peso):
        self.fecha_nacimiento = fecha_nacimiento  # debe ser un objeto date
        self.genero = genero
        self.altura = altura
        self.peso = peso

    def caminar(self):
        print(f'{self.genero} está caminando')

    def hablar(self):
        print('Hablando...')

    def calcular_edad(self):
        hoy = date.today() # date no esta importado, va a dar error
        edad = hoy.year - self.fecha_nacimiento.year - (
            (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )
        print(f'Tiene {edad} años')
        return edad


class Alumno(Persona):
    def __init__(self, fecha_nacimiento, genero, altura, peso, curso):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.curso = curso

    def asignar_curso(self, nuevo_curso):
        self.curso = nuevo_curso
        print(f'Se asignó el curso {self.curso}')


class Profesor(Persona):
    def __init__(self, fecha_nacimiento, genero, altura, peso, materia):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.materia = materia

    def asignar_materia(self, nueva_materia):
        self.materia = nueva_materia
        print(f'Se asignó la materia {self.materia}')
