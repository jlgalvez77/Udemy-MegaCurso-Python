# Funciones predefinidas en Python
def division(a, b):
    return divmod(a, b)

operacion = division(10, 3)
print(f'El resultado de la división es: {operacion}')
print(f'El cociente de la división es: {operacion[0]}')
print(f'El residuo de la división es: {operacion[1]}')


# Mator de n números
def mayor(*numeros):
    return max(numeros)

resultado = mayor(10, 20, 30, 40, 50)
print(f'El número mayor es: {resultado}')

# Menor de n números
def menor(*numeros):
    return min(numeros)

resultado = menor(10, 20, 30, 40, 50)
print(f'El número menor es: {resultado}')