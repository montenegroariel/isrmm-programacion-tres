class Persona:
   
    cantidad_piernas = 2


    def __init__(self, fecha_nacimiento, peso, genero, altura):
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self.genero = genero
        self.altura = altura


    def hablar(self):
        print("La persona habla")


    def caminar(self):
        print("La persona camina")


    def calcular_edad(self, anio_actual):
        edad = anio_actual - self.fecha_nacimiento
        print(f"La persona tiene: {edad} años")
        return edad







class Alumno(Persona):
    def __init__(self, anio_nacimiento, peso, altura, genero, curso):
        Persona.__init__(self, anio_nacimiento, peso, altura, genero)
        self.curso = curso  



    def asignar_curso(self, curso_nuevo):
        self.curso = curso_nuevo
        print(f"El curso del alumno es '{self.curso}'")






class Profesor(Persona):
    def __init__(self, anio_nacimiento, peso, altura, genero, materia):
        Persona.__init__(self, anio_nacimiento, peso, altura, genero)
        self.materia = materia  



    def asignar_materia(self, materia_nueva):
        self.materia = materia_nueva
        print(f"La materia es '{self.materia}'")
