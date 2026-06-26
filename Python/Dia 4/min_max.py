
menor = min(58, 79, 24, 54, 101)
maximo = max(58, 79, 24, 54, 101)
print(menor)
print(maximo)


lista = [58, 79, 24, 54, 101]
print(f"El menor es {min(lista)} y el mayor es {max(lista)}")

nombres = ['Juan', 'Pablo', 'Alicia', 'Carlos']
nombre = 'Carlos'

print(min(nombres))  # orden alfabetico
print(min(nombre))  # buscar primero las mayusculas y despues las minusculas
print(min(nombre.lower()))

dic = {'C1': 45, 'C2': 11}
print(min(dic['C3']))
print(min(dic.values()))

