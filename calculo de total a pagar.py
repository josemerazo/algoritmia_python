# -*- coding: utf-8 -*-
"""

Escriba un programa en python que permita elegir entre 3 
productos (leche, huevo y harina), siendo los precios 
$1.10,$4.50, $0.50 repectivamente y solicite: 
la cantidad a comprar, si la cantidad del producto 
es mayor a 3, aplicar 15 por ciento de 
descuento
Permitir al usuario ingresar otro producto si desea, al finalizar
mostrar el total
"""
def calculo_precio(nombre, precio, descuento):
    print('Ha seleccionado ',nombre)
    cantidad = int(input("Ingrese cantidad: "))
    precio_unitario = precio
    if(cantidad >= 3):
        precio_unitario = precio_unitario * (1 - descuento)
    subtotal = cantidad * precio_unitario
    print("El subtotal de ",nombre, " es ", subtotal)
    return subtotal

opcion = ''
total = 0
while opcion!='4':
    print("El total de la cuenta es: $ ", total)
    print(" 1.- Leche  ---------------- $ 1.10")
    print(" 2.- Huevo  ---------------- $ 4.50")
    print(" 3.- Harina ---------------- $ 0.50")
    print(" 4.- Salir")
    opcion = input("Ingrese opción: ")
    if(opcion=='1'):
        subTotal = calculo_precio('leche', 1.10, 0.15)
        total = total + subTotal
    elif(opcion=='2'):
        subTotal = calculo_precio('huevo', 4.50, 0.15)
        total = total + subTotal
    elif(opcion=='3'):
        subTotal = calculo_precio('harina', 0.50, 0.15)
        total = total + subTotal

        
print("El total de la cuenta es ", total)
        



