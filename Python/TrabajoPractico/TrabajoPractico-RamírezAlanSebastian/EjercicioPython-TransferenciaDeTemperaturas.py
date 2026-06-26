try:
    edad = int(input("Por favor, ingresa tu edad: "))
    if edad <= 0:
        print("Error: La edad debe ser un número mayor a cero.")
    elif edad >= 18:
        print("¡Bienvenido! Puedes pasar a ver la película.")
    else:
        anos_faltantes = 18 - edad
        print(f"Lo siento, no tienes la edad suficiente.")
        print(f"Te faltan {anos_faltantes} años para poder entrar.")

except ValueError:
    print("Error: Debes ingresar un número entero válido.")
