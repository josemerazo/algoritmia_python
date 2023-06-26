# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:58:29 2023

@author: Docente
"""

numero = int(input("Ingrese un número: "))
acumulador = 0
for iterador in range(1,numero+1):
    acumulador += iterador
print("El acumulador: ", acumulador)

