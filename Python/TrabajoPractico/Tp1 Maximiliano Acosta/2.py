n = int(input("ingrese su edad: "))
func = lambda n: n >= 18
if func(n) == True:
    print("Bienvenido")
else:
    faltante = lambda n:18-n
    print(f"no tiene la edad suficente de 18, usted tiene {n}. Le faltan {faltante(n)} año/s mas" )