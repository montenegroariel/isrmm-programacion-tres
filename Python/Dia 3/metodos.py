texto = "Esto es un texto"
a = "Python"
b = "es"
c = "genial"
d = "\n".join([a, b, c])
mayuscula = texto.upper()
minuscula = texto.lower()
separar = texto.split()
buscar = texto.find("g")  # Not found = -1
reemplazar = texto.replace("Esto", "String")

print(mayuscula)
print(minuscula)
print(separar)
print(d)
print(buscar)
print(reemplazar)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = frase.replace("difícil", "fácil")
resultado = resultado.replace("mala", "buena")
print(resultado)
