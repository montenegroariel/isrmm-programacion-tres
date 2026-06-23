lista = ['a', 'b', 'c']
indice = 0

for item in lista:  # bad
    print(indice, item)
    indice += 1


for indice, item in enumerate(lista):  # good
    print(indice, item)


for indice, item in enumerate(range(50, 55)):  # good
    print(indice, item)

tuples = list(enumerate(lista))
print(tuples)
print(tuples[0][1])