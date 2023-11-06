# -*- coding: utf-8 -*-
"""
Cree un programa que utilice un switch para calcular el 
perímetro de diferentes figuras geométricas (cuadrado,
triángulo, círculo) basándose en la selección el usuario, 
luego mostrar la respuesta
"""

print("Calculo de perimetro de las figuras:")
print("1.- Cuadrilatero")
print("2.- Triangulo")
print("3.- Circulo")

opcion = input("Ingrese opcion:")
perimetro = 0
if(opcion=="1"): #Perimetro de un cuadrado
    lado1 = float(input("Ingrese lado 1: "))
    lado2 = float(input("Ingrese lado 2: "))
    lado3 = float(input("Ingrese lado 3: "))
    lado4 = float(input("Ingrese lado 4: "))
    perimetro = lado1 + lado2 + lado3 + lado4
else:
    if(opcion=="2"): #Perimetro de un triangulo
        lado1 = float(input("Ingrese lado 1: "))
        lado2 = float(input("Ingrese lado 2: "))
        lado3 = float(input("Ingrese lado 3: "))
        perimetro = lado1 + lado2 + lado3
    elif(opcion=="3"):
        radio = float(input("Ingrese radio: "))
        perimetro = 2 * 3.1416 * radio
    else:
        print("La opcion ingresada es incorrecta")
print("El perimetro de la figura ingresada es", perimetro)

