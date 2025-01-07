def pedirNumeros():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    return num1, num2


def sumaDos(a, b):
    suma = a + b
    return suma



valor1, valor2 = pedirNumeros()
resultado = sumaDos(valor1, valor2)
print(f"La suma de los números es: {resultado}")