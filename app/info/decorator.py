def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

#mayuscula('Hola')
#minuscula('Hola')

# Queremos agregar el texto "Bienvenido" al principio y "Adios" al final.

def mayuscula(texto): # Esto altera la funcion original y es poco practico
    print('Bienvenido')
    print(texto.upper())
    print('Adios')

def minuscula(texto):
    print(texto.lower())

#mayuscula('Hola')

# Pasar una funcion como parametro
def decorador(funcion):
    def saludo(palabra, encoding):
        print('Bienvenido')
        funcion(palabra, encoding)
        print('Adios')
    return saludo
  
@decorador
def minuscula_decorado(texto, encoding):
    print(texto.lower() + f'{encoding}')


minuscula_decorado('Hola', ' utf8')