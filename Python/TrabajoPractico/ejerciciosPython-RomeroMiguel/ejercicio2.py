edad = int(input("Ingrese su edad:"))

if edad >= 18: 
    print("Bienvenido, podes entrar a ver la pelicula.")
else:
    anos_faltantes = 18 - edad
    print("No podes entrar. Te falta", anos_faltantes, "años para poder entrar.")