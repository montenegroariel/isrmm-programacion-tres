serie = "N-02"

if serie == "N-01":
    print('Samsung')
elif serie == "N-02":
    print('Nokia')
elif serie == "N-03":
    print('Motorola')
else:
    print('Ninguno')

match serie: #Evalúa una expresión y la compara con múltiples patrones
    case "N-01":
        print('Samsung')
    case "N-02":
        print('Nokia')
    case "N-03":
        print('Motorola')
    case _:
        print('Ninguno')

cliente = {'nombre': 'Ariel', 'edad': 44, 'ocupacion': 'instructor'}
pelicula = {'titulo': 'matrix', 'ficha_tecnica': {'protagonista': 'Keanu Reeves', 'director': 'Lana y Lily'}}

elementos = [cliente, pelicula, 'libro']
for e in elementos:
    match e:
        case {'nombre': nombre, 'edad': edad, 'ocupacion': ocupacion}:
            print('Es un cliente')
            print(nombre, edad, ocupacion)
        case {'titulo':titulo, 'ficha_tecnica':{'protagonista':protagonista, 'director':director}}:
            print('Es una pelicula')
            print(titulo, protagonista, director)
        case _:
            print('no se')
