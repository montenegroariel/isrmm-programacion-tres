diccionario = {'c1': 'valor1', 'c2': 'valor2'}
print(diccionario)
#resultado = diccionario['2c1'] 
resultado = diccionario.get('c1','Codigo no encontrado') # Es recomendable usar get
print(resultado)

cliente = {'nombre': 'Juan', 'apellido': 'Fuentes', 'peso': 88, 'talla': 1.76}
consulta = cliente['talla']
print(consulta)

dic = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic['c2'][0].upper()) #Accedo al elemento de la lista

dic['c3'] = 1234
print(dic)
dic['c2'] = 'B'
print(dic)
print(dic.keys()) # claves
print(dic.values()) # valores
print(dic.items()) # elementos



