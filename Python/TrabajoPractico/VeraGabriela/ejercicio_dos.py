def asistente_cine():
    print("=== Asistente de Cine ===")
 
    edad = int(input("Ingresá tu edad: "))
 
    if edad >= 18:
        print("¡Bienvenido!Que disfrute la película.")
    else:
        anios_faltantes = 18 - edad
        print("Lo sentimos, todavía no tenés la edad suficiente.")
        print("Te faltan ", anios_faltantes, "años para poder ingresar.")
 
asistente_cine()
