# Suma de dos números
def suma(a, b):
    suma = a + b
    print(f"La suma de {a} + {b} es: {suma}")

suma(5, 7)

def sumaParametros():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    suma = a + b
    print(f"La suma de {a} + {b} es: {suma}")

sumaParametros()