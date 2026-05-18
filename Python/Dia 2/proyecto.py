nombre = input("¿Cúal es tu nombre?")
total_ventas = input("¿Cúal es el total de ventas?")
comision = round(int(total_ventas) * 13 / 100, 2)
print(f"El total de comision para {nombre} es {comision}")

