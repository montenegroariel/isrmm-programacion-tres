lista = ['luis', 'laura', 'pablo', 'fede', 'julia']

for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print(f'{nombre} no comienza con l')

numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

palabra = 'python'
for letra in palabra:
    print(letra)

lista = [[1, 2], [3, 4], [5, 6]]
for a, b in lista:
    print(a)
    print(b)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for a, b in dic.items():
    print(a, b)

for item in dic.values():
    print(item)