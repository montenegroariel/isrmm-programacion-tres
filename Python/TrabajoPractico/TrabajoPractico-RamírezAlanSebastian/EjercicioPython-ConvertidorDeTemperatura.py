while True:
    print("\n--- Conversor de Celsius a Fahrenheit ---")
    entrada = input("Ingresa la temperatura en Celsius (o escribe 'salir'): ")
    if entrada.lower() == 'salir':
        break
    try:
        celsius = float(entrada)
        fahrenheit = (celsius * (9 / 5)) + 32
        print(f"Resultado: {celsius}°C equivalen a {fahrenheit:.2f}°F")     
    except ValueError:
        print("Pon un número válido por favor.")
