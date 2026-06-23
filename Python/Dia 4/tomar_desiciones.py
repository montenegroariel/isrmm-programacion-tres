mascota = "perro"
edad = 16
calificacion = 9

if mascota == "gato":
    print("tienes un gato")
elif mascota == "perro":
    print("tienes un perro")
else:
    print("no se que animal tienes")

if edad < 18:
    print('eres menor')
    if calificacion >= 6:
        print('aprobado')
    else:
        print('desaprobado')
else:
    print('eres adulto')
