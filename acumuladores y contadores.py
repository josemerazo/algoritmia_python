# -*- coding: utf-8 -*-
"""
Escriba un programa que permita el ingreso 
de n números y 
vaya acumulando la suma de los mismos, hasta
que el usuario ingrese 0.
Al finalizar se debe mostrar la suma 
total de los números ingresados
Y cuantos números ingresó el usuario
"""

numero = 1
acumulador = 0
contador = 0
cont_multiplos3 = 0
while numero!=0:
    numero = int(input("Ingrese número: "))
    acumulador = acumulador + numero
    contador = contador + 1
    if(numero%3 == 0 != numero > 0):
        cont_multiplos3 = cont_multiplos3 + 1
print("La suma total es", acumulador)
print("La cantidad de números ingresados es", contador)
print("La cantidad de números múltiplos de 3 es", cont_multiplos3)
    


