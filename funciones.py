#dESARROLLAR UNA FUNCION QUE SUME DOS NÙMEROS Y 
# LUEGO INVOCARLA DESDE EL PROGRAMA PRINCIPAL

def ingresaEntero(mensaje):
    return int(input(mensaje))

def sumar(num1,num2):
    respuesta = num1 + num2 
    return respuesta

def restar(num1,num2):
    respuesta = num1 - num2 
    return respuesta

numero1 = ingresaEntero("Ingrese número 1: ")

numero2 = float(input("Ingrese número 2: "))

print("Suma: ", sumar(numero1, numero2))

respuesta_restar = restar(numero1, numero2)
print("Resta: ", restar(numero1, numero2))


