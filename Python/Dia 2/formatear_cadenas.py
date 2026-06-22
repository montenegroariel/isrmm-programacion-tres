from random import shuffle
x = 10
y = 20

print("La suma de {} y {} es {}".format(x,y,x+y))

color = "rojo"
matricula = 456132

print(f"El auto es {color} y la matricula es {matricula}")

# lista inicial
palitos = ['-', '--', '---', '----']
# mezclar los palitos


def mezclar_palitos(lista):
    shuffle(lista)
    return lista


mezclar_palitos(palitos)


# pedrile intento
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un numero del 1 al 4 ')
        print(intento)
    return int(intento)


intento1 = probar_suerte()

# comprobar intento


def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print('A lavar los platos')
    else:
        print('Esta vez te a has salvado')
    print(f"Te ha tocado {lista[intento - 1]}")


palitos_mezclados = mezclar_palitos(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)

