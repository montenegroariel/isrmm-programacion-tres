mi_tuple = (1, 2, 3, 4) #Son inmutables;
print(type(mi_tuple))

mi_tuple = (1, 2, (10, 20), 4)
print(mi_tuple[2][1])

mi_tuple = list(mi_tuple)
print(type(mi_tuple))
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

t = (1, 2, 3)
x, y, z = t
print(t)

t = (1, 2, 3, 1)
print(t.count(1))  # Cantidad de repeticiones del elemento en la tupla
print(t.index(2))  # En que indice se encuentra

