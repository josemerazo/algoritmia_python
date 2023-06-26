# Calcula el  promedio de una lista de nùmeros, utilizando un ciclo repetitivo para recorrer el arregloen el siguiente arreglo [5,6,7,8,9,12,52], mostrar 


arreglo = [18,19,18,18,18,19,20]

acumulador = 0
for item in arreglo:
    acumulador += item
promedio = acumulador / len(arreglo)
print("El promedio es ", promedio)



