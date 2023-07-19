
"""
Hacer un programa con 5 funciones que haga la operación indicada enviando dos parámetros:
- sumar
- restar
- multiplicar
- dividir
- residuo

"""

def sumar(valor1,valor2):
    return valor1 + valor2

def restar(valor1,valor2):
    return valor1 - valor2

def multiplicar(valor1,valor2):
    return valor1 * valor2

def dividir(valor1,valor2):
    return valor1 / valor2

def residuo(valor1,valor2):
    return valor1 % valor2

numero1 = float(input("Ingrese valor 1:"))
numero2 = float(input("Ingrese valor 2:"))

while(True):
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Residuo")
    print("6.- Salir")
    opcion = input("Ingrese opcion: ")
    
    if opcion == "1":
        print("La suma es ",sumar(numero1,numero2))
    elif opcion=="2":
        print("La resta es ",restar(numero1,numero2))
    elif opcion=="3":
        print("La multiplicacion es ",multiplicar(numero1,numero2))    
    elif opcion=="4":
        print("La division es ",dividir(numero1,numero2))    
    elif opcion=="5":
        print("El residuo es ",residuo(numero1,numero2)) 
    elif opcion=="6":
        print("Gracias por usar el programa") 
        break;
    else:
        print("La opción ingresada es inválida ") 

        
    

