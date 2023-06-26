# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:41:34 2023

@author: Docente
"""

# Muestre la tabla de multiplicar de un nùmero,
# del 0 hasta otro nùmero ingresado

print("Tabla de Multiplicar")
numero = int(input("Ingrese número: "))

limite_tabla  = int(input("Ingrese número límite: "))
for i in range(0,limite_tabla+1):
    print(numero, " X ", i, " = ", numero*i)
    
    
    