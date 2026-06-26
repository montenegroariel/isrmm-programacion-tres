mi_lista = ['a', 'b', 'c']
otra_lista = ['hola', 55, 6.1]
resultado = len(mi_lista) # Cantidad de elementos
indice = mi_lista[1:2]
print(type(mi_lista))
print(type(otra_lista))
print(resultado)
print(indice)

mi_lista3 = mi_lista + otra_lista # Concatenar dos listas
mi_lista3[0] = 'prueba'
print(mi_lista3)

mi_lista3.append('g') # Agrega elementos a la lista
print(mi_lista3)

mi_lista3.pop()  # quitar el ultimo elemento
print(mi_lista3)

eliminado = mi_lista3.pop(1)  # indice
print(mi_lista3)
print(eliminado)  # se guarda

ordenar = ['g', 'o', 'b', 'm', 'g']
ordenar.sort()  # None Type
print(ordenar)
ordenar.reverse()
print(ordenar)


