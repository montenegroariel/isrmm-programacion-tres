edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Bienvenido a la función")
else:
    años_faltantes = 18 - edad
    print(f"No tiene la edad suficiente. Le faltan {años_faltantes} años para poder entrar")