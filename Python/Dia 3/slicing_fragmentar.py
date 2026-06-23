texto = "ABCDEFGHIJKLM"
fragmento1 = texto[2:10] #Elementos del 2 al 10 (excluyente)
fragmento2 = texto[2:10:3] # Salta de a tres posiciones
fragmento3 = texto[::3] # Desde el principio hasta el final pero de a tres
fragmento4 = texto[::-1] # invierte el texto
print(fragmento1)
print(fragmento2)
print(fragmento3)
print(fragmento4)