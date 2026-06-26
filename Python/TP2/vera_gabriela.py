from datetime import date

class Persona:

    cantidad_de_piernas = 2

    def __init__(self, fecha_nacimiento, genero, altura, peso):
        self.fecha_nacimiento = fecha_nacimiento 
        self.genero           = genero            
        self.altura           = altura           
        self.peso             = peso              

    def caminar(self):
        print(f"{self} está caminando.")

    def hablar(self):
        print(f"{self} está hablando.")

    def calcular_edad(self):
        hoy = date.today()
        nacimiento = date.fromisoformat(self.fecha_nacimiento)
        edad = hoy.year - nacimiento.year
        if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
            edad -= 1
        print(f"Edad: {edad} años")
        return edad


class Alumno(Persona):

    def __init__(self, fecha_nacimiento, genero, altura, peso):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.curso = None   

    def asignar_curso(self, curso):
        self.curso = curso
        print(f"Curso asignado: {self.curso}")


class Profesor(Persona):

    def __init__(self, fecha_nacimiento, genero, altura, peso):
        super().__init__(fecha_nacimiento, genero, altura, peso)
        self.materia = None

    def asignar_materia(self, materia):
        self.materia = materia
        print(f"Materia asignada: {self.materia}")


