# -*- coding: utf-8 -*-
"""

Escriba un algoritmo que sume los números ingresados
 por el usuario 
y cuando la suma sea superior a 100 deje de 
pedir números y muestre el total.
"""

acumulador = 0

while acumulador <= 100:
    numero = int(input("Ingrese número: "))
    acumulador = acumulador + numero
print("La suma de los números es: ", acumulador)

