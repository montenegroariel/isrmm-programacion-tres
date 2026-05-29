from random import randint
# Juego para explicar while
nombre = input('Dime tu nombre: ')
intento = 0
aleatorio = randint(1, 100)

print(f"""Hola {nombre} hemos seleccionado un número magico entre 1 y 100.
Debes adivinar cual es. Recuerda que tienes 8 intentos. Suerte!!""")
intentos = 8
# print(aleatorio)

while intentos != 0: #Mientras
    intento = int(input("Ingresa un número "))
    if intento not in range(1, 101):
        print('Ingresa un numero valido entre 1 y 100')
        continue
    elif intento > aleatorio:
        print(f'El número magico es menor a {intento}')
    elif intento < aleatorio:
        print(f'El número magico es mayor a {intento}')
    else:
        print(f'Felicidades el número magico es {aleatorio}, solo te tomo {8 - intentos} intentos')
        break
    intentos -= 1
if intento != aleatorio:
    print('Has agotado los intentos, suerte la proxima')
