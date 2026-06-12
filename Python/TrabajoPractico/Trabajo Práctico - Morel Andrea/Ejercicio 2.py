edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Bienvenido,puede pasar a ver la película.")
else:
    faltan = 18 - edad
    print("No tiene la edad suficiente para ingresar.")
    print("Le faltan", faltan, "años para poder entrar.")