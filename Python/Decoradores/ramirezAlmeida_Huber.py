def decorador_alumno(funcion):

        def decorador(self, curso):
            print("Bienvenido")
            funcion(self, curso)
            print("El curso se asignó de forma correcta")


        return decorador
        



def decorador_profesor(funcion):

        def decorador(self, curso):
            if type(curso) == str:
                funcion(self, curso)
            else:
                print("Curso no es un STRING.")


        return decorador
            


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
    def __init__(self, anio_nacimiento, peso, genero, altura, curso):
        Persona.__init__(self, anio_nacimiento, peso, genero, altura)
        self.curso = curso  



    def asignar(self, curso_nuevo):
        self.curso = curso_nuevo
        print(f"El curso del alumno es '{self.curso}'")


    @decorador_alumno
    def asignar_curso(self, curso):
        self.curso = curso 
        print("El curso del alumno es: ", self.curso)
   






class Profesor(Persona):
    def __init__(self, anio_nacimiento, peso, genero, altura, materia, curso):
        Persona.__init__(self, anio_nacimiento, peso, genero, altura)
        self.materia = materia  
        self.curso = curso



    def asignar_materia(self, materia_nueva):
        self.materia = materia_nueva
        print(f"La materia es '{self.materia}'")



    @decorador_profesor
    def asignar_curso(self,curso):
        self.curso = curso
        print("El curso del profesor es: ", self.curso)

