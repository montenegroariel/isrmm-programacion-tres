mi_lista = ['a', 'b', 'c']
otra_lista = ['hola', 55, 6.1]
resultado = len(mi_lista)
indice = mi_lista[0:]
print(type(mi_lista))
print(type(otra_lista))
print(resultado)
print(indice)

mi_lista3 = mi_lista + otra_lista
mi_lista3[0] = 'alfa'
print(mi_lista3)

mi_lista3.append('g')
print(mi_lista3)

mi_lista3.pop()  # ultimo elemento
print(mi_lista3)

eliminado = mi_lista3.pop(0)  # indice
print(mi_lista3)
print(eliminado)  # se guarda

ordenar = ['g', 'o', 'b', 'm', 'g']
ordenar.sort()  # None Type
print(ordenar)
ordenar.reverse()
print(ordenar)


