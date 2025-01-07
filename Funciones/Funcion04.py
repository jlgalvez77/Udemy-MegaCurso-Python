def operaciones():
    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese otro número: "))
    if a > 0 and b > 0:
        suma = a + b
        resta = a - b
        multiplicacion = a * b
        division = a / b
        return suma, resta, multiplicacion, division
    else:
        print("Los números deben ser mayores a 0")

suma, resta, multiplicacion, division = operaciones()
print(f"La suma de los números es: {suma}")
print(f"La resta de los números es: {resta}")
print(f"La multiplicación de los números es: {multiplicacion}")
print(f"La división de los números es: {division}")