# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:13:12 2023

@author: Docente
"""
# Generar un nùmero aleatorio del 1 al 10, 
# y solicitar un número al usuario hasta que lo adivine


import random

incognita = random.randint(1, 10)

while True:
    numero_ingresado = int(input("Ingrese un número del 1 al 10: "))
    if(numero_ingresado == incognita):
        break
    else:
        print("Has ingresado un número incorrecto")
print("Ha adivinado el número")
