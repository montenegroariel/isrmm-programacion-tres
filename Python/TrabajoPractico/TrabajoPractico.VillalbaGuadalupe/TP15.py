#Ejercicio 1
celsius = float(input("Ingresá la temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")

#Ejercicio 2
edad = int(input("¿Cuántos años tenés? "))
if edad >= 18:
    print("¡Bienvenido! Disfruta la pelicula.")
else:
    anios_faltantes = 18 - edad
    print(f"No estas apto. Te faltan {anios_faltantes} año(s) para poder ver esta película.")

#Ejercicio 3
numero = 10
while numero >= 1:      
    print(numero)
    numero = numero - 1
print("¡Despegue!")