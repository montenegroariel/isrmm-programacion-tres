mi_texto = "Esta es una prueba"
resultado1 = mi_texto[-4]
resultado2 = mi_texto.index("a",5,11) #Busca la letra a entre la posicion 5 y 11 si no la encuentra se rompe
resultado2 = mi_texto.find("a",5,11) # Si no encuentra la letra siempre arroja -1

print(resultado1)
print(resultado2)
