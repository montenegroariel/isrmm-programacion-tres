#Alumno: Gauna Gonzalo Exequiel

# Pedimos la edad al usuario
edad = int(input("Ingresá tu edad: "))

# Evaluamos la condición
if edad >= 18:
    print("¡Bienvenido/a al cine! Podés ingresar a ver la película.")
else:
    años_faltantes = 18 - edad
    print(f"Lo sentimos, no tenés la edad suficiente para ver esta película.")
    print(f"Te falta{'n' if años_faltantes > 1 else ''} {años_faltantes} año{'s' if años_faltantes > 1 else ''} para poder entrar.")