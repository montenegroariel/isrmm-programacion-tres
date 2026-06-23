texto = input("Ingrese un texto").lower()
letras = input("Ingrese tres caracteres").lower()

l1 = texto.count(letras[0])  # cuantas veces aparece cada letra
l2 = texto.count(letras[1])  # cuantas veces aparece cada letra
l3 = texto.count(letras[2])  # cuantas veces aparece cada letra
lista_texto = texto.split(' ')
palabras = len(lista_texto)  # cuantas palabras hay en total
primer_letra = texto[0]
ultima_letra = texto[-1]  # primer y ultima letra
lista_texto.reverse() # palabras en orden inverso
inverso = " ".join(lista_texto)
palabra_python = 'python' in texto  # aparece ¿python?
dic = {True:"si", False:"no"}

print(f"""Las letras aparecen en el texto la cantidad de {letras[0]}:{l1}; {letras[1]}:{l2};
{letras[2]}:{l3}. En total el texto contiene {palabras} palabras. La primer letra es {primer_letra} 
y la última {ultima_letra}. Texto Inverso: {inverso}.
¿Aparece la palabra python? {dic[palabra_python]}.""")



