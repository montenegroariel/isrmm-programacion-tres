# zip toma múltiples objetos iterables 
# (como listas, tuplas o strings) y los agrupa 
# en un iterador de tuplas. Cada tupla contiene 
# los elementos que comparten la misma posición 
# (índice) en los iterables
nombres = ['Ana', 'Julio', 'Valeria']
edades = [65, 29, 42]
ciudades = ['Lima', 'Madrid', 'Mexico']

combinados = zip(nombres, edades)
print(combinados)

combinados = list(zip(nombres, edades))
print(combinados)

combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")


