import time

def cuenta_regresiva_for():
    print("=== Cuenta Regresiva con FOR ===")
    for i in range(10, 0, -1):
        print(i)
        time.sleep(0.5)
    print("¡Despegue!")

def cuenta_regresiva_while():
    print("=== Cuenta Regresiva con WHILE ===")
    i = 10
    while i > 0:
        print(i)
        time.sleep(0.5)
        i -= 1
    print("¡Despegue!")

cuenta_regresiva_for()
cuenta_regresiva_while()
