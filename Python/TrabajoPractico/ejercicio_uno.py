def convertir_temperatura():
    print("===  El Convertidor de Temperatura ===")

    celsius = float(input("Ingrese la temperatura en grados C°: "))

    fahrenheit = (celsius * 9 / 5) + 32

    print(" La temperatura {celsius}°C equivalen en Fahrenheit a: ", fahrenheit, "°F")
convertir_temperatura()

