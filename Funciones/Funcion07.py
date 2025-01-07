# Mayor de dos números
def mayorDos(num1, num2):
    if(type(num1) == int or type(num1) == float) and (type(num2) == int or type(num2) == float):
        if num1 > num2:
            return num1
        elif num1 == num2:
            return "Los números son iguales"
        else:
            return num2
    else:
        return "Los valores ingresados no son números"
    
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

resultado = mayorDos(num1, num2)
print(f"El número mayor es: {resultado}")