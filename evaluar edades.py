# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 09:53:12 2023

@author: Docente

Pide al usuario que ingrese su edad y determine 
en que categorìa de edad se encuentra (por
ejemplo niño, adolescente, adulto, adulto mayor
utilizando condicionales
Menor 10 años
Adolescente de 11 a 18 años
adulto de 18 a 64 años
adulto mayor de 65 en adelante
"""
edad = int(input("Ingrese edad: "))
if(edad<=10):
    print("Es un niño")
else:
    if(edad<18):
        print("Es Adolescente")
    else:
        if(edad<64):
            print("Es Adulto")
        else:
            print("Es Adulto mayor")
        

