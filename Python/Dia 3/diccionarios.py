diccionario = {'c1': 'valor1', 'c2': 'valor2'}
print(diccionario)
resultado = diccionario['c1']
print(resultado)

cliente = {'nombre': 'Juan', 'apellido': 'Fuentes', 'peso': 88, 'talla': 1.76}
consulta = cliente['talla']
print(consulta)

dic = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic['c2'][1].upper())

dic['c3'] = 1234
print(dic)
dic['c2'] = 'B'
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())



