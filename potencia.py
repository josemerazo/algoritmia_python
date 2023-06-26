# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 10:41:48 2023

@author: Docente
Pide al usuario que ingrese un número base y un exponente. utilizando un ciclo
mientras para calcular y mostrar el restulado de elvar el numero base a la 
potencia del exponente
"""

base=int(input("Ingrese número base: "))
exponente = int(input("Ingrese número exponente: "))
contador = 0
acumulador = 1
while(contador<exponente):
    acumulador = acumulador * base
    contador = contador + 1
print(base, " ^ ", exponente , " = ", acumulador)


