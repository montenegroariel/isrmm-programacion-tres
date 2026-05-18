mi_set = set([1, 2, 3, 4, 5])
print(type(mi_set))
print(mi_set)

otro_set = {1, 2, 3}
print(type(otro_set))
print(otro_set)

mi_set = set([1, 2, 3, 4, 5, 4, 4, 4, 4, 'a'])
print(type(mi_set))
print(mi_set)

print(len(mi_set))
print(2 in mi_set)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

s3.add(6)
print(s3)

s3.remove(3)
print(s3)

# s3.remove(7)  Error no existe el elemnto
s3.discard(7)  # Misma funcionalidad que remove pero si no existe no arroja error
print(s3)

aleatorio = s3.pop()  # Elimina de forma aleatoria
print(aleatorio)

s3.clear()  # Vacia el set
print(s3)

