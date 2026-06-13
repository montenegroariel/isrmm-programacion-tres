# Entrada de la edad
edad = int(input("Por favor, ingrese su edad: "))

# Verificación de la edad para el ingreso
if edad >= 18:
    print("¡Bienvenido! Puede pasar a ver la película.")
else:
    anios_faltantes = 18 - edad
    print(f"Lo siento, no tenés la edad suficiente para entrar.")
    print(f"Te faltan {anios_faltantes} años para poder ingresar.")